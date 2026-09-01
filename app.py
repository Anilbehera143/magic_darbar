import streamlit as st

st.set_page_config(page_title="MAYA OS - AI System", page_icon="⚡", layout="wide")

# Futuristic MAYA OS Theme & Styling (Pure English)
st.markdown("""
    <style>
    .stApp { background-color: #030712; color: #00f0ff; font-family: 'Courier New', monospace; }
    
    [data-testid="stHeader"], [data-testid="stToolbar"] { display: none !important; }
    
    .main-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 85vh;
    }
    
    .maya-orb {
        width: 240px;
        height: 240px;
        border-radius: 50%;
        background: conic-gradient(from 0deg at 50% 50%, #ff007f, #7f00ff, #00f0ff, #00ff7f, #ff007f);
        box-shadow: 0 0 80px rgba(0, 240, 255, 0.7), inset 0 0 50px rgba(255, 255, 255, 0.5);
        animation: spin 6s linear infinite, pulse 3s ease-in-out infinite alternate;
        margin-bottom: 25px;
    }

    @keyframes spin {
        0% { transform: rotate(0deg) scale(1); }
        50% { transform: rotate(180deg) scale(1.03); }
        100% { transform: rotate(360deg) scale(1); }
    }

    @keyframes pulse {
        0% { box-shadow: 0 0 50px rgba(127, 0, 255, 0.8); }
        100% { box-shadow: 0 0 100px rgba(0, 240, 255, 1); }
    }

    .system-title {
        font-size: 28px;
        font-weight: bold;
        color: #00f0ff;
        text-shadow: 0 0 15px rgba(0, 240, 255, 0.8);
        text-align: center;
        letter-spacing: 2px;
    }

    .system-status {
        font-size: 14px;
        color: #10b981;
        margin-top: 5px;
        text-align: center;
        letter-spacing: 1px;
    }
    </style>

    <div class="main-container">
        <div class="maya-orb"></div>
        <div class="system-title">MAYA OS v7.0 // NEURAL INTERFACE</div>
        <div class="system-status">SYSTEM ONLINE -- ALL CORES ACTIVE</div>
    </div>
""", unsafe_allow_html=True)

# Chat and Voice Command Section (Fully in English)
st.markdown("---")
st.markdown("<h4 style='color: #a78bfa; text-align: center;'>AI Terminal Input</h4>", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello Anil, MAYA OS is fully initialized. Awaiting your command."}
    ]

for msg in st.session_state.messages:
    avatar = "⚡" if msg["role"] == "assistant" else "💻"
    with st.chat_message(msg["role"], avatar=avatar):
        st.markdown(msg["content"])

if prompt := st.chat_input("Enter command or query here..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="💻"):
        st.markdown(prompt)

    response = f"Command executed successfully: '{prompt}'. All neural parameters are operating at peak efficiency, Anil."
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant", avatar="⚡"):
        st.markdown(response)
