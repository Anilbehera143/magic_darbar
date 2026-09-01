import streamlit as st

st.set_page_config(page_title="ब्रह्मांड गैलेक्सी", page_icon="🌌", layout="centered")

# सिर्फ गैलेक्सी और ब्रह्मांड का कोड
st.markdown("""
    <style>
    .stApp { background-color: #010104; }
    
    .universe-container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 80vh;
    }
    
    .galaxy {
        width: 280px;
        height: 280px;
        border-radius: 50%;
        background: conic-gradient(from 0deg at 50% 50%, #ff007f, #7f00ff, #00f0ff, #00ffcc, #ffcc00, #ff007f);
        box-shadow: 0 0 90px #7f00ff, 0 0 160px #00f0ff, inset 0 0 60px #ffffff;
        animation: rotate-galaxy 10s linear infinite, pulse-galaxy 4s ease-in-out infinite alternate;
        position: relative;
    }

    .galaxy::before {
        content: '';
        position: absolute;
        top: 15px; left: 15px; right: 15px; bottom: 15px;
        border-radius: 50%;
        border: 2px dashed rgba(255, 255, 255, 0.5);
        animation: rotate-reverse 15s linear infinite;
    }

    .galaxy::after {
        content: '';
        position: absolute;
        top: 50px; left: 50px; right: 50px; bottom: 50px;
        border-radius: 50%;
        background: radial-gradient(circle, #ffffff 10%, rgba(127,0,255,0.6) 50%, transparent 80%);
        animation: pulse-galaxy 2s ease-in-out infinite alternate;
    }

    @keyframes rotate-galaxy {
        0% { transform: rotate(0deg) scale(1); }
        50% { transform: rotate(180deg) scale(1.04); }
        100% { transform: rotate(360deg) scale(1); }
    }

    @keyframes rotate-reverse {
        0% { transform: rotate(360deg); }
        100% { transform: rotate(0deg); }
    }

    @keyframes pulse-galaxy {
        0% { box-shadow: 0 0 60px #7f00ff, 0 0 100px #00f0ff; }
        100% { box-shadow: 0 0 120px #ff007f, 0 0 200px #00ffcc; }
    }
    </style>

    <div class="universe-container">
        <div class="galaxy"></div>
    </div>
""", unsafe_allow_html=True)
