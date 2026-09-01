import streamlit as st

st.set_page_config(page_title="Magic Galaxy", page_icon="🌌", layout="wide")

# पूरी स्क्रीन पर फैली हुई और धीरे-धीरे घूमने वाली असली गैलेक्सी का कोड
st.markdown("""
    <style>
    /* Streamlit के डिफ़ॉल्ट मार्जिन और हेडर हटाकर पूरी स्क्रीन खाली करना */
    [data-testid="stAppViewContainer"] {
        background: #000000;
        padding: 0 !important;
        overflow: hidden;
    }
    [data-testid="stHeader"], [data-testid="stToolbar"] {
        display: none !important;
    }
    
    .full-screen-galaxy {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        background-image: url('https://images.unsplash.com/photo-1506703719100-a0f3a48c0f86?q=80&w=2000&auto=format&fit=crop');
        background-size: cover;
        background-position: center;
        animation: rotate-universe 40s linear infinite;
        z-index: 1;
    }

    @keyframes rotate-universe {
        0% { transform: scale(1) rotate(0deg); }
        50% { transform: scale(1.08) rotate(180deg); }
        100% { transform: scale(1) rotate(360deg); }
    }
    </style>

    <div class="full-screen-galaxy"></div>
""", unsafe_allow_html=True)
