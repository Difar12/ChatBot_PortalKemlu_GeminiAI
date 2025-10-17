# database_EN.py

# --- Knowledge Base & Follow-ups ---

PETA_LOKASI = {
    "afghanistan": "http://googleusercontent.com/maps/google.com/0",
    "south africa": "https://maps.google.com/?q=Embassy+of+Indonesia+in+Pretoria",
    "united states": "https://maps.google.com/?q=Embassy+of+Indonesia+in+Washington,D.C.",
    "australia": "http://googleusercontent.com/maps/google.com/3",
    "netherlands": "http://googleusercontent.com/maps/google.com/4",
    "china": "http://googleusercontent.com/maps/google.com/5",
    "united kingdom": "http://googleusercontent.com/maps/google.com/6",
    "japan": "http://googleusercontent.com/maps/google.com/7",
    "germany": "http://googleusercontent.com/maps/google.com/8",
    "malaysia": "http://googleusercontent.com/maps/google.com/9",
    "singapore": "http://googleusercontent.com/maps/google.com/10",
    "algeria": "https://maps.google.com/?q=Embassy+of+Indonesia+in+Algiers",
    "saudi arabia": "http://googleusercontent.com/maps/google.com/12",
    "argentina": "http://googleusercontent.com/maps/google.com/13",
    "austria": "http://googleusercontent.com/maps/google.com/14",
    "azerbaijan": "https://maps.google.com/?q=Embassy+of+Indonesia+in+Baku",
    "kuwait": "http://googleusercontent.com/maps/google.com/16",
    "bangladesh": "https://maps.google.com/?q=Embassy+of+Indonesia+in+Dhaka",
    "belgium": "http://googleusercontent.com/maps/google.com/18",
    "bosnia and herzegovina": "https://maps.google.com/?q=Embassy+of+Indonesia+in+Budapest",
    "brazil": "http://googleusercontent.com/maps/google.com/20",
    "brunei darussalam": "https://maps.google.com/?q=Embassy+of+Indonesia+in+Bandar+Seri+Begawan",
    "bulgaria": "https://maps.google.com/?q=Embassy+of+Indonesia+in+Sofia",
    "czech republic": "https://maps.google.com/?q=Embassy+of+Indonesia+in+Prague",
    "chile": "https://maps.google.com/?q=Embassy+of+Indonesia+in+Santiago",
    "denmark": "http://googleusercontent.com/maps/google.com/25",
    "peru": "http://googleusercontent.com/maps/google.com/26",
    "egypt": "http://googleusercontent.com/maps/google.com/27",
    "ethiopia": "https://maps.google.com/?q=Embassy+of+Indonesia+in+Addis+Ababa",
    "fiji": "http://googleusercontent.com/maps/google.com/29",
    "philippines": "https://maps.google.com/?q=Embassy+of+Indonesia+in+Manila",
    "finland": "http://googleusercontent.com/maps/google.com/31",
    "hungary": "https://maps.google.com/?q=Embassy+of+Indonesia+in+Budapest",
    "india": "https://maps.google.com/?q=Embassy+of+Indonesia+in+New+Delhi",
    "iraq": "http://googleusercontent.com/maps/google.com/33",
    "iran": "http://googleusercontent.com/maps/google.com/34",
    "italy": "https://maps.google.com/?q=Embassy+of+Indonesia+in+Rome",
    "jordan": "https://maps.google.com/?q=Embassy+of+Indonesia+in+Amman",
    "cambodia": "http://googleusercontent.com/maps/google.com/37",
    "canada": "https://maps.google.com/?q=Embassy+of+Indonesia+in+Ottawa",
    "kenya": "http://googleusercontent.com/maps/google.com/39",
    "south korea": "https://maps.google.com/?q=Embassy+of+Indonesia+in+Seoul",
    "north korea": "https://maps.google.com/?q=Embassy+of+Indonesia+in+Pyongyang",
    "croatia": "https://maps.google.com/?q=Embassy+of+Indonesia+in+Budapest",
    "cuba": "https://maps.google.com/?q=Embassy+of+Indonesia+in+Havana",
    "laos": "https://maps.google.com/?q=Embassy+of+Indonesia+in+Vientiane",
    "lebanon": "http://googleusercontent.com/maps/google.com/44",
    "libya": "https://maps.google.com/?q=Embassy+of+Indonesia+in+Tripoli",
    "morocco": "https://maps.google.com/?q=Embassy+of+Indonesia+in+Rabat",
    "mexico": "https://maps.google.com/?q=Embassy+of+Indonesia+in+Mexico+City",
    "myanmar": "https://maps.google.com/?q=Embassy+of+Indonesia+in+Yangon",
    "namibia": "https://maps.google.com/?q=Embassy+of+Indonesia+in+Windhoek",
    "nigeria": "https://maps.google.com/?q=Embassy+of+Indonesia+in+Abuja",
    "norway": "https://maps.google.com/?q=Embassy+of+Indonesia+in+Oslo",
    "pakistan": "https://maps.google.com/?q=Embassy+of+Indonesia+in+Islamabad",
    "papua new guinea": "https://maps.google.com/?q=Embassy+of+Indonesia+in+Port+Moresby",
    "united arab emirates": "https://maps.google.com/?q=Embassy+of+Indonesia+in+Abu+Dhabi",
    "poland": "https://maps.google.com/?q=Embassy+of+Indonesia+in+Warsaw",
    "portugal": "https://maps.google.com/?q=Embassy+of+Indonesia+in+Lisbon",
    "france": "https://maps.google.com/?q=Embassy+of+Indonesia+in+Paris",
    "qatar": "https://maps.google.com/?q=Embassy+of+Indonesia+in+Doha",
    "romania": "https://maps.google.com/?q=Embassy+of+Indonesia+in+Bucharest",
    "russia": "https://maps.google.com/?q=Embassy+of+Indonesia+in+Moscow",
    "new zealand": "https://maps.google.com/?q=Embassy+of+Indonesia+in+Wellington",
    "senegal": "http://googleusercontent.com/maps/google.com/62",
    "serbia": "https://maps.google.com/?q=Embassy+of+Indonesia+in+Budapest",
    "slovakia": "https://maps.google.com/?q=Embassy+of+Indonesia+in+Bratislava",
    "spain": "https://maps.google.com/?q=Embassy+of+Indonesia+in+Madrid",
    "sri lanka": "https://maps.google.com/?q=Embassy+of+Indonesia+in+Colombo",
    "sudan": "https://maps.google.com/?q=Embassy+of+Indonesia+in+Khartoum",
    "syria": "https://maps.google.com/?q=Embassy+of+Indonesia+in+Damascus",
    "suriname": "https://maps.google.com/?q=Embassy+of+Indonesia+in+Paramaribo",
    "sweden": "https://maps.google.com/?q=Embassy+of+Indonesia+in+Stockholm",
    "switzerland": "https://maps.google.com/?q=Embassy+of+Indonesia+in+Bern",
    "tanzania": "https://maps.google.com/?q=Embassy+of+Indonesia+in+Dar+es+Salaam",
    "thailand": "https://maps.google.com/?q=Embassy+of+Indonesia+in+Bangkok",
    "timor leste": "https://maps.google.com/?q=Embassy+of+Indonesia+in+Dili",
    "tunisia": "https://maps.google.com/?q=Embassy+of+Indonesia+in+Tunis",
    "turkey": "https://maps.google.com/?q=Embassy+of+Indonesia+in+Ankara",
    "ukraine": "https://maps.google.com/?q=Embassy+of+Indonesia+in+Kyiv",
    "uzbekistan": "https://maps.google.com/?q=Embassy+of+Indonesia+in+Tashkent",
    "vatican": "https://maps.google.com/?q=Embassy+of+Indonesia+to+the+Holy+See",
    "venezuela": "http://googleusercontent.com/maps/google.com/79",
    "vietnam": "http://googleusercontent.com/maps/google.com/80",
    "yemen": "http://googleusercontent.com/maps/google.com/81",
    "greece": "https://maps.google.com/?q=Embassy+of+Indonesia+in+Athens",
    "zimbabwe": "https://maps.google.com/?q=Embassy+of+Indonesia+in+Harare"
}

KNOWLEDGE_BASE_EN = {
    # --- General Info Ministry of Foreign Affairs (MFA) ---
    "address": {
        "type": "paragraph",
        "content": "<strong>Address of the Ministry of Foreign Affairs of the Republic of Indonesia:</strong><br>Jalan Taman Pejambon No. 6, Central Jakarta 10110, Indonesia.<br><a href='https://maps.google.com/?q=Kementerian+Luar+Negeri+RI' target='_blank' style='color:blue;'>View Map</a>"
    },
    "official website": {
        "type": "paragraph",
        "content": "The official website of the Indonesian Ministry of Foreign Affairs is <a href='https://www.kemlu.go.id' target='_blank' style='color:blue;'>www.kemlu.go.id</a>."
    },
    "emergency contact": {
        "type": "paragraph",
        "content": "For emergencies, you can contact the <strong>Indonesian Citizen Protection Hotline</strong> via WhatsApp at: <strong>+62 812-9007-0027</strong>."
    },
    "safe travel": {
        "type": "paragraph",
        "content": "<strong>Safe Travel</strong> is the official application from the Ministry of Foreign Affairs that provides security information, data on Indonesian representatives, and emergency features for Indonesian citizens abroad. You can download it from the App Store or Google Play."
    },

    # --- Passport Services ---
    "renew passport": {
        "type": "list",
        "title": "To renew an Indonesian citizen's passport abroad:",
        "items": [
            "This can be done at the nearest <strong>Indonesian Embassy/Consulate General</strong> in your country.",
            "You are advised to bring your <strong>old passport</strong> that is about to expire.",
            "Also, include <strong>supporting identity documents</strong> such as a local residence permit card or other proof of identity."
        ]
    },
    "lost passport": {
        "type": "list",
        "title": "If your passport is lost while abroad, immediately take these steps:",
        "items": [
            "Report it to the <strong>local police authority</strong> to obtain an official loss report.",
            "After that, immediately contact the <strong>nearest Indonesian Embassy/Consulate General</strong> to process an <strong>Emergency Travel Document (SPLP)</strong> as a temporary replacement for your passport."
        ]
    },

    # --- Visa Services ---
    "visit visa": {
        "type": "list",
        "title": "General procedure for applying for a visit visa to Indonesia:",
        "items": [
            "<strong>Determine the Visa Type:</strong> Make sure you choose the visa type that matches the purpose of your visit (e.g., tourist, business, or family).",
            "<strong>Complete the Documents:</strong> Gather all required documents, such as a <strong>valid passport</strong>, <strong>application form</strong>, passport photo, and proof of funds.",
            "<strong>Submit the Application:</strong> You can submit your visa application through the <strong>Embassy/Consulate General of the Republic of Indonesia</strong> in your country.",
            "<strong>Pay the Visa Fee:</strong> Make the visa application fee payment according to the applicable regulations.",
            "<strong>Wait for Approval:</strong> The visa approval processing time can vary depending on the Indonesian representative office and the completeness of your documents."
        ]
    },
    "visa extension abroad": {
        "type": "list",
        "title": "Procedure for visa extension abroad:",
        "items": [
            "The extension must be done through the <strong>Embassy/Consulate General of the Republic of Indonesia (KBRI/KJRI)</strong> in the country where you are located.",
            "Procedures and requirements <strong>vary</strong> depending on the type of visa and local regulations.",
            "Please visit the official website of the KBRI/KJRI in your country to get accurate information about the required documents, fees, and processing times.",
            "<strong>Important:</strong> Apply for the extension well before your visa expires to avoid immigration issues."
        ]
    },
    "visa requirements for foreigners": {
        "type": "list",
        "title": "In general, here are the requirements for a visa application for foreigners:",
        "items": [
            "<strong>Valid Passport:</strong> Ensure the passport is valid for at least 6 months upon arrival in Indonesia.",
            "<strong>Visa Application Form:</strong> Fill out the visa application form completely and correctly.",
            "<strong>Passport Photo:</strong> Provide a recent color passport photo according to the specified requirements.",
            "<strong>Proof of Funds:</strong> Show proof of sufficient funds to cover living expenses while in Indonesia.",
            "<strong>Return Ticket:</strong> Have a ticket to return to your home country or a ticket to continue your journey to another country.",
            "<strong>Purpose of Visit:</strong> Attach supporting documents according to your purpose, such as an invitation letter, hotel booking confirmation, or sponsorship letter."
        ]
    },
    "do i need a visa": {
        "type": "paragraph",
        "content": "The need for a visa to enter Indonesia <strong>depends on your nationality</strong>. Some countries have visa-free agreements, while others require a visa that must be applied for before arrival or can use a Visa on Arrival (VoA).<br><br>For the most accurate and up-to-date information, please check the visa policy applicable to your country on the official website <a href='https://www.kemlu.go.id' target='_blank' style='color:blue;'>kemlu.go.id</a> or contact the nearest Indonesian Representative."
    },
    "online visa": {
        "type": "paragraph",
        "content": "Currently, a <strong>fully online</strong> tourist visa application system is not available for all countries. The visa application procedure is generally still carried out through the <strong>Embassy/Consulate General of the Republic of Indonesia (KBRI/KJRI)</strong> in your country.<br><br>To find out the correct procedure, including whether any partial online application facilities are available, please visit the official website of the KBRI/KJRI in your country. Always refer to the official site <a href='https://www.kemlu.go.id' target='_blank' style='color:blue;'>kemlu.go.id</a> and the relevant Indonesian Representative's site for the latest information."
    },

    # --- Legalization Services ---
    "document legalization": {
        "type": "list",
        "title": "Information regarding document legalization:",
        "items": [
            "The complete procedure can be accessed at <a href='https://legalisasi.kemlu.go.id' target='_blank' style='color:blue;'>legalisasi.kemlu.go.id</a>.",
            "Ensure your document has been legalized by the <strong>Ministry of Law and Human Rights</strong> before submitting it to the Ministry of Foreign Affairs.",
            "For countries that are members of the Apostille Convention, legalization is sufficient up to obtaining an <strong>Apostille</strong> certificate from the Ministry of Law and Human Rights."
        ]
    },
    
    # --- UPDATED AND NEW ENTRIES FROM .TXT FILE ---

    # --- Policy ---
    "asean policy": {
        "type": "paragraph",
        "content": "Information regarding Indonesia's policies and cooperation within the ASEAN framework, including priorities and initiatives. For more details, visit the <a href='https://kemlu.go.id/kebijakan/asean' target='_blank' style='color:blue;'>ASEAN Policy page</a>."
    },
    "economic diplomacy policy": {
        "type": "paragraph",
        "content": "Learn more about Indonesia's economic diplomacy strategies and policies aimed at enhancing trade, investment, and other economic collaborations globally. Full info is available at the <a href='https://kemlu.go.id/kebijakan/diplomasi-ekonomi' target='_blank' style='color:blue;'>Economic Diplomacy page</a>."
    },
    "special issues": {
        "type": "paragraph",
        "content": "Find information on Indonesia's position and policies on various special issues at the international level, such as climate change, maritime security, and more. Details can be accessed on the <a href='https://kemlu.go.id/kebijakan/isu-khusus' target='_blank' style='color:blue;'>Special Issues page</a>."
    },
    "bilateral cooperation": {
        "type": "paragraph",
        "content": "Information on bilateral relations and cooperation between Indonesia and other countries across various regions. Visit the <a href='https://kemlu.go.id/kebijakan/kerja-sama-bilateral' target='_blank' style='color:blue;'>Bilateral Cooperation page</a> for complete data."
    },
    "multilateral cooperation": {
        "type": "paragraph",
        "content": "Get information about Indonesia's participation and policies in multilateral forums like the UN and other international organizations. Learn more at the <a href='https://kemlu.go.id/kebijakan/kerja-sama-multilateral' target='_blank' style='color:blue;'>Multilateral Cooperation page</a>."
    },
    "regional cooperation": {
        "type": "paragraph",
        "content": "Learn about Indonesia's cooperation with various organizations and forums at a regional level beyond ASEAN. More information can be found on the <a href='https://kemlu.go.id/kebijakan/kerja-sama-regional' target='_blank' style='color:blue;'>Regional Cooperation page</a>."
    },
    "vision and mission of foreign policy": {
        "type": "paragraph",
        "content": "The principles, vision, and mission that form the foundation for the implementation of Indonesia's Foreign Policy. Official documents and explanations can be accessed on the <a href='https://kemlu.go.id/kebijakan/landasan-visi-dan-misi-polugri' target='_blank' style='color:blue;'>Vision and Mission of Foreign Policy page</a>."
    },
    "international organizations": {
        "type": "paragraph",
        "content": "Information on Indonesia's membership and active role in various International Organizations. Visit the <a href='https://kemlu.go.id/kebijakan/organisasi-internasional' target='_blank' style='color:blue;'>International Organizations page</a> for a full list."
    },
    "gender mainstreaming": {
        "type": "paragraph",
        "content": "Learn about the commitment and implementation of gender mainstreaming policies in Indonesia's diplomacy and foreign relations. More info at the <a href='https://kemlu.go.id/kebijakan/pengarusutamaan-gender' target='_blank' style='color:blue;'>Gender Mainstreaming page</a>."
    },
    "bureaucratic reform": {
        "type": "paragraph",
        "content": "Information related to the programs and achievements of Bureaucratic Reform within the Ministry of Foreign Affairs to realize good governance. See the details on the <a href='https://kemlu.go.id/kebijakan/reformasi-birokrasi-kemlu' target='_blank' style='color:blue;'>MFA Bureaucratic Reform page</a>."
    },

    # --- Performance ---
    "mfa performance": {
        "type": "paragraph",
        "content": "Access performance reports, including the Government Agency Performance Accountability Report (AKIP) from various work units at the MFA. For full reports, visit the <a href='https://kemlu.go.id/kinerja' target='_blank' style='color:blue;'>Ministry of Foreign Affairs Performance page</a>."
    },

    # --- Publications ---
    "mfa publications": {
        "type": "paragraph",
        "content": "The Ministry of Foreign Affairs provides various publications such as agendas, books, diplomacy galleries, journals, studies, magazines, speeches, press releases, and tabloids. Access all these materials through the <a href='https://kemlu.go.id/publikasi' target='_blank' style='color:blue;'>MFA Publications Portal</a>."
    },
    "press releases": {
        "type": "paragraph",
        "content": "Get official and up-to-date information from the Ministry of Foreign Affairs through press releases published regularly. Visit the <a href='https://kemlu.go.id/publikasi/siaran-pers' target='_blank' style='color:blue;'>Press Releases page</a>."
    },

    # --- PPID ---
    "ppid": {
        "type": "paragraph",
        "content": "The Information and Documentation Management Officer (PPID) of the MFA provides public information services as mandated by the Public Information Openness Law. To submit an information request, visit the <a href='https://kemlu.go.id/ppid' target='_blank' style='color:blue;'>MFA PPID page</a>."
    },

    # --- News ---
    "mfa news": {
        "type": "paragraph",
        "content": "Follow the latest developments on diplomacy, foreign policy, and activities of the Ministry of Foreign Affairs through the official news portal. Access the latest news on the <a href='https://kemlu.go.id/berita' target='_blank' style='color:blue;'>News page</a>."
    },

    # --- About Us ---
    "organizational structure": {
        "type": "paragraph",
        "content": "View the chart and explanation of the organizational structure of the Ministry of Foreign Affairs of the Republic of Indonesia. Detailed information is available on the <a href='https://kemlu.go.id/tentang-kami/struktur-organisasi' target='_blank' style='color:blue;'>Organizational Structure page</a>."
    },
    "list of joint statements": {
        "type": "paragraph",
        "content": "Access a collection of Joint Statements between Indonesia and other countries or international organizations. The full list can be viewed on the <a href='https://kemlu.go.id/daftar-joint-statement' target='_blank' style='color:blue;'>List of Joint Statements page</a>."
    },
    "information sheets": {
        "type": "paragraph",
        "content": "Find various information sheets (fact sheets) that provide concise data and information on a range of foreign relations issues. To access them, please visit the <a href='https://kemlu.go.id' target='_blank' style='color:blue;'>MFA Portal</a> and look for the 'Information Sheets' section in the menu."
    },
    
    # --- Services ---
    "legal documentation and information network": {
        "type": "paragraph",
        "content": "The Legal Documentation and Information Network (JDIH) is an integrated platform providing public access to various legal products and information issued by the Ministry of Foreign Affairs. Its goal is to ensure the availability of complete, accurate, and easily accessible legal documentation. For more information, visit the official site at <a href='https://jdih.kemlu.go.id/' target='_blank' style='color:blue;'>MFA JDIH Service</a>.",
        "bullets": [
            "Provides access to International Treaties, Ministerial Regulations, and other legal products.",
            "Facilitates easy search and browsing of laws and regulations.",
            "Supports transparency and the electronic dissemination of legal information.",
            "Serves as the central database for legal information within the Ministry of Foreign Affairs."
        ]
    },
    "card for indonesian diaspora": {
        "type": "paragraph",
        "content": "The Card for Indonesian Society Abroad (KMILN) is an electronic identity card for Indonesian citizens residing overseas. This card functions as a form of identification and personal data, offering various conveniences and benefits to its holders. For complete information, visit the official <a href='https://iocs.kemlu.go.id/' target='_blank' style='color:blue;'>KMILN Service</a> page.",
        "bullets": [
            "Serves as an official identity card for the Indonesian diaspora.",
            "Simplifies access to public services in Indonesia (e.g., opening bank accounts, managing properties).",
            "Provides access to special facilities or discounts from participating partners.",
            "Registration is conducted online through a dedicated portal."
        ]
    },
    "list of foreign diplomatic and consular missions": {
        "type": "paragraph",
        "content": "The Ministry of Foreign Affairs provides an official and up-to-date list of all foreign diplomatic missions (Embassies) and consular posts (Consulates) accredited in Indonesia. This information is crucial for government agencies, private entities, and the public. The complete list can be accessed via: <a href='https://kemlu.go.id/layanan/layanan-konsuler-fasilitas-diplomatik-dan-pelindungan-wni/daftar-perwakilan-diplomatik-dan-konsuler-asing' target='_blank' style='color:blue;'>List of Foreign Missions</a>.",
        "bullets": [
            "Presents address, phone number, and other essential contact information.",
            "Includes a comprehensive list of Embassies and Consulates General/Consulates.",
            "The information is regularly updated to ensure data accuracy.",
            "Useful for official correspondence and verification purposes."
        ]
    },
    "diplomatic facilities": {
        "type": "paragraph",
        "content": "The Diplomatic Facilities service is intended to provide convenience for the diplomatic corps and international organizations in Indonesia. This service covers various facilities that support their duties in accordance with the Vienna Convention and applicable regulations. More detailed information can be accessed via <a href='https://kemlu.go.id/layanan/layanan-konsuler-fasilitas-diplomatik-dan-pelindungan-wni/fasilitas-diplomatik' target='_blank' style='color:blue;'>MFA Diplomatic Facilities</a>.",
        "bullets": [
            "Issuance of diplomatic and consular identity cards.",
            "Granting of entry permits for diplomatic officials and their families.",
            "Provision of immunities and privileges in line with international law.",
            "Coordination regarding the duty-free import of personal goods and official vehicles."
        ]
    },
    "consular services": {
        "type": "paragraph",
        "content": "Consular Services encompass a wide range of public services provided by the Ministry of Foreign Affairs and Indonesian Missions abroad to both Indonesian Citizens and foreign nationals. These services aim to provide legal certainty and protection for citizens. More information can be found at <a href='https://kemlu.go.id/layanan/layanan-konsuler-fasilitas-diplomatik-dan-pelindungan-wni/kekonsuleran' target='_blank' style='color:blue;'>Consular Services</a>.",
        "bullets": [
            "Issuance of Passports and Emergency Travel Documents (SPLP).",
            "Legalization of documents for use both domestically and internationally.",
            "Visa services for foreign nationals intending to visit Indonesia.",
            "Registration of vital events such as births, marriages, and deaths."
        ]
    },
    "protection for indonesian citizens": {
        "type": "paragraph",
        "content": "The Ministry of Foreign Affairs is committed to providing maximum protection for all Indonesian citizens abroad. This service includes assistance in various situations, from lost documents and legal cases to emergencies. For assistance, visit <a href='https://kemlu.go.id/layanan/layanan-konsuler-fasilitas-diplomatik-dan-pelindungan-wni/pelindungan-wni' target='_blank' style='color:blue;'>Protection for Indonesian Citizens</a> or contact the emergency hotline.",
        "bullets": [
            "Legal aid and assistance for Indonesian citizens facing legal issues.",
            "Evacuation from countries experiencing conflict or natural disasters.",
            "Assistance for victims of human trafficking (TPPO) and violence.",
            "Online self-reporting service via the Peduli WNI Portal to facilitate protection."
        ]
    },
    "country signing certificate authority": {
        "type": "paragraph",
        "content": "The Country Signing Certificate Authority (CSCA) of Indonesia is responsible for issuing and managing the digital certificates used to secure data in the electronic passport (e-passport). This ensures the data cannot be forged and its authenticity can be verified. Technical information can be accessed at <a href='https://kemlu.go.id/layanan/layanan-konsuler-fasilitas-diplomatik-dan-pelindungan-wni/country-signing-certificate-authority-csca' target='_blank' style='color:blue;'>MFA CSCA</a>.",
        "bullets": [
            "Manages the public keys for verifying the authenticity of Indonesian e-passports.",
            "Ensures the integrity and security of the data within the electronic passport chip.",
            "Part of the international Public Key Infrastructure (PKI) framework.",
            "Provides certificates for other countries to download for verification purposes."
        ]
    },
    "foreign ngo registration": {
        "type": "paragraph",
        "content": "This service regulates the procedures and requirements for Foreign Non-Governmental Organizations (NGOs) wishing to operate legally in Indonesia. Verification is conducted to ensure the NGO's activities align with regulations and benefit the community. Procedures can be found at <a href='https://kemlu.go.id/layanan/pendaftaran-ormas-asing-indonesia' target='_blank' style='color:blue;'>Foreign NGO Registration</a>.",
        "bullets": [
            "Provides a complete guide on the necessary documentation.",
            "Operational permits are granted for a specific period and are renewable.",
            "Ensures the accountability and transparency of Foreign NGO activities in Indonesia.",
            "The verification process includes assessing the alignment of work programs with national priorities."
        ]
    },
    "public complaints": {
        "type": "paragraph",
        "content": "The Ministry of Foreign Affairs provides an official channel for the public to submit complaints, feedback, or aspirations regarding the ministry's performance and services. Each report is handled professionally and transparently to improve public service quality. Submit your complaint via <a href='https://kemlu.go.id/layanan/pengaduan-masyarakat' target='_blank' style='color:blue;'>Public Complaints</a>.",
        "bullets": [
            "A means to report alleged violations or dissatisfaction with services.",
            "The identity of the complainant is kept confidential.",
            "A structured and trackable complaint management mechanism.",
            "Supports bureaucratic reform and the enhancement of public service quality."
        ]
    },
    "media services": {
        "type": "paragraph",
        "content": "Media Services are designed to facilitate reporting activities by domestic and international journalists on Indonesia's foreign policy. This service includes accreditation, press releases, and arranging interviews. For media purposes, information can be accessed via <a href='https://kemlu.go.id/layanan/pelayanan-media' target='_blank' style='color:blue;'>MFA Media Services</a>.",
        "bullets": [
            "Accreditation for foreign journalists who will be reporting in Indonesia.",
            "Distribution of press releases, transcripts, and other official information materials.",
            "Organization of regular press briefings and press conferences.",
            "Assistance in arranging interview sessions with ministry officials."
        ]
    },
    "online rogatory": {
        "type": "paragraph",
        "content": "The Online Rogatory system facilitates the process of requesting mutual legal assistance in criminal matters between Indonesia and other countries electronically. Further information is available on the <a href='https://kemlu.go.id/layanan/rogatory-online' target='_blank' style='color:blue;'>Online Rogatory page</a>."
    },
    "treaty database": {
        "type": "paragraph",
        "content": "The Treaty Database provides access to the collection of international treaties to which the Government of Indonesia is a party. Access the database via the <a href='https://kemlu.go.id/layanan/treaty-database' target='_blank' style='color:blue;'>MFA Treaty Database</a>."
    },
    "procurement unit": {
        "type": "paragraph",
        "content": "The Goods/Services Procurement Unit (UKPBJ) of the Ministry of Foreign Affairs is responsible for carrying out the procurement process transparently and accountably. Tender and procurement information can be accessed on the <a href='https://kemlu.go.id/layanan/unit-kerja-pengadaan-barangjasa-ukpbj' target='_blank' style='color:blue;'>UKPBJ page</a>."
    },
    "indonesian missions": {
        "type": "paragraph",
        "content": "Find a complete list of all Indonesian Missions abroad, including Embassies, Consulates General, and Permanent Missions. Visit the <a href='https://kemlu.go.id/perwakilan' target='_blank' style='color:blue;'>Indonesian Missions portal</a> for the full directory."
    },

    # --- Greetings & General Responses ---
    "thank you": {"type": "paragraph", "content": "You're welcome! Happy to help. If you have any other questions, don't hesitate to ask again. 😊"},
    "hello": {"type": "paragraph", "content": "Hello! Welcome to the Virtual Assistant Service of the Indonesian Ministry of Foreign Affairs. I'm ready to help with your questions about <strong>passports, visas, addresses of Indonesian representatives, document legalization</strong>, and other consular services."},
    "hi": {"type": "paragraph", "content": "Hello! Welcome to the Virtual Assistant Service of the Indonesian Ministry of Foreign Affairs. Please ask your questions about the official services of the MFA."},
    "greetings": {"type": "paragraph", "content": "Hello! I am the official Virtual Assistant of the Indonesian Ministry of Foreign Affairs. I am ready to help answer your questions about consular services."},

    # --- Addresses of Indonesian Representatives (Embassy/Consulate/Permanent Mission) ---
    "afghanistan": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Afghanistan:<br><br><strong>Embassy of the Republic of Indonesia in Kabul, Afghanistan</strong><br>Address: Malalai Watt, Shah-re-Naw, Ministry of Interior Street, Kabul, Afghanistan<br>Phone: (+93-20) 220-1066<br>Website: <a href='https://kemlu.go.id/afghanistan' target='_blank' style='color:blue;'>kemlu.go.id/afghanistan</a><br><a href='" + PETA_LOKASI["afghanistan"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "south africa": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in South Africa:<br><br><strong>Embassy of the Republic of Indonesia in Pretoria, South Africa</strong><br>Address: 949 Schoeman Street, Arcadia, Pretoria, Republic of South Africa<br>Phone: (+27-12) 342-3350<br>Website: <a href='https://kemlu.go.id/southafrica' target='_blank' style='color:blue;'>kemlu.go.id/southafrica</a><br><a href='" + PETA_LOKASI["south africa"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "united states": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in the United States:<br><br><strong>Embassy of the Republic of Indonesia in Washington, D.C., USA</strong><br>Address: 2020 Massachusetts Avenue N.W., Washington, D.C. 20036, USA<br>Phone: (+1-202) 775-5200<br>Website: <a href='https://kemlu.go.id/washington' target='_blank' style='color:blue;'>kemlu.go.id/washington</a><br><a href='" + PETA_LOKASI["united states"] + "' target='_blank' style='color:blue;'>View Map</a><br><br>There are also Consulates General in <strong>New York, Los Angeles, Chicago, Houston,</strong> and <strong>San Francisco</strong>."},
    "australia": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Australia:<br><br><strong>Embassy of the Republic of Indonesia in Canberra, Australia</strong><br>Address: 8 Darwin Avenue, Yarralumla ACT 2600, Canberra, Australia<br>Phone: (+61-2) 6250-8600<br>Website: <a href='https://kbri-canberra.go.id' target='_blank' style='color:blue;'>kbri-canberra.go.id</a><br><a href='" + PETA_LOKASI["australia"] + "' target='_blank' style='color:blue;'>View Map</a><br><br>There are also Consulates General in <strong>Sydney, Melbourne,</strong> and <strong>Perth</strong>."},
    "netherlands": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in the Netherlands:<br><br><strong>Embassy of the Republic of Indonesia in The Hague, Netherlands</strong><br>Address: Tobias Asserlaan 8, 2517 KC Den Haag (The Hague), Netherlands<br>Phone: (+31-70) 310-8100, 310-8176, 310-8177<br>Website: <a href='https://kemlu.go.id/netherlands' target='_blank' style='color:blue;'>kemlu.go.id/netherlands</a><br><a href='" + PETA_LOKASI["netherlands"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "china": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in China:<br><br><strong>Embassy of the Republic of Indonesia in Beijing, China</strong><br>Address: Dong Zhi Men Wai Da Jie No.4, Chaoyang District, Beijing 100600, China<br>Phone: (+86-10) 6532-5486, 6532-5488<br>Website: <a href='https://kemlu.go.id/beijing' target='_blank' style='color:blue;'>kemlu.go.id/beijing</a><br><a href='" + PETA_LOKASI["china"] + "' target='_blank' style='color:blue;'>View Map</a><br><br>There are also Consulates General in <strong>Shanghai, Guangzhou,</strong> and <strong>Hong Kong</strong>."},
    "united kingdom": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in the United Kingdom:<br><br><strong>Embassy of the Republic of Indonesia in London, UK</strong><br>Address: 38 Grosvenor Square, London W1K 2HW, UK<br>Phone: (+44-20) 7499-7661, 7290-9600<br>Website: <a href='https://indonesianembassy.org.uk' target='_blank' style='color:blue;'>indonesianembassy.org.uk</a><br><a href='" + PETA_LOKASI["united kingdom"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "japan": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Japan:<br><br><strong>Embassy of the Republic of Indonesia in Tokyo, Japan</strong><br>Address: 2-9 Higashi Gotanda 5-chome, Shinagawa-ku, Tokyo 141-0022, Japan<br>Phone: (+81-3) 3441-4201<br>Website: <a href='https://kemlu.go.id/tokyo' target='_blank' style='color:blue;'>kemlu.go.id/tokyo</a><br><a href='" + PETA_LOKASI["japan"] + "' target='_blank' style='color:blue;'>View Map</a><br><br>There is also a Consulate General in <strong>Osaka</strong>."},
    "germany": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Germany:<br><br><strong>Embassy of the Republic of Indonesia in Berlin, Germany</strong><br>Address: Lehrter Straße 16-17, 10557 Berlin, Germany<br>Phone: (+49-30) 478-070<br>Website: <a href='https://indonesianembassy.de' target='_blank' style='color:blue;'>indonesianembassy.de</a><br><a href='" + PETA_LOKASI["germany"] + "' target='_blank' style='color:blue;'>View Map</a><br><br>There are also Consulates General in <strong>Frankfurt</strong> and <strong>Hamburg</strong>."},
    "malaysia": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Malaysia:<br><br><strong>Embassy of the Republic of Indonesia in Kuala Lumpur, Malaysia</strong><br>Address: 233 Jalan Tun Razak, 50400 Kuala Lumpur, Malaysia<br>Phone: (+60-3) 2116-4000, 2116-4016<br>Website: <a href='https://kemlu.go.id/kualalumpur' target='_blank' style='color:blue;'>kemlu.go.id/kualalumpur</a><br><a href='" + PETA_LOKASI["malaysia"] + "' target='_blank' style='color:blue;'>View Map</a><br><br>There are also Consulates General in <strong>Johor Bahru, Kota Kinabalu, Kuching,</strong> and <strong>Penang</strong>."},
    "singapore": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Singapore:<br><br><strong>Embassy of the Republic of Indonesia in Singapore</strong><br>Address: 7 Chatsworth Road, Singapore 249761<br>Phone: (+65) 6737-7422<br>Website: <a href='https://kemlu.go.id/singapore' target='_blank' style='color:blue;'>kemlu.go.id/singapore</a><br><a href='" + PETA_LOKASI["singapore"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "algeria": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Algeria:<br><br><strong>Indonesian Representative in Algiers, Algeria</strong><br>Address: 17 Rue Chemin Abdelkadir Gadouch, Hydra, El Biar, Algiers, Algeria<br>Phone: (+213-21) 694-915, 694-921<br>Website: <a href='https://kemlu.go.id/algiers' target='_blank' style='color:blue;'>kemlu.go.id/algiers</a><br><a href='" + PETA_LOKASI["algeria"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "saudi arabia": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Saudi Arabia:<br><br><strong>Embassy of the Republic of Indonesia in Riyadh, Saudi Arabia</strong><br>Address: Riyadh Diplomatic Quarter, PO Box 94343, Riyadh 11693, Kingdom of Saudi Arabia<br>Phone: (+966-1) 488-2800; Fax: (+966-1) 488-2966<br>Website: <a href='https://kemlu.go.id/riyadh' target='_blank' style='color:blue;'>kemlu.go.id/riyadh</a><br><a href='" + PETA_LOKASI["saudi arabia"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "argentina": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Argentina:<br><br><strong>Embassy of the Republic of Indonesia in Buenos Aires, Argentina</strong><br>Address: Mariscal Ramón Castilla 2901, Capital Federal, Buenos Aires 1425, Argentina<br>Phone: (+54-11) 4807-2211, 4807-2956, 4807-3324<br>Website: <a href='https://kemlu.go.id/buenosaires' target='_blank' style='color:blue;'>kemlu.go.id/buenosaires</a><br><a href='" + PETA_LOKASI["argentina"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "austria": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Austria:<br><br><strong>Embassy of the Republic of Indonesia in Vienna, Austria</strong><br>Address: Gustav Tschermakgasse 5-7, A-1180 Wien (Vienna), Austria<br>Phone: (+43-1) 47-623<br>Website: <a href='https://kemlu.go.id/vienna' target='_blank' style='color:blue;'>kemlu.go.id/vienna</a><br><a href='" + PETA_LOKASI["austria"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "azerbaijan": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Azerbaijan:<br><br><strong>Embassy of the Republic of Indonesia in Baku, Azerbaijan</strong><br>Address: Azer Aliyev 3, Nasimi District, Baku City 1022, Azerbaijan<br>Phone: (+994-12) 597-0514 / 596-2168<br>Website: <a href='https://kemlu.go.id/baku' target='_blank' style='color:blue;'>kemlu.go.id/baku</a><br><a href='" + PETA_LOKASI["azerbaijan"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "bahrain": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Bahrain:<br><br><strong>Embassy of the Republic of Indonesia in Kuwait (covers Bahrain)</strong><br>Address: Kaifan Block 6, Al Andalus Street No. 29, 13076 Safat, Kuwait City, Kuwait (covers Bahrain)<br>Phone: (+965) 483-9927, 483-9953<br>Website: <a href='https://kemlu.go.id/kuwaitcity' target='_blank' style='color:blue;'>kemlu.go.id/kuwaitcity</a><br><a href='" + PETA_LOKASI["kuwait"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "bangladesh": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Bangladesh:<br><br><strong>Embassy of the Republic of Indonesia in Dhaka, Bangladesh</strong><br>Address: Road No.53, Plot No.14, Gulshan-2, Dhaka 1212, Bangladesh<br>Phone: (+880-2) 988-1640, 988-1641, 881-2260<br>Website: <a href='https://kemlu.go.id/dhaka' target='_blank' style='color:blue;'>kemlu.go.id/dhaka</a><br><a href='" + PETA_LOKASI["bangladesh"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "belgium": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Belgium:<br><br><strong>Embassy of the Republic of Indonesia in Brussels, Belgium</strong><br>Address: Avenue de Tervueren 294, 1150 Brussels, Belgium<br>Phone: (+32-2) 771-2014, 771-1778, 771-2666, 771-3347<br>Website: <a href='https://kemlu.go.id/brussels' target='_blank' style='color:blue;'>kemlu.go.id/brussels</a><br><a href='" + PETA_LOKASI["belgium"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "bosnia and herzegovina": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Bosnia and Herzegovina:<br><br><strong>Indonesian Representative (Embassy in Budapest covers Bosnia & Herzegovina)</strong><br>Address: Varosligeti fasor 26, 1068 Budapest, Hungary (diplomatic)<br>Phone: (+36-1) 413-3800<br>Website: <a href='https://kemlu.go.id/budapest' target='_blank' style='color:blue;'>kemlu.go.id/budapest</a><br><a href='" + PETA_LOKASI["bosnia and herzegovina"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "brazil": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Brazil:<br><br><strong>Embassy of the Republic of Indonesia in Brasilia, Brazil</strong><br>Address: SES Avenida Das Nações Quadra 805, Lote 20, CEP 70479-900, Brasília-DF, Brazil<br>Phone: (+55-61) 3443-8800, 3443-1788<br>Website: <a href='https://kemlu.go.id/brasilia' target='_blank' style='color:blue;'>kemlu.go.id/brasilia</a><br><a href='" + PETA_LOKASI["brazil"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "brunei darussalam": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Brunei Darussalam:<br><br><strong>Embassy of the Republic of Indonesia in Bandar Seri Begawan, Brunei</strong><br>Address: Kampung Sungai Hanching Baru, Simpang 528, Lot 4498, Jalan Muara, Bandar Seri Begawan BS 1930, Brunei<br>Phone: (+673) 233-0180, 233-0358<br>Website: <a href='https://kemlu.go.id/brunei' target='_blank' style='color:blue;'>kemlu.go.id/brunei</a><br><a href='" + PETA_LOKASI["brunei darussalam"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "bulgaria": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Bulgaria:<br><br><strong>Indonesian Representative in Bulgaria</strong><br>Address: 5 Yozef Valdhard Str. (53 Simenovsko Shosse, No.4), 1700 Sofia, Bulgaria<br>Phone: (+359-2) 962-5240, 962-6170, 683-220<br>Website: <a href='https://kemlu.go.id/sofia' target='_blank' style='color:blue;'>kemlu.go.id/sofia</a><br><a href='" + PETA_LOKASI["bulgaria"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "czech republic": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in the Czech Republic:<br><br><strong>Embassy of the Republic of Indonesia in Prague, Czech Republic</strong><br>Address: Nad Budankami II/7, 150 21 Prague 5, Czech Republic<br>Phone: (+420-2) 5721-4388 to 4390<br>Website: <a href='https://kemlu.go.id/prague' target='_blank' style='color:blue;'>kemlu.go.id/prague</a><br><a href='" + PETA_LOKASI["czech republic"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "chile": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Chile:<br><br><strong>Indonesian Representative in Chile</strong><br>Address: Av. Nueva Costanera 3318, Vitacura, Santiago, Chile (PO Box 20-D)<br>Phone: (+56-2) 207-6266, 207-9880, 207-4372<br>Website: <a href='https://kemlu.go.id/santiago' target='_blank' style='color:blue;'>kemlu.go.id/santiago</a><br><a href='" + PETA_LOKASI["chile"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "denmark": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Denmark:<br><br><strong>Indonesian Representative in Denmark</strong><br>Address: Ørehøj Allé 1, 2900 Hellerup, Copenhagen, Denmark<br>Phone: (+45) 3962-4422<br>Website: <a href='https://kemlu.go.id/copenhagen' target='_blank' style='color:blue;'>kemlu.go.id/copenhagen</a><br><a href='" + PETA_LOKASI["denmark"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "ecuador": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Ecuador:<br><br><strong>Indonesian Representative in Lima (covers Ecuador)</strong><br>Address: Av. Las Flores 334-336, San Isidro, Lima 27, Peru<br>Phone: (+51-1) 222-0308, 222-0309<br>Website: <a href='https://kemlu.go.id/lima' target='_blank' style='color:blue;'>kemlu.go.id/lima</a><br><a href='" + PETA_LOKASI["peru"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "egypt": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Egypt:<br><br><strong>Embassy of the Republic of Indonesia in Cairo, Egypt</strong><br>Address: 13 Aisha El Taimouria Street, Garden City, Cairo 11512, Egypt (PO Box 1661)<br>Phone: (+20-2)794-7200, 794-7209, 792-5451<br>Website: <a href='https://kemlu.go.id/egypt' target='_blank' style='color:blue;'>kemlu.go.id/egypt</a><br><a href='" + PETA_LOKASI["egypt"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "ethiopia": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Ethiopia:<br><br><strong>Embassy of the Republic of Indonesia in Addis Ababa, Ethiopia</strong><br>Address: Mekanissa Road Higher 23, Kebele 13, House No. 1816, PO Box 1004, Addis Ababa, Ethiopia<br>Phone: (+251-1) 712-104, 712-185<br>Website: <a href='https://kemlu.go.id/addisababa' target='_blank' style='color:blue;'>kemlu.go.id/addisababa</a><br><a href='" + PETA_LOKASI["ethiopia"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "fiji": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Fiji:<br><br><strong>Indonesian Representative in Suva, Fiji</strong><br>Address: 6th Floor Ra Marama Building, 91 Gordon Street, Suva, Fiji (PO Box 878 Suva)<br>Phone: (+679) 331-6697<br>Website: <a href='https://kemlu.go.id/suva' target='_blank' style='color:blue;'>kemlu.go.id/suva</a><br><a href='" + PETA_LOKASI["fiji"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "philippines": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in the Philippines:<br><br><strong>Embassy of the Republic of Indonesia in Manila, Philippines</strong><br>Address: 185 Salcedo Street, Legaspi Village, Makati City 1229, Metro Manila, Philippines (PO Box 1671 MCPO)<br>Phone: (+63-2) 892-5061 to 68<br>Website: <a href='https://kemlu.go.id/philippines' target='_blank' style='color:blue;'>kemlu.go.id/philippines</a><br><a href='" + PETA_LOKASI["philippines"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "finland": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Finland:<br><br><strong>Indonesian Representative in Finland</strong><br>Address: Kuusisaarentie 3, 00340 Helsinki, Finland<br>Phone: (+358-9) 477-0370<br>Website: <a href='https://kemlu.go.id/helsinki' target='_blank' style='color:blue;'>kemlu.go.id/helsinki</a><br><a href='" + PETA_LOKASI["finland"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "hungary": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Hungary:<br><br><strong>Indonesian Representative in Hungary</strong><br>Address: Varosligeti fasor 26, 1068 Budapest, Hungary<br>Phone: (+36-1) 413-3800<br>Website: <a href='https://kemlu.go.id/budapest' target='_blank' style='color:blue;'>kemlu.go.id/budapest</a><br><a href='" + PETA_LOKASI["hungary"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "india": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in India:<br><br><strong>Embassy of the Republic of Indonesia in New Delhi, India</strong><br>Address: 50-A Kautilya Marg, Chanakyapuri, New Delhi 110021, India<br>Phone: (+91-11) 2611-8642 to 46<br>Website: <a href='https://kemlu.go.id/india' target='_blank' style='color:blue;'>kemlu.go.id/india</a><br><a href='" + PETA_LOKASI["india"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "iraq": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Iraq:<br><br><strong>Embassy of the Republic of Indonesia in Baghdad, Iraq</strong><br>Address: Salhiya, Hay Al-'Ilam 220, Zukak 5, House 8, PO Box 420, Baghdad, Iraq<br>Phone: +964 776 984 2020<br>Website: (check official MFA site)<br><a href='" + PETA_LOKASI["iraq"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "iran": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Iran:<br><br><strong>Embassy of the Republic of Indonesia in Tehran, Iran</strong><br>Address: 210 Ghaemmagham Farahani Ave., Tehran 11365/4564, Iran<br>Phone: (+98-21) 8871-6865, 8871-7251, 8855-3655<br>Website: <a href='https://kemlu.go.id/tehran' target='_blank' style='color:blue;'>kemlu.go.id/tehran</a><br><a href='" + PETA_LOKASI["iran"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "italy": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Italy:<br><br><strong>Embassy of the Republic of Indonesia in Rome, Italy</strong><br>Address: Via Campania 53-55, 00187 Rome, Italy<br>Phone: (+39-06) 420-0911<br>Website: <a href='https://kemlu.go.id/italy' target='_blank' style='color:blue;'>kemlu.go.id/italy</a><br><a href='" + PETA_LOKASI["italy"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "jordan": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Jordan:<br><br><strong>Indonesian Representative in Jordan</strong><br>Address: 6th Circle, South Um-Uthaina, 44 Feisal bin Abdul Aziz Street, Amman 11181, Jordan<br>Phone: (+962-6) 552-8912<br>Website: <a href='https://kemlu.go.id/amman' target='_blank' style='color:blue;'>kemlu.go.id/amman</a><br><a href='" + PETA_LOKASI["jordan"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "cambodia": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Cambodia:<br><br><strong>Embassy of the Republic of Indonesia in Phnom Penh, Cambodia</strong><br>Address: No.1, Street 466 corner Norodom Blvd & 90, Sangkat Tonle Bassac, Khan Chamkarmon, Phnom Penh, Cambodia (PO Box 894)<br>Phone: (+855-23) 217-934, 216-148<br>Website: <a href='https://kemlu.go.id/cambodia' target='_blank' style='color:blue;'>kemlu.go.id/cambodia</a><br><a href='" + PETA_LOKASI["cambodia"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "canada": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Canada:<br><br><strong>Embassy of the Republic of Indonesia in Ottawa, Canada</strong><br>Address: 55 Park Dale Avenue, Ottawa, Ontario K1Y 5E5, Canada<br>Phone: (+1-613) 724-1100<br>Website: <a href='https://kemlu.go.id/ottawa' target='_blank' style='color:blue;'>kemlu.go.id/ottawa</a><br><a href='" + PETA_LOKASI["canada"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "kenya": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Kenya:<br><br><strong>Indonesian Representative in Kenya</strong><br>Address: Menengai Road, Upper Hill, Nairobi, Kenya (PO Box 48868-00100)<br>Phone: (+254-20) 271-4196–98<br>Website: <a href='https://kemlu.go.id/nairobi' target='_blank' style='color:blue;'>kemlu.go.id/nairobi</a><br><a href='" + PETA_LOKASI["kenya"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "south korea": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in South Korea:<br><br><strong>Embassy of the Republic of Indonesia in Seoul, South Korea</strong><br>Address: 55 Youido-dong, Yeongdeungpo-gu, Seoul, South Korea<br>Phone: (+82-2) 783-5675–77, 783-5371–72<br>Website: <a href='https://kemlu.go.id/republicofkorea' target='_blank' style='color:blue;'>kemlu.go.id/republicofkorea</a><br><a href='" + PETA_LOKASI["south korea"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "north korea": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in North Korea:<br><br><strong>Embassy of the Republic of Indonesia in Pyongyang, North Korea</strong><br>Address: 5, Munsudong, Taedonggang District, Pyongyang, DPRK (PO Box 178)<br>Phone: (+850-2) 381-7425<br>Website: <a href='https://kemlu.go.id/pyongyang' target='_blank' style='color:blue;'>kemlu.go.id/pyongyang</a><br><a href='" + PETA_LOKASI["north korea"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "croatia": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Croatia:<br><br><strong>Indonesian Representative (Embassy in Budapest covers Croatia)</strong><br>Address: Varosligeti fasor 26, 1068 Budapest, Hungary<br>Phone: (+36-1) 413-3800<br>Website: <a href='https://kemlu.go.id/budapest' target='_blank' style='color:blue;'>kemlu.go.id/budapest</a><br><a href='" + PETA_LOKASI["croatia"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "cuba": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Cuba:<br><br><strong>Embassy of the Republic of Indonesia in Havana, Cuba</strong><br>Address: 5ta Avenida No.1607, Miramar, La Habana, Cuba<br>Phone: (+53-7) 204-9963, 204-9618, 204-0046<br>Website: <a href='https://kemlu.go.id/havana' target='_blank' style='color:blue;'>kemlu.go.id/havana</a><br><a href='" + PETA_LOKASI["cuba"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "kuwait": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Kuwait:<br><br><strong>Embassy of the Republic of Indonesia in Kuwait City, Kuwait</strong><br>Address: Kaifan Block 6, Al Andalus Street No.29, 13076 Safat, Kuwait City, Kuwait<br>Phone: (+965) 483-9927, 483-9953<br>Website: <a href='https://kemlu.go.id/kuwaitcity' target='_blank' style='color:blue;'>kemlu.go.id/kuwaitcity</a><br><a href='" + PETA_LOKASI["kuwait"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "laos": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Laos:<br><br><strong>Embassy of the Republic of Indonesia in Vientiane, Laos</strong><br>Address: Phone Kheng Road, Vientiane, Lao PDR (PO Box 277)<br>Phone: (+856-21) 413-909, 413-910, 416-264<br>Website: <a href='https://kemlu.go.id/laos' target='_blank' style='color:blue;'>kemlu.go.id/laos</a><br><a href='" + PETA_LOKASI["laos"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "lebanon": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Lebanon:<br><br><strong>Embassy of the Republic of Indonesia in Beirut, Lebanon</strong><br>Address: Presidential Palace Avenue, Rue 68, Sector 3 No.3237, Baabda, Lebanon (PO Box 4007)<br>Phone: (+961-5) 924-682, 924-683, 924-676<br>Website: <a href='https://kemlu.go.id/beirut' target='_blank' style='color:blue;'>kemlu.go.id/beirut</a><br><a href='" + PETA_LOKASI["lebanon"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "libya": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Libya:<br><br><strong>Indonesian Representative in Libya</strong><br>Address: Hay Al Karamah, Qobri Taariq Al Sari', Amaama Al Saraaj, Tripoli, Libya (PO Box 5921)<br>Phone: (+218-21) 484-2067, 484-2843<br>Website: <a href='https://kemlu.go.id/tripoli' target='_blank' style='color:blue;'>kemlu.go.id/tripoli</a><br><a href='" + PETA_LOKASI["libya"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "morocco": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Morocco:<br><br><strong>Embassy of the Republic of Indonesia in Rabat, Morocco</strong><br>Address: 63 Rue Beni Boufrah Souissi, Rabat, Morocco (PO Box 5076)<br>Phone: (+212-537) 757-860, 757-861<br>Website: <a href='https://kemlu.go.id/rabat' target='_blank' style='color:blue;'>kemlu.go.id/rabat</a><br><a href='" + PETA_LOKASI["morocco"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "mexico": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Mexico:<br><br><strong>Embassy of the Republic of Indonesia in Mexico City, Mexico</strong><br>Address: Julio Verne No.27, Colonia Polanco, Delegación Miguel Hidalgo, Mexico City 11560, Mexico<br>Phone: (+52-55) 5280-5748, 5280-6363, 5280-6863, 5280-3449<br>Website: <a href='https://kemlu.go.id/mexicocity' target='_blank' style='color:blue;'>kemlu.go.id/mexicocity</a><br><a href='" + PETA_LOKASI["mexico"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "myanmar": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Myanmar:<br><br><strong>Embassy of the Republic of Indonesia in Yangon, Myanmar</strong><br>Address: 100 Pyidaungsu Yeiktha Road, Dagon Township, Yangon, Myanmar<br>Phone: (+95-1) 254-465, 254-469<br>Website: <a href='https://kemlu.go.id/myanmar' target='_blank' style='color:blue;'>kemlu.go.id/myanmar</a><br><a href='" + PETA_LOKASI["myanmar"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "namibia": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Namibia:<br><br><strong>Embassy of the Republic of Indonesia in Windhoek, Namibia</strong><br>Address: 103 Nelson Mandela Avenue, Windhoek, Namibia (PO Box 20691)<br>Phone: (+264-61) 285-1000, 285-1219<br>Website: <a href='https://kemlu.go.id/windhoek' target='_blank' style='color:blue;'>kemlu.go.id/windhoek</a><br><a href='" + PETA_LOKASI["namibia"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "nigeria": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Nigeria:<br><br><strong>Embassy of the Republic of Indonesia in Abuja, Nigeria</strong><br>Address: 4 Salt Lake Street, Off Gana Street, Maitama, Abuja FCT, Nigeria<br>Phone: (+234-9) 413-8625, 461-3252<br>Website: <a href='https://kemlu.go.id/abuja' target='_blank' style='color:blue;'>kemlu.go.id/abuja</a><br><a href='" + PETA_LOKASI["nigeria"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "norway": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Norway:<br><br><strong>Embassy of the Republic of Indonesia in Oslo, Norway</strong><br>Address: Fritzners Gate 12, 0244 Oslo, Norway<br>Phone: (+47) 2212-5130<br>Website: <a href='https://kemlu.go.id/norway' target='_blank' style='color:blue;'>kemlu.go.id/norway</a><br><a href='" + PETA_LOKASI["norway"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "pakistan": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Pakistan:<br><br><strong>Embassy of the Republic of Indonesia in Islamabad, Pakistan</strong><br>Address: Diplomatic Enclave I, Street 5, Ramna G-5/4, Islamabad 44000, Pakistan (PO Box 1019)<br>Phone: (+92-51) 283-2017 to 20, 288-0067 to 68<br>Website: <a href='https://kemlu.go.id/islamabad' target='_blank' style='color:blue;'>kemlu.go.id/islamabad</a><br><a href='" + PETA_LOKASI["pakistan"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "papua new guinea": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Papua New Guinea:<br><br><strong>Embassy of the Republic of Indonesia in Port Moresby, Papua New Guinea</strong><br>Address: Sir John Guise Drive, Lot 1&2, Section 410, Kiroki Street, Gordons 5, NCD, Port Moresby, Papua New Guinea (PO Box 7165)<br>Phone: (+675) 325-3116, 325-3544<br>Website: <a href='https://kemlu.go.id/portmoresby' target='_blank' style='color:blue;'>kemlu.go.id/portmoresby</a><br><a href='" + PETA_LOKASI["papua new guinea"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "united arab emirates": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in the United Arab Emirates:<br><br><strong>Embassy of the Republic of Indonesia in Abu Dhabi, UAE</strong><br>Address: Zone 2, Sector 79, Villa No. 474, Sultan Bin Zayed Street (Str.32), Al Bateen, Abu Dhabi, UAE (PO Box 7256)<br>Phone: (+971-2) 445-4448<br>Website: <a href='https://kemlu.go.id/uae' target='_blank' style='color:blue;'>kemlu.go.id/uae</a><br><a href='" + PETA_LOKASI["united arab emirates"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "peru": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Peru:<br><br><strong>Indonesian Representative in Lima, Peru</strong><br>Address: Avenida Las Flores 334-336, San Isidro, Lima 27, Peru<br>Phone: (+51-1) 222-0308, 222-0309<br>Website: <a href='https://kemlu.go.id/lima' target='_blank' style='color:blue;'>kemlu.go.id/lima</a><br><a href='" + PETA_LOKASI["peru"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "poland": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Poland:<br><br><strong>Embassy of the Republic of Indonesia in Warsaw, Poland</strong><br>Address: ul. Estońska 3/5, 03-903 Warsaw, Poland<br>Phone: (+48-22) 617-5179, 617-5108<br>Website: <a href='https://kemlu.go.id/warsawa' target='_blank' style='color:blue;'>kemlu.go.id/warsawa</a><br><a href='" + PETA_LOKASI["poland"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "portugal": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Portugal:<br><br><strong>Embassy of the Republic of Indonesia in Lisbon, Portugal</strong><br>Address: Rua Miguel Lupi 12, 1st Floor, 1249-080 Lisbon, Portugal<br>Phone: (+351-21) 393-2070<br>Website: <a href='https://kemlu.go.id/lisbon' target='_blank' style='color:blue;'>kemlu.go.id/lisbon</a><br><a href='" + PETA_LOKASI["portugal"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "france": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in France:<br><br><strong>Embassy of the Republic of Indonesia in Paris, France</strong><br>Address: 47-49 Rue Cortambert, 75116 Paris, France<br>Phone: (+33-1) 4503-0760<br>Website: <a href='https://kemlu.go.id/france' target='_blank' style='color:blue;'>kemlu.go.id/france</a><br><a href='" + PETA_LOKASI["france"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "qatar": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Qatar:<br><br><strong>Indonesian Representative in Qatar</strong><br>Address: Al-Maahed Street, Al Salata Al Jadeeda, Doha, Qatar (PO Box 22375)<br>Phone: (+974) 465-7945, 466-4981<br>Website: <a href='https://kemlu.go.id/doha' target='_blank' style='color:blue;'>kemlu.go.id/doha</a><br><a href='" + PETA_LOKASI["qatar"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "romania": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Romania:<br><br><strong>Embassy of the Republic of Indonesia in Bucharest, Romania</strong><br>Address: Strada Gina Patrichi No.10, Sector 1, Bucharest, Romania<br>Phone: (+40-21) 312-0742 to 44<br>Website: <a href='https://kemlu.go.id/bucharest' target='_blank' style='color:blue;'>kemlu.go.id/bucharest</a><br><a href='" + PETA_LOKASI["romania"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "russia": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Russia:<br><br><strong>Embassy of the Republic of Indonesia in Moscow, Russia</strong><br>Address: Novokuznetskaya Ulitsa No.12, Moscow, Russian Federation<br>Phone: (+7-495) 951-9549 to 51<br>Website: <a href='https://kemlu.go.id/russia' target='_blank' style='color:blue;'>kemlu.go.id/russia</a><br><a href='" + PETA_LOKASI["russia"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "new zealand": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in New Zealand:<br><br><strong>Embassy of the Republic of Indonesia in Wellington, New Zealand</strong><br>Address: 70 Glen Road, Kelburn, Wellington 6012, New Zealand (PO Box 3543)<br>Phone: (+64-4) 475-8697 to 99<br>Website: <a href='https://kemlu.go.id/wellington' target='_blank' style='color:blue;'>kemlu.go.id/wellington</a><br><a href='" + PETA_LOKASI["new zealand"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "senegal": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Senegal:<br><br><strong>Indonesian Representative in Senegal</strong><br>Address: Avenue Cheikh Anta Diop, BP. 5859, Dakar, Senegal<br>Phone: (+221) 825-7316, 824-0738<br>Website: <a href='https://kemlu.go.id/dakar' target='_blank' style='color:blue;'>kemlu.go.id/dakar</a><br><a href='" + PETA_LOKASI["senegal"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "serbia": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Serbia:<br><br><strong>Indonesian Representative (Embassy in Budapest covers Serbia)</strong><br>Website: <a href='https://kemlu.go.id' target='_blank' style='color:blue;'>kemlu.go.id</a><br><a href='" + PETA_LOKASI["serbia"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "slovakia": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Slovakia:<br><br><strong>Embassy of the Republic of Indonesia in Bratislava, Slovakia</strong><br>Address: Mudronova 51, 81103 Bratislava, Slovakia<br>Phone: (+421-2) 5441-9886, 5463-0165–66<br>Website: <a href='https://kemlu.go.id/bratislava' target='_blank' style='color:blue;'>kemlu.go.id/bratislava</a><br><a href='" + PETA_LOKASI["slovakia"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "spain": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Spain:<br><br><strong>Embassy of the Republic of Indonesia in Madrid, Spain</strong><br>Address: Calle de Agastia No.65, 28043 Madrid, Spain<br>Phone: (+34-91) 413-0294, 413-0394, 413-0594<br>Website: <a href='https://kemlu.go.id/madrid' target='_blank' style='color:blue;'>kemlu.go.id/madrid</a><br><a href='" + PETA_LOKASI["spain"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "sri lanka": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Sri Lanka:<br><br><strong>Embassy of the Republic of Indonesia in Colombo, Sri Lanka</strong><br>Address: 400/50 Sarana Road, Off Buddhaloka Mawatha, Colombo 7, Sri Lanka<br>Phone: (+94-11) 267-4337<br>Website: <a href='https://kemlu.go.id/colombo' target='_blank' style='color:blue;'>kemlu.go.id/colombo</a><br><a href='" + PETA_LOKASI["sri lanka"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "sudan": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Sudan:<br><br><strong>Indonesian Representative in Sudan</strong><br>Address: 17 Amarat 35, Juba Street Block 11, Khartoum, Sudan (PO Box 13374)<br>Phone: (+249) 1835-64036<br>Website: <a href='https://kemlu.go.id/khartoum' target='_blank' style='color:blue;'>kemlu.go.id/khartoum</a><br><a href='" + PETA_LOKASI["sudan"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "syria": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Syria:<br><br><strong>Embassy of the Republic of Indonesia in Damascus, Syria</strong><br>Address: Mazzeh Eastern Villas, Madina Al-Munawwara Street No.132, Block 270A, Bldg. 26, Damascus, Syria (PO Box 3530)<br>Phone: (+963-11) 611-9630, 611-9631<br>Website: <a href='https://kemlu.go.id/damascus' target='_blank' style='color:blue;'>kemlu.go.id/damascus</a><br><a href='" + PETA_LOKASI["syria"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "suriname": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Suriname:<br><br><strong>Embassy of the Republic of Indonesia in Paramaribo, Suriname</strong><br>Address: Van Brussellaan #3, Uitvlugt, Paramaribo, Suriname<br>Phone: (+597) 431-230, 413-171, 439-577<br>Website: <a href='https://kemlu.go.id/paramaribo' target='_blank' style='color:blue;'>kemlu.go.id/paramaribo</a><br><a href='" + PETA_LOKASI["suriname"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "sweden": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Sweden:<br><br><strong>Embassy of the Republic of Indonesia in Stockholm, Sweden</strong><br>Address: Sysslomansgatan 18/1, 112 41 Stockholm, Sweden (PO Box 12520)<br>Phone: (+46-8) 5455-5880<br>Website: <a href='https://kemlu.go.id/stockholm' target='_blank' style='color:blue;'>kemlu.go.id/stockholm</a><br><a href='" + PETA_LOKASI["sweden"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "switzerland": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Switzerland:<br><br><strong>Embassy of the Republic of Indonesia in Bern, Switzerland</strong><br>Address: Elfenauweg 51, 3006 Bern, Switzerland (PO Box 270, 3000 Bern)<br>Phone: (+41-31) 352-0983–85<br>Website: <a href='https://kemlu.go.id/bern' target='_blank' style='color:blue;'>kemlu.go.id/bern</a><br><a href='" + PETA_LOKASI["switzerland"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "tanzania": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Tanzania:<br><br><strong>Embassy of the Republic of Indonesia in Dar Es Salaam, Tanzania</strong><br>Address: 299 Ali Hassan Mwinyi Road, Dar Es Salaam, Tanzania (PO Box 572)<br>Phone: (+255-22) 211-9119, 211-8133<br>Website: <a href='https://kemlu.go.id/daressalaam' target='_blank' style='color:blue;'>kemlu.go.id/daressalaam</a><br><a href='" + PETA_LOKASI["tanzania"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "thailand": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Thailand:<br><br><strong>Embassy of the Republic of Indonesia in Bangkok, Thailand</strong><br>Address: 600-602 Petchburi Road, Ratchathewi, Bangkok 10400, Thailand<br>Phone: (+66-2) 252-3135 to 40<br>Website: <a href='https://kemlu.go.id/thailand' target='_blank' style='color:blue;'>kemlu.go.id/thailand</a><br><a href='" + PETA_LOKASI["thailand"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "timor leste": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Timor Leste:<br><br><strong>Embassy of the Republic of Indonesia in Dili, Timor Leste</strong><br>Address: Farol-Palapaso, Dili, Timor Leste (PO Box 207)<br>Phone: (+670) 331-7107, 331-1109<br>Website: <a href='https://kemlu.go.id/timorleste' target='_blank' style='color:blue;'>kemlu.go.id/timorleste</a><br><a href='" + PETA_LOKASI["timor leste"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "tunisia": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Tunisia:<br><br><strong>Indonesian Representative in Tunisia</strong><br>Address: 15 Rue du Lac Malaren/Rue du Lac Oubeira, BP 58 Berges du Lac, 1053 Tunis, Tunisia<br>Phone: (+216-71) 860-377, 860-702, 860-842<br>Website: <a href='https://kemlu.go.id/tunis' target='_blank' style='color:blue;'>kemlu.go.id/tunis</a><br><a href='" + PETA_LOKASI["tunisia"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "turkey": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Turkey:<br><br><strong>Embassy of the Republic of Indonesia in Ankara, Turkey</strong><br>Address: Abdullah Cevdet Sokak No.10, Çankaya 06680, Ankara, Turkey (PO Box 42)<br>Phone: (+90-312) 438-2190<br>Website: <a href='https://kemlu.go.id/turkey' target='_blank' style='color:blue;'>kemlu.go.id/turkey</a><br><a href='" + PETA_LOKASI["turkey"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "ukraine": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Ukraine:<br><br><strong>Embassy of the Republic of Indonesia in Kyiv, Ukraine</strong><br>Address: Ul. Otto Shmidta No.8, Kyiv 01054, Ukraine<br>Phone: (+380-44) 206-5490 to 94<br>Website: <a href='https://kemlu.go.id/kyiv' target='_blank' style='color:blue;'>kemlu.go.id/kyiv</a><br><a href='" + PETA_LOKASI["ukraine"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "uzbekistan": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Uzbekistan:<br><br><strong>Embassy of the Republic of Indonesia in Tashkent, Uzbekistan</strong><br>Address: 73 Yahyo Gulomov Street, Tashkent 700000, Uzbekistan<br>Phone: (+998-71) 132-0236 to 38<br>Website: <a href='https://kemlu.go.id/tashkent' target='_blank' style='color:blue;'>kemlu.go.id/tashkent</a><br><a href='" + PETA_LOKASI["uzbekistan"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "vatican": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in the Vatican:<br><br><strong>Indonesian Representative to the Holy See (Vatican)</strong><br>Address: Via Marocco No.10, 00144 Roma Eur, Italy<br>Phone: (+39-06) 5929-0049, 591-8610<br>Website: <a href='https://kemlu.go.id/vatican' target='_blank' style='color:blue;'>kemlu.go.id/vatican</a><br><a href='" + PETA_LOKASI["vatican"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "venezuela": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Venezuela:<br><br><strong>Embassy of the Republic of Indonesia in Caracas, Venezuela</strong><br>Address: Av. El Paseo con Calle Maracaibo, Quinta \"Indonesia\" Prados del Este, Caracas 1080, Venezuela<br>Phone: (+58-212) 975-2291, 976-2725<br>Website: <a href='https://kemlu.go.id/caracas' target='_blank' style='color:blue;'>kemlu.go.id/caracas</a><br><a href='" + PETA_LOKASI["venezuela"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "vietnam": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Vietnam:<br><br><strong>Embassy of the Republic of Indonesia in Hanoi, Vietnam</strong><br>Address: 50 Ngô Quyền Street, Hà Nội, Vietnam<br>Phone: (+84-4) 3825-3353, 3825-3324<br>Website: <a href='https://kemlu.go.id/vietnam' target='_blank' style='color:blue;'>kemlu.go.id/vietnam</a><br><a href='" + PETA_LOKASI["vietnam"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "yemen": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Yemen:<br><br><strong>Embassy of the Republic of Indonesia in Sana'a, Yemen</strong><br>Address: Beirut Street Faj Attan, Hadda, Sanaa 19873, Yemen (PO Box 19873)<br>Phone: (+967-1) 427-210, 427-211<br>Website: <a href='https://kemlu.go.id' target='_blank' style='color:blue;'>kemlu.go.id</a><br><a href='" + PETA_LOKASI["yemen"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "greece": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Greece:<br><br><strong>Embassy of the Republic of Indonesia in Athens, Greece</strong><br>Address: 99 Marathonodromon Street, Paleo Psychico 15452, Athens, Greece<br>Phone: (+30-210) 677-4692, 674-2345<br>Website: <a href='https://kemlu.go.id/athens' target='_blank' style='color:blue;'>kemlu.go.id/athens</a><br><a href='" + PETA_LOKASI["greece"] + "' target='_blank' style='color:blue;'>View Map</a>"},
    "zimbabwe": {"type": "paragraph", "content": "Of course, with pleasure! Here is the address and contact information for the Indonesian Representative in Zimbabwe:<br><br><strong>Embassy of the Republic of Indonesia in Harare, Zimbabwe</strong><br>Address: 3 Duthie Avenue, Belgravia, Harare, Republic of Zimbabwe (PO Box CY69 Causeway)<br>Phone: (+263-4) 251-799, 250-072<br>Website: <a href='https://kemlu.go.id/harare' target='_blank' style='color:blue;'>kemlu.go.id/harare</a><br><a href='" + PETA_LOKASI["zimbabwe"] + "' target='_blank' style='color:blue;'>View Map</a><br>Covers Malawi, Mozambique, Zambia."},
    "permanent mission asean": {"type": "paragraph", "content": "For details on the Permanent Mission of the Republic of Indonesia to ASEAN in Jakarta, please visit the official site: <a href='https://kemlu.go.id/asean' target='_blank' style='color:blue;'>kemlu.go.id/asean</a>"},
    "permanent mission geneva": {"type": "paragraph", "content": "For details on the Permanent Mission of the Republic of Indonesia to the UN in Geneva, please visit the official site: <a href='https://kemlu.go.id/geneva' target='_blank' style='color:blue;'>kemlu.go.id/geneva</a>"},
}

AUTOCOMPLETE_TERMS_EN = [
    # Core Services
    "Where is the Ministry of Foreign Affairs address?",
    "Location of the Ministry of Foreign Affairs.",
    "What is the official website of the Ministry of Foreign Affairs?",
    "How to legalize documents?",
    "What is document legalization?",
    "What is the emergency contact for Indonesian citizens?",
    "How to renew a passport?",
    "What is the Safe Travel application?",
    "What to do if my passport is lost?",
    "I lost my passport",
    "How to get protection for Indonesian citizens abroad?",
    "What are consular services?",

    # New & Specific Services
    "What is MFA's JDIH?",
    "How to get a Card for Indonesian Diaspora?",
    "List of foreign embassies in Indonesia",
    "How to get diplomatic facilities?",
    "Foreign NGO Registration",
    "How to file a public complaint?",
    "Services for the media",
    "Information on Online Rogatory",
    "What is the MFA Treaty Database?",
    "Info on procurement (UKPBJ)",
    "Where to find the list of Indonesian missions?",

    # Policy
    "What is MFA's policy on ASEAN?",
    "Information on economic diplomacy",
    "Indonesia's bilateral cooperation",
    "Indonesia's multilateral cooperation",
    "MFA organizational structure",
    
    # Information & News
    "Where can I find MFA news?",
    "MFA publications and journals",
    "Public information services (PPID)",
    "MFA performance reports",

    # Embassy Addresses (Sample)
    "Where is the Indonesian Embassy in the United States?",
    "Where is the Indonesian Embassy in Australia?",
    "Where is the Indonesian Embassy in the Netherlands?",
    "Where is the Indonesian Embassy in China?",
    "Where is the Indonesian Embassy in the United Kingdom?",
    "Where is the Indonesian Embassy in Japan?",
    "Where is the Indonesian Embassy in Germany?",
    "Where is the Indonesian Embassy in Malaysia?",
    "Where is the Indonesian Embassy in Singapore?",
    "Where is the Indonesian Embassy in Algeria?",
    "Where is the Indonesian Embassy in Saudi Arabia?",
    "Where is the Indonesian Embassy in Argentina?",
    "Where is the Indonesian Embassy in Austria?",
    "Where is the Indonesian Embassy in Azerbaijan?",
    "Where is the Indonesian Embassy in Bahrain?",
    "Where is the Indonesian Embassy in Bangladesh?",
    "Where is the Indonesian Embassy in Belgium?",
    "Where is the Indonesian Embassy in Bosnia and Herzegovina?",
    "Where is the Indonesian Embassy in Brazil?",
    "Where is the Indonesian Embassy in Brunei Darussalam?",
    "Where is the Indonesian Embassy in Bulgaria?",
    "Where is the Indonesian Embassy in the Czech Republic?",
    "Where is the Indonesian Embassy in Chile?",
    "Where is the Indonesian Embassy in Denmark?",
    "Where is the Indonesian Embassy in Ecuador?",
    "Where is the Indonesian Embassy in Egypt?",
    "Where is the Indonesian Embassy in Ethiopia?",
    "Where is the Indonesian Embassy in Fiji?",
    "Where is the Indonesian Embassy in the Philippines?",
    "Where is the Indonesian Embassy in Finland?",
    "Where is the Indonesian Embassy in Hungary?",
    "Where is the Indonesian Embassy in India?",
    "Where is the Indonesian Embassy in Iraq?",
    "Where is the Indonesian Embassy in Iran?",
    "Where is the Indonesian Embassy in Italy?",
    "Where is the Indonesian Embassy in Jordan?",
    "Where is the Indonesian Embassy in Cambodia?",
    "Where is the Indonesian Embassy in Canada?",
    "Where is the Indonesian Embassy in Kenya?",
    "Where is the Indonesian Embassy in South Korea?",
    "Where is the Indonesian Embassy in North Korea?",
    "Where is the Indonesian Embassy in Croatia?",
    "Where is the Indonesian Embassy in Cuba?",
    "Where is the Indonesian Embassy in Kuwait?",
    "Where is the Indonesian Embassy in Laos?",
    "Where is the Indonesian Embassy in Lebanon?",
    "Where is the Indonesian Embassy in Libya?",
    "Where is the Indonesian Embassy in Morocco?",
    "Where is the Indonesian Embassy in Mexico?",
    "Where is the Indonesian Embassy in Myanmar?",
    "Where is the Indonesian Embassy in Namibia?",
    "Where is the Indonesian Embassy in Nigeria?",
    "Where is the Indonesian Embassy in Norway?",
    "Where is the Indonesian Embassy in Pakistan?",
    "Where is the Indonesian Embassy in Papua New Guinea?",
    "Where is the Indonesian Embassy in the United Arab Emirates?",
    "Where is the Indonesian Embassy in Peru?",
    "Where is the Indonesian Embassy in Poland?",
    "Where is the Indonesian Embassy in Portugal?",
    "Where is the Indonesian Embassy in France?",
    "Where is the Indonesian Embassy in Qatar?",
    "Where is the Indonesian Embassy in Romania?",
    "Where is the Indonesian Embassy in Russia?",
    "Where is the Indonesian Embassy in New Zealand?",
    "Where is the Indonesian Embassy in Senegal?",
    "Where is the Indonesian Embassy in Serbia?",
    "Where is the Indonesian Embassy in Slovakia?",
    "Where is the Indonesian Embassy in Spain?",
    "Where is the Indonesian Embassy in Sri Lanka?",
    "Where is the Indonesian Embassy in Sudan?",
    "Where is the Indonesian Embassy in Syria?",
    "Where is the Indonesian Embassy in Suriname?",
    "Where is the Indonesian Embassy in Sweden?",
    "Where is the Indonesian Embassy in Switzerland?",
    "Where is the Indonesian Embassy in Tanzania?",
    "Where is the Indonesian Embassy in Thailand?",
    "Where is the Indonesian Embassy in Timor Leste?",
    "Where is the Indonesian Embassy in Tunisia?",
    "Where is the Indonesian Embassy in Turkey?",
    "Where is the Indonesian Embassy in Ukraine?",
    "Where is the Indonesian Embassy in Uzbekistan?",
    "Where is the Indonesian Embassy in the Vatican?",
    "Where is the Indonesian Embassy in Venezuela?",
    "Where is the Indonesian Embassy in Vietnam?",
    "Where is the Indonesian Embassy in Yemen?",
    "Where is the Indonesian Embassy in Greece?",
    "Where is the Indonesian Embassy in Zimbabwe?",
]

FOLLOW_UP_SUGGESTIONS_EN = {
    "lost passport": {
        "message": "I understand. To provide you with the correct contact information, in which country was your passport lost?",
        "suggestions": ["Lost passport in Malaysia", "Lost passport in Singapore", "Lost passport in the USA"]
    },
    "passport": {
        "message": "Certainly. Regarding passports, what specific information do you need?",
        "suggestions": [
            "What to do if my passport is lost?", 
            "Passport renewal requirements", 
            "How to apply for a new passport"
        ]
    },
    "visa": {
        "message": "Of course, I can help with visas. What would you like to know?",
        "suggestions": ["Do I need a visa to enter Indonesia?", "Visa requirements for foreigners", "How to apply for a visit visa"]
    },
    "address": {
        "message": "I can help find the address of an Indonesian Mission. Which country or city are you looking for?",
        "suggestions": ["Embassy address in Kuala Lumpur", "Embassy address in London", "Consulate General address in New York"]
    },
    "legalization": {
        "message": "Further information regarding document legalization:",
        "suggestions": ["What are the legalization requirements?", "How long is the legalization process?", "What is an Apostille?"]
    },
    "emergency": {
        "message": "If you are in an emergency, what would you like to do?",
        "suggestions": ["Online self-report", "Nearest Embassy address", "Contact emergency hotline"]
    },
    "services": {
        "message": "Certainly, regarding other MFA services, what would you like to know?",
        "suggestions": ["Legal Documentation Network", "Card for Indonesian Diaspora", "Public Complaints"]
    }
}

CITY_TO_COUNTRY = {
    # Afghanistan
    "kabul": "afghanistan", "kandahar": "afghanistan", "herat": "afghanistan", "mazar-i-sharif": "afghanistan", "jalalabad": "afghanistan", "kunduz": "afghanistan", "ghazni": "afghanistan",
    # South Africa
    "cape town": "south africa", "johannesburg": "south africa", "durban": "south africa", "pretoria": "south africa", "gqeberha": "south africa", "bloemfontein": "south africa",
    # United States
    "washington": "united states", "new york": "united states", "los angeles": "united states", "chicago": "united states", "houston": "united states", "phoenix": "united states", "philadelphia": "united states", "san antonio": "united states", "san diego": "united states", "dallas": "united states", "san jose": "united states", "austin": "united states", "jacksonville": "united states", "fort worth": "united states", "columbus": "united states", "indianapolis": "united states", "charlotte": "united states", "seattle": "united states", "denver": "united states", "boston": "united states", "el paso": "united states", "nashville": "united states", "detroit": "united states", "oklahoma city": "united states", "portland": "united states", "las vegas": "united states", "memphis": "united states", "louisville": "united states", "baltimore": "united states", "milwaukee": "united states", "albuquerque": "united states", "tucson": "united states", "fresno": "united states", "sacramento": "united states", "kansas city": "united states", "long beach": "united states", "mesa": "united states", "atlanta": "united states", "colorado springs": "united states", "virginia beach": "united states", "raleigh": "united states", "omaha": "united states", "miami": "united states", "oakland": "united states", "minneapolis": "united states", "tulsa": "united states", "wichita": "united states", "new orleans": "united states", "arlington": "united states",
    # Australia
    "canberra": "australia", "sydney": "australia", "melbourne": "australia", "brisbane": "australia", "perth": "australia", "adelaide": "australia", "gold coast": "australia", "newcastle": "australia", "wollongong": "australia", "geelong": "australia", "hobart": "australia", "townsville": "australia", "cairns": "australia", "darwin": "australia",
    # Netherlands
    "amsterdam": "netherlands", "rotterdam": "netherlands", "the hague": "netherlands", "utrecht": "netherlands", "eindhoven": "netherlands", "tilburg": "netherlands", "groningen": "netherlands", "almere": "netherlands", "breda": "netherlands", "nijmegen": "netherlands",
    # China
    "beijing": "china", "shanghai": "china", "chongqing": "china", "tianjin": "china", "guangzhou": "china", "shenzhen": "china", "chengdu": "china", "nanjing": "china", "wuhan": "china", "hangzhou": "china", "hong kong": "china", "macau": "china",
    # United Kingdom
    "london": "united kingdom", "birmingham": "united kingdom", "manchester": "united kingdom", "liverpool": "united kingdom", "leeds": "united kingdom", "sheffield": "united kingdom", "bristol": "united kingdom", "leicester": "united kingdom", "coventry": "united kingdom", "nottingham": "united kingdom",
    # Japan
    "tokyo": "japan", "yokohama": "japan", "osaka": "japan", "nagoya": "japan", "sapporo": "japan", "fukuoka": "japan", "kobe": "japan", "kyoto": "japan", "kawasaki": "japan", "saitama": "japan", "hiroshima": "japan", "sendai": "japan",
    # Germany
    "berlin": "germany", "hamburg": "germany", "munich": "germany", "cologne": "germany", "frankfurt": "germany", "stuttgart": "germany", "düsseldorf": "germany", "dortmund": "germany", "essen": "germany", "leipzig": "germany",
    # Malaysia
    "kuala lumpur": "malaysia", "george town": "malaysia", "ipoh": "malaysia", "shah alam": "malaysia", "petaling jaya": "malaysia", "johor bahru": "malaysia", "melaka": "malaysia", "kota kinabalu": "malaysia", "kuching": "malaysia", "penang": "malaysia",
    # Singapore
    "singapore": "singapore",
    # Algeria
    "algiers": "algeria", "oran": "algeria", "constantine": "algeria", "annaba": "algeria", "blida": "algeria", "batna": "algeria", "setif": "algeria",
    # Saudi Arabia
    "riyadh": "saudi arabia", "jeddah": "saudi arabia", "mecca": "saudi arabia", "medina": "saudi arabia", "dammam": "saudi arabia",
    # Argentina
    "buenos aires": "argentina", "cordoba": "argentina", "rosario": "argentina", "mendoza": "argentina", "la plata": "argentina",
    # Austria
    "vienna": "austria", "graz": "austria", "linz": "austria", "salzburg": "austria", "innsbruck": "austria",
    # Azerbaijan
    "baku": "azerbaijan", "sumqayit": "azerbaijan", "ganja": "azerbaijan",
    # Bangladesh
    "dhaka": "bangladesh", "chattogram": "bangladesh", "khulna": "bangladesh", "sylhet": "bangladesh", "rajshahi": "bangladesh",
    # Belgium
    "brussels": "belgium", "antwerp": "belgium", "ghent": "belgium", "charleroi": "belgium", "liège": "belgium", "bruges": "belgium",
    # Brazil
    "sao paulo": "brazil", "rio de janeiro": "brazil", "salvador": "brazil", "brasilia": "brazil", "fortaleza": "brazil", "belo horizonte": "brazil", "manaus": "brazil", "curitiba": "brazil",
    # Brunei Darussalam
    "bandar seri begawan": "brunei darussalam", "kuala belait": "brunei darussalam", "seria": "brunei darussalam",
    # Bulgaria
    "sofia": "bulgaria", "plovdiv": "bulgaria", "varna": "bulgaria", "burgas": "bulgaria",
    # Czech Republic
    "prague": "czech republic", "brno": "czech republic", "ostrava": "czech republic", "pilsen": "czech republic",
    # Chile
    "santiago": "chile", "valparaiso": "chile", "concepcion": "chile", "antofagasta": "chile",
    # Denmark
    "copenhagen": "denmark", "aarhus": "denmark", "odense": "denmark", "aalborg": "denmark",
    # Peru
    "lima": "peru", "arequipa": "peru", "trujillo": "peru", "chiclayo": "peru", "cusco": "peru",
    # Egypt
    "cairo": "egypt", "alexandria": "egypt", "giza": "egypt", "shubra el-kheima": "egypt",
    # Ethiopia
    "addis ababa": "ethiopia", "dire dawa": "ethiopia", "mekelle": "ethiopia", "gondar": "ethiopia",
    # Fiji
    "suva": "fiji", "nadi": "fiji", "lautoka": "fiji",
    # Philippines
    "manila": "philippines", "quezon city": "philippines", "davao city": "philippines", "cebu city": "philippines",
    # Finland
    "helsinki": "finland", "espoo": "finland", "tampere": "finland", "vantaa": "finland",
    # Hungary
    "budapest": "hungary", "debrecen": "hungary", "szeged": "hungary", "miskolc": "hungary",
    # India
    "delhi": "india", "mumbai": "india", "bangalore": "india", "kolkata": "india", "chennai": "india", "new delhi": "india",
    # Iraq
    "baghdad": "iraq", "mosul": "iraq", "basra": "iraq", "erbil": "iraq",
    # Iran
    "tehran": "iran", "mashhad": "iran", "isfahan": "iran", "karaj": "iran", "tabriz": "iran",
    # Italy
    "rome": "italy", "milan": "italy", "naples": "italy", "turin": "italy", "palermo": "italy",
    # Jordan
    "amman": "jordan", "zarqa": "jordan", "irbid": "jordan",
    # Cambodia
    "phnom penh": "cambodia", "siem reap": "cambodia", "battambang": "cambodia",
    # Canada
    "toronto": "canada", "montreal": "canada", "vancouver": "canada", "calgary": "canada", "edmonton": "canada", "ottawa": "canada",
    # Kenya
    "nairobi": "kenya", "mombasa": "kenya", "kisumu": "kenya",
    # South Korea
    "seoul": "south korea", "busan": "south korea", "incheon": "south korea", "daegu": "south korea",
    # North Korea
    "pyongyang": "north korea", "hamhung": "north korea", "chongjin": "north korea",
    # Croatia
    "zagreb": "croatia", "split": "croatia", "rijeka": "croatia",
    # Cuba
    "havana": "cuba", "santiago de cuba": "cuba", "camaguey": "cuba",
    # Kuwait
    "kuwait city": "kuwait", "al ahmadi": "kuwait", "hawalli": "kuwait",
    # Laos
    "vientiane": "laos", "pakse": "laos", "savannakhet": "laos",
    # Lebanon
    "beirut": "lebanon", "tripoli": "lebanon",
    # Libya
    "tripoli": "libya", "benghazi": "libya", "misrata": "libya",
    # Morocco
    "casablanca": "morocco", "rabat": "morocco", "fes": "morocco", "marrakesh": "morocco",
    # Mexico
    "mexico city": "mexico", "guadalajara": "mexico", "monterrey": "mexico", "puebla": "mexico",
    # Myanmar
    "yangon": "myanmar", "mandalay": "myanmar", "naypyidaw": "myanmar",
    # Namibia
    "windhoek": "namibia", "rundu": "namibia", "walvis bay": "namibia",
    # Nigeria
    "lagos": "nigeria", "kano": "nigeria", "ibadan": "nigeria", "abuja": "nigeria",
    # Norway
    "oslo": "norway", "bergen": "norway", "trondheim": "norway",
    # Pakistan
    "karachi": "pakistan", "lahore": "pakistan", "faisalabad": "pakistan", "islamabad": "pakistan",
    # Papua New Guinea
    "port moresby": "papua new guinea", "lae": "papua new guinea",
    # United Arab Emirates
    "dubai": "united arab emirates", "abu dhabi": "united arab emirates", "sharjah": "united arab emirates",
    # Poland
    "warsaw": "poland", "krakow": "poland", "lodz": "poland", "wroclaw": "poland",
    # Portugal
    "lisbon": "portugal", "porto": "portugal",
    # France
    "paris": "france", "marseille": "france", "lyon": "france", "toulouse": "france", "nice": "france",
    # Qatar
    "doha": "qatar", "al rayyan": "qatar",
    # Romania
    "bucharest": "romania", "cluj-napoca": "romania", "timisoara": "romania",
    # Russia
    "moscow": "russia", "saint petersburg": "russia", "novosibirsk": "russia", "yekaterinburg": "russia",
    # New Zealand
    "auckland": "new zealand", "wellington": "new zealand", "christchurch": "new zealand",
    # Senegal
    "dakar": "senegal", "touba": "senegal",
    # Slovakia
    "bratislava": "slovakia", "kosice": "slovakia",
    # Spain
    "madrid": "spain", "barcelona": "spain", "valencia": "spain", "seville": "spain",
    # Sri Lanka
    "colombo": "sri lanka", "sri jayawardenepura kotte": "sri lanka",
    # Sudan
    "khartoum": "sudan", "omdurman": "sudan",
    # Syria
    "damascus": "syria", "aleppo": "syria", "homs": "syria",
    # Suriname
    "paramaribo": "suriname",
    # Sweden
    "stockholm": "sweden", "gothenburg": "sweden", "malmo": "sweden",
    # Switzerland
    "zurich": "switzerland", "geneva": "switzerland", "basel": "switzerland", "bern": "switzerland",
    # Tanzania
    "dar es salaam": "tanzania", "dodoma": "tanzania", "mwanza": "tanzania",
    # Thailand
    "bangkok": "thailand", "nonthaburi": "thailand", "nakhon ratchasima": "thailand",
    # Timor Leste
    "dili": "timor leste", "baucau": "timor leste",
    # Tunisia
    "tunis": "tunisia", "sfax": "tunisia", "sousse": "tunisia",
    # Turkey
    "istanbul": "turkey", "ankara": "turkey", "izmir": "turkey", "bursa": "turkey",
    # Ukraine
    "kyiv": "ukraine", "kharkiv": "ukraine", "odesa": "ukraine", "kiev": "ukraine",
    # Uzbekistan
    "tashkent": "uzbekistan", "samarkand": "uzbekistan", "bukhara": "uzbekistan",
    # Venezuela
    "caracas": "venezuela", "maracaibo": "venezuela", "valencia": "venezuela",
    # Vietnam
    "ho chi minh city": "vietnam", "hanoi": "vietnam", "da nang": "vietnam",
    # Yemen
    "sanaa": "yemen", "aden": "yemen", "taiz": "yemen",
    # Greece
    "athens": "greece", "thessaloniki": "greece", "patras": "greece",
    # Zimbabwe
    "harare": "zimbabwe", "bulawayo": "zimbabwe"
}