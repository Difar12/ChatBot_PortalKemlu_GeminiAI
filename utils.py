# chatbot-apikemlu/utils.py

import logging
import re
from logging.handlers import RotatingFileHandler

# Impor dari kedua file database
from database_ID import (
    KNOWLEDGE_BASE_ID,
    CITY_TO_COUNTRY as CITY_TO_COUNTRY_ID, # Diubah untuk kejelasan
    FOLLOW_UP_SUGGESTIONS_ID,
    PETA_LOKASI as PETA_LOKASI_ID
)
from database_EN import (
    KNOWLEDGE_BASE_EN,
    CITY_TO_COUNTRY as CITY_TO_COUNTRY_EN, # Ditambahkan
    FOLLOW_UP_SUGGESTIONS_EN,
    PETA_LOKASI as PETA_LOKASI_EN
)


# --- Logging ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
log_handler = RotatingFileHandler('chatbot_activity.log', maxBytes=10*1024*1024, backupCount=5, encoding='utf-8')
log_handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
activity_logger = logging.getLogger('activity_logger')
activity_logger.setLevel(logging.INFO)
activity_logger.addHandler(log_handler)

def log_activity(ip, query, source, response):
    clean_response = ' '.join(str(response).splitlines())
    activity_logger.info(f"IP: {ip} | Query: \"{query}\" | Source: {source} | Response: \"{clean_response}\"")

# --- Knowledge Base Function (Updated for multilingual support) ---
def search_knowledge_base(query, lang='id'):
    """
    Mencari knowledge base lokal berdasarkan bahasa yang dipilih.
    """
    normalized_query = query.lower().strip()

    if lang == 'id':
        KNOWLEDGE_BASE = KNOWLEDGE_BASE_ID
        PETA_LOKASI = PETA_LOKASI_ID
        CITY_TO_COUNTRY = CITY_TO_COUNTRY_ID # Menggunakan kamus ID
        # --- LOGIKA KHUSUS BAHASA INDONESIA ---
        if "peta" in normalized_query or "lokasi" in normalized_query:
            for country, map_link in PETA_LOKASI.items():
                if country in normalized_query:
                    return {
                        "type": "paragraph",
                        "content": f"Berikut adalah tautan peta untuk perwakilan RI di {country.title()}:<br><a href='{map_link}' target='_blank' style='color:blue;'>Buka di Google Maps</a>"
                    }
        if "syarat visa" in normalized_query and ("wna" in normalized_query or "asing" in normalized_query):
            return KNOWLEDGE_BASE.get("syarat visa wna")

    else: # lang == 'en'
        KNOWLEDGE_BASE = KNOWLEDGE_BASE_EN
        PETA_LOKASI = PETA_LOKASI_EN
        CITY_TO_COUNTRY = CITY_TO_COUNTRY_EN # Menggunakan kamus EN
        # --- ENGLISH-SPECIFIC LOGIC ---
        if "map" in normalized_query or "location" in normalized_query:
            for country, map_link in PETA_LOKASI.items():
                if country in normalized_query:
                    return {
                        "type": "paragraph",
                        "content": f"Here is the map link for the Indonesian mission in {country.title()}:<br><a href='{map_link}' target='_blank' style='color:blue;'>Open in Google Maps</a>"
                    }
        if "visa requirements" in normalized_query and "foreigner" in normalized_query:
            return KNOWLEDGE_BASE.get("visa requirements for foreigners")


    # --- LOGIKA UMUM (berlaku untuk kedua bahasa) ---
    # Pencarian berdasarkan kota (CITY_TO_COUNTRY sekarang dinamis)
    for city, country_key in CITY_TO_COUNTRY.items():
        if re.search(r'\b' + re.escape(city) + r'\b', normalized_query):
            return KNOWLEDGE_BASE.get(country_key)

    # General keyword search (Updated for flexibility)
    for keyword, answer in KNOWLEDGE_BASE.items():
        # Split keyword into individual words and check if all are in the query
        keyword_words = keyword.split()
        if all(re.search(r'\b' + re.escape(word) + r'\b', normalized_query) for word in keyword_words):
            return answer

# --- Follow-up Logic (Updated for multilingual support) ---
def get_follow_ups(query, lang='id'):
    """
    Finds follow-up question suggestions based on the selected language.
    """
    FOLLOW_UP_SUGGESTIONS = FOLLOW_UP_SUGGESTIONS_ID if lang == 'id' else FOLLOW_UP_SUGGESTIONS_EN
    normalized_query = query.lower().strip()
    best_match = None
    longest_match = 0
    for keyword, data in FOLLOW_UP_SUGGESTIONS.items():
        if keyword in normalized_query:
            if len(keyword) > longest_match:
                longest_match = len(keyword)
                best_match = data
    return best_match

# --- Parse Response Function (No changes needed here) ---
def parse_bot_response(text: str) -> dict:
    """
    Cleans the response from the AI, detects bullet points and numbering,
    and formats it as HTML.
    """
    if not text.strip():
        return {"type": "paragraph", "content": "Maaf, saya tidak dapat memberikan jawaban saat ini."}

    match = re.search(r'```html(.*)```', text, re.DOTALL | re.IGNORECASE)
    if match:
        text = match.group(1).strip()

    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)

    lines = text.split('\n')
    html_output = []
    in_ul_list = False
    in_ol_list = False

    for line in lines:
        stripped_line = line.strip()
        if stripped_line.startswith(('* ', '- ')):
            if in_ol_list:
                html_output.append('</ol>')
                in_ol_list = False
            if not in_ul_list:
                html_output.append('<ul>')
                in_ul_list = True
            list_item = stripped_line[2:]
            html_output.append(f'<li>{list_item}</li>')
        elif re.match(r'^\d+\.\s', stripped_line):
            if in_ul_list:
                html_output.append('</ul>')
                in_ul_list = False
            if not in_ol_list:
                html_output.append('<ol>')
                in_ol_list = True
            list_item = re.sub(r'^\d+\.\s', '', stripped_line)
            html_output.append(f'<li>{list_item}</li>')
        else:
            if in_ul_list:
                html_output.append('</ul>')
                in_ul_list = False
            if in_ol_list:
                html_output.append('</ol>')
                in_ol_list = False
            if stripped_line:
                 html_output.append(f'<p>{line}</p>')

    if in_ul_list:
        html_output.append('</ul>')
    if in_ol_list:
        html_output.append('</ol>')

    final_html = ''.join(html_output)
    return {"type": "paragraph", "content": final_html}