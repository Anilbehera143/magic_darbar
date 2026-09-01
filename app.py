import streamlit as st

st.set_page_config(page_title="ब्रह्मांड गैलेक्सी", page_icon="🌌", layout="centered")

# असली डीप-स्पेस गैलेक्सी और तारों भरा ब्रह्मांड
st.markdown("""
    <style>
    .stApp { background-color: #000003; }
    
    .space-container {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 85vh;
        position: relative;
        overflow: hidden;
    }

    /* असली घूमती हुई गैलेक्सी का कोर और आर्म्स */
    .true-galaxy {
        width: 320px;
        height: 320px;
        position: relative;
        animation: galaxy-spin 25s linear infinite;
    }

    /* गैलेक्सी का चमकीला केंद्र (Core) */
    .galaxy-core {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 90px;
        height: 90px;
        background: radial-gradient(circle, #ffffff 0%, #ffddaa 40%, #ff5500 70%, transparent 100%);
        border-radius: 50%;
        box-shadow: 0 0 50px #ffaa00, 0 0 100px #ff3300;
        z-index: 2;
    }

    /* गैलेक्सी की फैली हुई स्पाइरल भुजाएं */
    .spiral-arm-1, .spiral-arm-2 {
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        border-radius: 50%;
        border: 4px solid transparent;
        border-top-color: rgba(0, 242, 254, 0.7);
        border-right-color: rgba(120, 0, 255, 0.6);
        filter: blur(4px);
    }

    .spiral-arm-1 {
        animation: spin-clockwise 8s linear infinite;
    }

    .spiral-arm-2 {
        animation: spin-counter 12s linear infinite;
        transform: rotate(45deg);
        border-top-color: rgba(255, 0, 128, 0.7);
        border-left-color: rgba(0, 255, 200, 0.5);
    }

    @keyframes galaxy-spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }

    @keyframes spin-clockwise {
        0% { transform: rotate(0deg) scale(1); }
        50% { transform: rotate(180deg) scale(1.08); }
        100% { transform: rotate(360deg) scale(1); }
    }

    @keyframes spin-counter {
        0% { transform: rotate(360deg) scale(1.05); }
        50% { transform: rotate(180deg) scale(1); }
        100% { transform: rotate(0deg) scale(1.05); }
    }
    </style>

    <div class="space-container">
        <div class="true-galaxy">
            <div class="galaxy-core"></div>
            <div class="spiral-arm-1"></div>
            <div class="spiral-arm-2"></div>
        </div>
    </div>
""", unsafe_allow_html=True)
