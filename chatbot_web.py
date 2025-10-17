# chatbot_web.py
import logging
import re
from flask import Flask, request, jsonify, session, render_template
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_cors import CORS
import google.generativeai as genai
from datetime import timedelta

# Impor dari file-file yang sudah dipisah
import config
from utils import log_activity, search_knowledge_base, get_follow_ups, parse_bot_response
from database_ID import AUTOCOMPLETE_TERMS_ID
from database_EN import AUTOCOMPLETE_TERMS_EN

# --- Konfigurasi Google Gemini ---
if config.GOOGLE_API_KEY:
    genai.configure(api_key=config.GOOGLE_API_KEY)

# --- Flask App & Routes ---
app = Flask(__name__)
CORS(app)
app.secret_key = config.FLASK_SECRET_KEY
app.permanent_session_lifetime = timedelta(minutes=7)

limiter = Limiter(get_remote_address, app=app, default_limits=["200 per day", "50 per hour"])

def format_history_for_prompt(history):
    if not history:
        return ""
    formatted_text = ""
    for message in history:
        role = "User" if message["role"] == "user" else "Virtual Assistant"
        content = message["content"]
        
        if isinstance(content, str) and content.startswith("{"):
            try:
                import ast
                content_dict = ast.literal_eval(content)
                content = content_dict.get('content', '') or content_dict.get('title', '')
            except (ValueError, SyntaxError):
                 pass
        
        clean_content = re.sub('<[^<]+?>', '', str(content))
        formatted_text += f"{role}: {clean_content}\n"
    return formatted_text

@app.before_request
def make_session_permanent():
    session.permanent = True

@app.route("/")
def index():
    if "history" not in session:
        session["history"] = []
    # Atur bahasa default ke 'id' jika belum ada
    if 'lang' not in session:
        session['lang'] = 'id'
    return render_template("index.html")

@app.route("/autocomplete")
def autocomplete():
    lang = session.get('lang', 'id')
    if lang == 'en':
        return jsonify(AUTOCOMPLETE_TERMS_EN)
    return jsonify(AUTOCOMPLETE_TERMS_ID)


# Endpoint baru untuk mengganti bahasa
@app.route("/language", methods=["POST"])
def set_language():
    data = request.json
    lang = data.get("lang", "id")
    if lang in ["en", "id"]:
        session["lang"] = lang
        session.pop("history", None) # Hapus riwayat chat saat ganti bahasa
        return jsonify({"status": "success", "message": f"Language changed to {lang}"})
    return jsonify({"status": "error", "message": "Invalid language"}), 400


@app.route("/chat", methods=["POST"])
@limiter.limit("10 per minute")
def chat():
    user_ip = get_remote_address()
    try:
        # Dapatkan bahasa dari session, default ke 'id'
        lang = session.get('lang', 'id')

        data = request.json
        user_message = data.get("message", "").strip()
        if not user_message:
            error_message = "Error: Question cannot be empty." if lang == 'en' else "Error: Pertanyaan tidak boleh kosong."
            return jsonify({"status": "error", "response": {"type": "paragraph", "content": error_message}}), 400
        
        if "history" not in session:
            session["history"] = []

        is_more_details_request = user_message.lower() in ['more details', 'bisa lebih detail?', 'jelaskan lebih detail']
        
        original_query = user_message
        if is_more_details_request:
            if len(session.get("history", [])) >= 2:
                for i in range(len(session["history"]) - 1, -1, -1):
                    if session["history"][i]["role"] == "user":
                        original_query = session["history"][i]["content"]
                        break
            else:
                no_question_message = "Please ask a question first before requesting more details." if lang == 'en' else "Silakan ajukan pertanyaan terlebih dahulu sebelum meminta detail lebih lanjut."
                return jsonify({
                    "status": "success",
                    "source": "local",
                    "response": {"type": "paragraph", "content": no_question_message},
                    "follow_ups": None
                })
        else:
            session["history"].append({"role": "user", "content": user_message})
            session.modified = True
            
        json_response = {"status": "success", "source": "local", "response": {}, "follow_ups": None}
        
        # Kirimkan `lang` ke search_knowledge_base
        local_answer = None
        if not is_more_details_request:
            local_answer = search_knowledge_base(original_query, lang)
        
        if local_answer:
            json_response["response"] = local_answer
            log_activity(user_ip, original_query, "local", str(local_answer))
            session["history"].append({"role": "bot", "content": str(local_answer)})
            session.modified = True
        else:
            if not config.GOOGLE_API_KEY:
                raise ValueError("GOOGLE_API_KEY is not set.")
            
            # Pilih system prompt berdasarkan bahasa di session
            system_prompt = config.SYSTEM_PROMPT_EN if lang == 'en' else config.SYSTEM_PROMPT_ID

            json_response["source"] = "api"
            model = genai.GenerativeModel(model_name=config.GEMINI_MODEL, system_instruction=system_prompt)
            
            gemini_history = [{"role": ("model" if msg["role"] == "bot" else msg["role"]), "parts": [{"text": str(msg["content"]) }]} for msg in session.get("history", [])[:-1]]
            
            chat_session = model.start_chat(history=gemini_history)
            response = chat_session.send_message(original_query)
            
            bot_message = response.text.strip()
            session["history"].append({"role": "bot", "content": bot_message})
            session.modified = True

            json_response["response"] = parse_bot_response(bot_message)
            log_activity(user_ip, original_query, "api", bot_message)
        
        json_response["response"]["footer"] = {"text": "kemlu.go.id", "link": "https://kemlu.go.id"}
        
        # Kirimkan `lang` ke get_follow_ups
        follow_ups = get_follow_ups(original_query, lang)
        if follow_ups:
            json_response["follow_ups"] = follow_ups
        
        return jsonify(json_response)

    except Exception as e:
        logging.error(f"API/Config error for IP {user_ip}: {e}")
        error_message = "⚠️ Sorry, there was a system error. Please try again later." if session.get('lang') == 'en' else "⚠️ Maaf, terjadi gangguan pada sistem. Silakan coba lagi nanti."
        return jsonify({"status": "error", "response": {"type": "paragraph", "content": error_message}}), 503

@app.route("/reset", methods=["POST"])
def reset():
    session.pop("history", None)
    return jsonify({"status": "success", "message": "Chat history cleared."})

@app.route("/feedback", methods=["POST"])
def feedback():
    data = request.json
    feedback_text = data.get("feedback", "").strip()
    if feedback_text:
        with open("feedback.log", "a", encoding="utf-8") as f:
            f.write(f"{logging.Formatter('%(asctime)s').format(logging.makeLogRecord({}))} - IP: {get_remote_address()} | Feedback: {feedback_text}\n")
        return jsonify({"status": "success"})
    return jsonify({"status": "error", "message": "Feedback cannot be empty."}), 400

@app.route("/log_reaction", methods=["POST"])
def log_reaction():
    data = request.json
    reaction = data.get("reaction")
    message = data.get("message", "")
    if reaction and message:
        with open("reaction.log", "a", encoding="utf-8") as f:
            f.write(f"{logging.Formatter('%(asctime)s').format(logging.makeLogRecord({}))} - IP: {get_remote_address()} | Reaction: {reaction} | Message: \"{message}\"\n")
        return jsonify({"status": "success"})
    return jsonify({"status": "error", "message": "Invalid reaction data."}), 400

@app.route("/summarize", methods=["POST"])
def summarize():
    user_ip = get_remote_address()
    try:
        history = session.get("history", [])
        if len(history) < 2:
            return jsonify({"summary": "Tidak ada percakapan yang cukup untuk diringkas."})

        conversation_text = format_history_for_prompt(history)
        
        prompt = f"""
        Anda adalah asisten yang ahli dalam membuat ringkasan. Berdasarkan riwayat percakapan berikut antara seorang pengguna dan asisten virtual, buatkan ringkasan singkat dari poin-poin utama yang didiskusikan. Fokus pada pertanyaan pengguna dan jawaban paling penting dari asisten.

        Percakapan:
        {conversation_text}

        Ringkasan:
        """

        model = genai.GenerativeModel(model_name=config.GEMINI_MODEL)
        response = model.generate_content(prompt)
        
        summary = response.text.strip()
        log_activity(user_ip, "summarize_request", "api", summary)
        
        return jsonify({"summary": summary})

    except Exception as e:
        logging.error(f"Summarize error for IP {user_ip}: {e}")
        return jsonify({"error": "Gagal membuat ringkasan."}), 500

@app.route("/draft_email", methods=["POST"])
def draft_email():
    user_ip = get_remote_address()
    try:
        history = session.get("history", [])
        if len(history) < 2:
            return jsonify({"draft": "Tidak ada percakapan yang cukup untuk membuat draf email."})

        conversation_text = format_history_for_prompt(history)
        
        prompt = f"""
        Anda adalah asisten yang sangat baik dalam menulis email formal. Berdasarkan riwayat percakapan berikut, buatkan draf email formal dalam Bahasa Indonesia yang sopan kepada perwakilan RI yang relevan (KBRI/KJRI). 
        - Identifikasi masalah utama pengguna.
        - Sebutkan informasi atau solusi kunci yang diberikan oleh asisten.
        - Buat email yang jelas dan ringkas.
        - Akhiri dengan salam penutup dan placeholder "[Nama Lengkap Anda]" untuk diisi oleh pengguna.
        - Jika topik percakapan tidak cocok untuk email formal (misalnya, hanya sapaan), berikan respons yang menyatakan hal tersebut.

        Percakapan:
        {conversation_text}

        Draf Email:
        """
        
        model = genai.GenerativeModel(model_name=config.GEMINI_MODEL)
        response = model.generate_content(prompt)
        
        draft = response.text.strip()
        log_activity(user_ip, "draft_email_request", "api", draft)
        
        return jsonify({"draft": draft})

    except Exception as e:
        logging.error(f"Draft email error for IP {user_ip}: {e}")
        return jsonify({"error": "Gagal membuat draf email."}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)