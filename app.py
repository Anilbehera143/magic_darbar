import streamlit as st

st.set_page_config(page_title="राधा रानी जादुई दरबार", page_icon="🌌", layout="wide")

# वीडियो बैकग्राउंड और दिव्य दरबार का फाइनल कोड
st.markdown("""
    <style>
    /* Streamlit के डिफ़ॉल्ट मार्जिन हटाना */
    [data-testid="stAppViewContainer"] {
        background: #000000;
        padding: 0 !important;
        overflow: hidden;
    }
    [data-testid="stHeader"], [data-testid="stToolbar"] {
        display: none !important;
    }
    
    /* बैकग्राउंड वीडियो को पूरी स्क्रीन पर सेट करना */
    .bg-video {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        object-fit: cover;
        z-index: 1;
    }

    /* नीचे दरबार का बैनर */
    .darbar-banner {
        position: fixed;
        bottom: 30px;
        left: 50%;
        transform: translateX(-50%);
        text-align: center;
        z-index: 10;
        background: rgba(0, 0, 0, 0.7);
        padding: 10px 25px;
        border-radius: 25px;
        border: 1px solid rgba(0, 240, 255, 0.4);
        box-shadow: 0 0 25px rgba(127, 0, 255, 0.8);
    }
    </style>

    <video autoplay muted loop playsinline class="bg-video">
        <source src="https://assets.mixkit.co/videos/preview/mixkit-galaxy-in-space-4264-large.mp4" type="video/mp4">
    </video>
    
    <div class="darbar-banner">
        <h2 style='color: #00f0ff; margin: 0; font-size: 22px; text-shadow: 0 0 10px #00f0ff;'>🔮 राधा रानी जादुई दरबार 🔮</h2>
        <p style='color: #ffffff; margin: 3px 0 0 0; font-size: 13px;'><i>अरे अनिल भाई, दिव्य दरबार सज चुका है!</i></p>
    </div>
""", unsafe_allow_html=True)
