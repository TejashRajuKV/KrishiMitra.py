import streamlit as st
from datetime import datetime
import base64

# Import profit prediction dashboard
try:
    from profit_prediction_dashboard import integrate_profit_dashboard
    PROFIT_DASHBOARD_AVAILABLE = True
except ImportError:
    PROFIT_DASHBOARD_AVAILABLE = False

# ------------------ Language Data ------------------
LANGUAGE_DATA = {
    "English": {
        "welcome": "🌾 Welcome to KrishiMitra!",
        "fertilizer": "🌱 Fertilizer Recommendation",
        "loan": "🏦 Loan/Subsidy Checker",
        "weather_alert": "🌦️ Weather Alerts",
        "crop_calendar": "📅 Crop Calendar",
        "profit_prediction": "📊 Profit Prediction"
    },
    "Hindi": {
        "welcome": "🌾 कृषि मित्र में आपका स्वागत है!",
        "fertilizer": "🌱 उर्वरक सिफारिश",
        "loan": "🏦 ऋण/सब्सिडी जांच",
        "weather_alert": "🌦️ मौसम अलर्ट",
        "crop_calendar": "📅 फसल कैलेंडर",
        "profit_prediction": "📊 लाभ पूर्वानुमान"
    },
    "Bhojpuri": {
        "welcome": "🌾 कृषिमित्र में रउआ स्वागत बा!",
        "fertilizer": "🌱 खाद सिफारिश",
        "loan": "🏦 कर्ज/सब्सिडी जांच",
        "weather_alert": "🌦️ मौसम चेतावनी",
        "crop_calendar": "📅 फसल कैलेंडर",
        "profit_prediction": "📊 लाभ अनुमान"
    },
    "Punjabi": {
        "welcome": "🌾 ਕ੍ਰਿਸ਼ੀ ਮਿਤਰ ਵਿੱਚ ਤੁਹਾਡਾ ਸੁਆਗਤ ਹੈ!",
        "fertilizer": "🌱 ਖਾਦ ਸਿਫਾਰਸ਼",
        "loan": "🏦 ਕਰਜ਼ਾ ਜਾਂ ਸਬਸਿਡੀ ਚੈੱਕਰ",
        "weather_alert": "🌦️ ਮੌਸਮ ਚੇਤਾਵਨੀ",
        "crop_calendar": "📅 ਫਸਲ ਕੈਲੰਡਰ",
        "profit_prediction": "📊 ਲਾਭ ਪੂਰਵ ਅਨੁਮਾਨ"
    },
    "Tamil": {
        "welcome": "🌾 கிருஷிமித்ராவிற்கு வரவேற்கிறோம்!",
        "fertilizer": "🌱 உர பரிந்துரை",
        "loan": "🏦 கடன்/தொகை சரிபார்ப்பு",
        "weather_alert": "🌦️ வானிலை எச்சரிக்கை",
        "crop_calendar": "📅 பயிர் நாட்காட்டி",
        "profit_prediction": "📊 லாப கணிப்பு"
    },
    "Telugu": {
        "welcome": "🌾 కృషిమిత్రా కు స్వాగతం!",
        "fertilizer": "🌱 ఎరువు సిఫార్సు",
        "loan": "🏦 రుణం/సబ్సిడీ తనిఖీ",
        "weather_alert": "🌦️ వాతావరణ హెచ్చరికలు",
        "crop_calendar": "📅 పంట క్యాలెండర్",
        "profit_prediction": "📊 లాభ అంచనా"
    },
    "Kannada": {
        "welcome": "🌾 ಕೃಷಿ ಮಿತ್ರಕ್ಕೆ ಸ್ವಾಗತ!",
        "fertilizer": "🌱 ರಸಗೊಬ್ಬರ ಶಿಫಾರಸು",
        "loan": "🏦 ಸಾಲ/ಸಬ್ಸಿಡಿ ತಪಾಸಣೆ",
        "weather_alert": "🌦️ ಹವಾಮಾನ ಎಚ್ಚರಿಕೆ",
        "crop_calendar": "📅 ಬೆಳೆ ದಿನದರ್ಶಿ",
        "profit_prediction": "📊 ಲಾಭ ಮುನ್ಸೂಚನೆ"
    },
    "Awadhi": {
        "welcome": "🌾 कृषिमित्र मा तोहार स्वागत बा!",
        "fertilizer": "🌱 खाद सिफारिश",
        "loan": "🏦 कर्ज/सब्सिडी जांच",
        "weather_alert": "🌦️ मौसम चेतावनी",
        "crop_calendar": "📅 फसल कैलेंडर",
        "profit_prediction": "📊 लाभ पूर्वानुमान"
    }
    # Add other languages here as needed
}

# Place this right after your imports and before any UI code
def set_bg_from_url(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{image_url}");
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Example usage:
set_bg_from_url("https://ibb.co/n4w8k5F.jpg")

# ------------------ Sidebar for Language ------------------
st.sidebar.title("🌐 Select Language")
language = st.sidebar.selectbox("Choose your preferred language:", list(LANGUAGE_DATA.keys()))
lang_content = LANGUAGE_DATA[language]

# Store language in session state for profit dashboard
st.session_state.language = language

# ------------------ Main UI ------------------
st.title(lang_content["welcome"])

# ------------------ Navigation ------------------
st.markdown("---")
nav_col1, nav_col2, nav_col3, nav_col4, nav_col5 = st.columns(5)

with nav_col1:
    if st.button("🏠 Home", use_container_width=True):
        st.session_state.page = "home"

with nav_col2:
    if st.button(lang_content["fertilizer"], use_container_width=True):
        st.session_state.page = "fertilizer"

with nav_col3:
    if st.button(lang_content["loan"], use_container_width=True):
        st.session_state.page = "loan"

with nav_col4:
    if st.button(lang_content["weather_alert"], use_container_width=True):
        st.session_state.page = "weather"

with nav_col5:
    if PROFIT_DASHBOARD_AVAILABLE and st.button(lang_content["profit_prediction"], use_container_width=True):
        st.session_state.page = "profit_prediction"

st.markdown("---")

# Initialize page state
if 'page' not in st.session_state:
    st.session_state.page = "home"

# Page routing
if st.session_state.page == "profit_prediction" and PROFIT_DASHBOARD_AVAILABLE:
    integrate_profit_dashboard()
    st.stop()  # Stop executing the rest of the main page

# Show main content only if on home page or other specific pages
if st.session_state.page in ["home", "fertilizer", "loan", "weather"]:
    
    # ------------------ Fertilizer Recommendation ------------------
    st.header(lang_content["fertilizer"])
    fertilizer_info = {
        "Wheat": {
            "Black": "Apply 120 kg N, 60 kg P₂O₅, 40 kg K₂O per hectare. Use Urea, DAP, and MOP.",
            "Red": "Apply 100 kg N, 50 kg P₂O₅, 30 kg K₂O per hectare. Add 5 tonnes FYM before sowing.",
            "Sandy": "Use 90 kg N, 45 kg P₂O₅, and 25 kg K₂O. Split N into 2–3 doses.",
            "Brown": "Apply 110 kg N, 55 kg P₂O₅, 35 kg K₂O per hectare. Include organic manure."
        },
        "Rice": {
            "Black": "Apply 100 kg N, 50 kg P₂O₅, 50 kg K₂O per hectare. Use split application for N.",
            "Red": "Use 90 kg N, 40 kg P₂O₅, and 40 kg K₂O. Add zinc sulphate @ 25 kg/ha.",
            "Sandy": "Apply 80 kg N, 30 kg P₂O₅, and 30 kg K₂O. Water management is essential.",
            "Brown": "Use 90:45:45 NPK with green manure incorporation before transplanting."
        },
        "Maize": {
            "Black": "Apply 120 kg N, 60 kg P₂O₅, 40 kg K₂O. Use basal + top dressing method.",
            "Red": "Use 100:50:30 NPK with 5 tonnes FYM. Zinc and Boron may be needed.",
            "Sandy": "Apply 80 kg N, 40 kg P₂O₅, 20 kg K₂O. Split nitrogen application in 3 stages.",
            "Brown": "100 kg N, 50 kg P₂O₅, 30 kg K₂O per hectare. Use organic compost pre-sowing."
        },
        "Potato": {
            "Black": "150:80:120 NPK kg/ha. Apply FYM @ 25 tons/ha before sowing.",
            "Red": "120:60:100 NPK + 2 tonnes of compost. Potassium is critical for tuber growth.",
            "Sandy": "100:40:80 NPK. Add micronutrients like Boron if deficiency appears.",
            "Brown": "130:70:110 NPK. Ensure deep ploughing and ridge formation."
        },
        "Sugarcane": {
            "Black": "Apply 250:115:115 NPK. Apply in 3 split doses with organic matter.",
            "Red": "Use 225:100:100 NPK with 10 tonnes FYM. Micronutrients essential.",
            "Sandy": "200:90:90 NPK. Add press mud or compost for better results.",
            "Brown": "240:110:110 NPK + green manure or biofertilizer for soil enrichment."
        },
        "Tomato": {
            "Black": "100:60:60 NPK per ha. Add 10–15 tonnes FYM. Split nitrogen.",
            "Red": "80:40:50 NPK + Boron and Magnesium. Add neem cake for pest resistance.",
            "Sandy": "70:35:45 NPK. Frequent irrigation needed.",
            "Brown": "90:50:50 NPK + Trichoderma enriched compost for disease control."
        },
        "Mustard": {
            "Black": "80:40:30 NPK + 5 kg Zinc Sulphate. Ideal for higher oil yield.",
            "Red": "70:35:25 NPK. Sulphur application helps oil quality.",
            "Sandy": "60:30:20 NPK. Add FYM and maintain moisture.",
            "Brown": "75:40:25 NPK. Use neem-coated urea."
        }
    }
    crop = st.selectbox("Select Crop", list(fertilizer_info.keys()))
    soil = st.selectbox("Soil Type", list(fertilizer_info[crop].keys()))
    if st.button("Get Recommendation"):
        st.success(fertilizer_info[crop][soil])

    # ------------------ Loan/Subsidy Info ------------------
    st.header(lang_content["loan"])
    age = st.number_input("Enter your age", min_value=18, max_value=80)
    holding = st.selectbox("Land holding (acres)", ["<1", "1-5", ">5"])

    if st.button("Check Eligibility"):
        schemes = []

        # Age-based
        if age < 40:
            schemes.append("Kisan Credit Card (KCC)")
            schemes.append("PM-KISAN")
            schemes.append("Youth Agri Loan (NABARD)")
        elif age >= 60:
            schemes.append("Senior Farmer Pension Scheme")

        # Landholding-based
        if holding == "<1":
            schemes.extend([
                "PM-KISAN",
                "KALIA Scheme (Odisha)",
                "YSR Rythu Bharosa (Andhra Pradesh)",
                "Mukhya Mantri Krishi Ashirwad (Jharkhand)"
            ])
        elif holding == "1-5":
            schemes.extend([
                "NABARD Subsidized Loans",
                "Solar Pump Subsidy",
                "Crop Insurance Scheme (PMFBY)",
                "Fasal Bima Yojana"
            ])
        elif holding == ">5":
            schemes.extend([
                "NABARD Long-Term Projects",
                "Warehouse Construction Loans",
                "Tractor Subsidy Scheme"
            ])

        # Remove duplicates
        schemes = list(set(schemes))

        if schemes:
            st.success("✅ You are eligible for the following schemes:")
            for scheme in schemes:
                st.markdown(f"- {scheme}")
        else:
            st.warning("❌ Not eligible for current subsidies based on given inputs.")

    # ------------------ Government Schemes ------------------
    st.subheader("📜 Government Schemes")
    schemes = {
        "PM-KISAN": "₹6000/year in 3 installments",
        "PMFBY": "Crop insurance at low premium",
        "KCC": "Credit up to ₹3 lakh @ 4% interest",
        "NABARD": "Irrigation and farm infra support",
        "Mahila Kisan Sashaktikaran": "Skill, input and support for women farmers"
    }
    st.json(schemes)

    # ------------------ Weather Alerts ------------------
    st.header(lang_content["weather_alert"])
    region = st.selectbox("Select Region", ["Punjab", "UP", "MP", "Bihar"])
    weather_data = {
        "Punjab": "🌧️ Light rain expected tomorrow",
        "UP": "☀️ Clear skies today",
        "MP": "⛈️ Thunderstorms likely in evening",
        "Bihar": "🌦️ Cloudy with chances of rain"
    }
    st.warning(weather_data[region])

    # ------------------ Crop Calendar ------------------
    st.header(lang_content["crop_calendar"])
    season = st.selectbox("Choose Season", ["Rabi", "Kharif", "Zaid"])
    calendar_data = {
        "Rabi": "Wheat, Mustard, Barley",
        "Kharif": "Paddy, Maize, Bajra",
        "Zaid": "Watermelon, Cucumber"
    }
    st.success(calendar_data[season])

    # ------------------ Mandi Prices ------------------
    st.subheader("💸 Mandi Prices")
    mandi_data = {
        "wheat": "₹2200/qtl",
        "rice": "₹1800/qtl",
        "mustard": "₹5500/qtl",
        "maize": "₹1700/qtl",
        "barley": "₹1600/qtl",
        "soybean": "₹4800/qtl",
        "cotton": "₹6600/qtl",
        "groundnut": "₹5500/qtl",
        "sugarcane": "₹340/qtl",
        "potato": "₹1200/qtl",
        "onion": "₹900/qtl",
        "tomato": "₹1100/qtl",
        "bajra": "₹2150/qtl",
        "jowar": "₹2738/qtl",
        "urad dal": "₹6600/qtl",
        "moong dal": "₹7275/qtl",
        "chana": "₹5400/qtl",
        "masoor dal": "₹6000/qtl",
        "banana": "₹1500/qtl",
        "apple": "₹3000/qtl",
        "brinjal": "₹900/qtl",
        "carrot": "₹1100/qtl",
        "cabbage": "₹850/qtl",
        "peas": "₹1400/qtl"
    }
    st.table(mandi_data)

    # ------------------ Task Selection ------------------
    st.subheader("📋 Task for Today")
    tasks = ["Irrigation", "Apply pesticide to paddy", "Harvest tomatoes"]
    task = st.selectbox("Select Task", tasks)
    st.success(f"Your task for today: {task}")

    # ------------------ Footer ------------------
    st.markdown("---")
    st.markdown("Made with ❤️ for Indian Farmers - KrishiMitra")

# Display navigation info if profit dashboard is not available
if not PROFIT_DASHBOARD_AVAILABLE:
    st.sidebar.warning("📊 Profit Prediction feature unavailable. Please ensure profit_prediction_dashboard.py is in the same directory.")