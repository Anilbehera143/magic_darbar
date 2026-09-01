import streamlit as st

st.set_page_config(page_title="Magic Galaxy", page_icon="🌌", layout="centered")

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
        width: 380px;
        height: 380px;
        border-radius: 50%;
        overflow: hidden;
        box-shadow: 0 0 70px rgba(138, 43, 226, 0.9), 0 0 140px rgba(0, 240, 255, 0.7);
        border: 2px solid rgba(255, 255, 255, 0.3);
    }

    .galaxy-frame img {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }
    </style>

    <div class="universe-box">
        <div class="galaxy-frame">
            <img src="https://images.unsplash.com/photo-1506703719100-a0f3a48c0f86?q=80&w=1000&auto=format&fit=crop" alt="Real Spiral Galaxy">
        </div>
    </div>
""", unsafe_allow_html=True)
