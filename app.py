import streamlit as st

st.set_page_config(page_title="Magic Galaxy", page_icon="🌌", layout="centered")

# सिर्फ असली ब्रह्मांड की गैलेक्सी दिखाने के लिए साफ़-सुथरा कोड
st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    
    .universe-box {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 85vh;
        width: 100%;
    }
    
    .galaxy-frame {
        width: 350px;
        height: 350px;
        border-radius: 50%;
        overflow: hidden;
        box-shadow: 0 0 50px rgba(127, 0, 255, 0.8), 0 0 100px rgba(0, 240, 255, 0.6);
        border: 2px solid rgba(255, 255, 255, 0.2);
    }

    .galaxy-frame img {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }
    </style>

    <div class="universe-box">
        <div class="galaxy-frame">
            <img src="https://media.giphy.com/media/3oKIPnAiaMCws8nOsE/giphy.gif" alt="Universe Galaxy">
        </div>
    </div>
""", unsafe_allow_html=True)
