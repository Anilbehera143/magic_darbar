import streamlit as st

st.set_page_config(page_title="MAYA OS v7.0", page_icon="🌐", layout="wide")

# Full-Screen Ultimate MAYA OS & 3D Core UI (Pure English)
st.markdown("""
    <style>
    /* Force full screen dark mode and remove all margins */
    .stApp {
        background: radial-gradient(circle at center, #0a0f1d 0%, #000000 100%);
        color: #00f0ff;
        font-family: 'Courier New', monospace;
        overflow: hidden;
    }
    
    [data-testid="stHeader"], [data-testid="stToolbar"], footer {
        display: none !important;
    }
    
    /* Center container for the futuristic core */
    .maya-universe {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 78vh;
        width: 100vw;
    }

    /* 3D Holographic Spinning Globe / Core */
    .holo-globe {
        width: 280px;
        height: 280px;
        border-radius: 50%;
        background: conic-gradient(from 0deg at 50% 50%, #00f0ff, #7f00ff, #ff007f, #00ff7f, #00f0ff);
        box-shadow: 0 0 100px rgba(0, 240, 255, 0.6), inset 0 0 60px rgba(255, 255, 255, 0.8);
        animation: globe-spin 8s linear infinite, core-pulse 4s ease-in-out infinite alternate;
        position: relative;
    }

    .holo-globe::before {
        content: '';
        position: absolute;
        top: -10px; left: -10px; right: -10px; bottom: -10px;
        border-radius: 50%;
        border: 2px dashed rgba(0, 240, 255, 0.4);
        animation: ring-spin 12s linear infinite reverse;
    }

    @keyframes globe-spin {
        0% { transform: rotate(0deg) scale(1); }
        50% { transform: rotate(180deg) scale(1.04); }
        100% { transform: rotate(360deg) scale(1); }
    }

    @keyframes ring-spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }

    @keyframes core-pulse {
        0% { box-shadow: 0 0 60px rgba(127, 0, 255, 0.8), inset 0 0 40px rgba(255,255,255,0.5); }
        100% { box-shadow: 0 0 140px rgba(0, 240, 255, 1), inset 0 0 80px rgba(255,255,255,0.9); }
    }

    .system-heading {
        margin-top: 25px;
        font-size: 26px;
        font-weight: bold;
        color: #00f0ff;
        text-shadow: 0 0 20px rgba(0, 240, 255, 0.8);
        letter-spacing: 3px;
        text-align: center;
    }

    .system-status {
        font-size: 13px;
        color: #00ffcc;
        margin-top: 8px;
        letter-spacing: 2px;
        text-align: center;
        text-shadow: 0 0 10px rgba(0, 255, 204, 0.6);
    }
    </style>

    <div class="maya-universe">
        <div class="holo-globe"></div>
        <div class="system-heading">MAYA OS v7.0 // NEURAL INTERFACE</div>
        <div class="system-status">SYSTEM ONLINE -- ALL CORES ACTIVE & READY</div>
    </div>
""", unsafe_allow_html=True)

# Interactive Command Terminal Input
st.markdown("---")
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello Anil, MAYA OS core is fully synchronized. Awaiting your command."}
    ]

for msg in st.session_state.messages:
    avatar = "⚡" if msg["role"] == "assistant" else "💻"
    with st.chat_message(msg["role"], avatar=avatar):
        st.markdown(msg["content"])

if prompt := st.chat_input("Enter command into MAYA OS terminal..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="💻"):
        st.markdown(prompt)

    response = f"Command received and processed: '{prompt}'. All subsystems are operating at maximum capacity, Anil."
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant", avatar="⚡"):
        st.markdown(response)
