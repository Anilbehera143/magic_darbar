import streamlit as st

st.set_page_config(page_title="राधा रानी जादुई दरबार", page_icon="🔮", layout="centered")

# जादुई स्टाइल और 3D ओर्ब (गोले) के लिए डिजाइन
st.markdown("""
    <style>
    .stApp { background-color: #050508; color: #ffffff; }
    .magic-orb {
        width: 180px;
        height: 180px;
        margin: 20px auto;
        border-radius: 50%;
        background: radial-gradient(circle at 30% 30%, #00ffcc, #0066ff, #050508);
        box-shadow: 0 0 50px #00ffcc, inset 0 0 30px #ffffff;
        animation: pulse 3s infinite alternate;
    }
    @keyframes pulse {
        0% { transform: scale(0.95); box-shadow: 0 0 30px #00ffcc; }
        100% { transform: scale(1.05); box-shadow: 0 0 60px #00ffcc, 0 0 90px #0066ff; }
    }
    </style>
    <div class="magic-orb"></div>
    <h1 style='text-align: center; color: #00ffcc;'>🔮 राधा रानी जादुई दरबार 🔮</h1>
    <p style='text-align: center; color: #8892b0;'><i>'जिन्न का जादुई ओर्ब सक्रिय है... हुक्म दीजिए मेरे आका!'</i></p>
""", unsafe_allow_html=True)

# चैट मेसेज के लिए सेशन स्टेट
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "नमस्कार अनिल भाई! जादुई दरबार में आपका स्वागत है। बताइए आज क्या बात करनी है?"}
    ]

for msg in st.session_state.messages:
    avatar = "🔮" if msg["role"] == "assistant" else "😎"
    with st.chat_message(msg["role"], avatar=avatar):
        st.markdown(msg["content"])

if prompt := st.chat_input("यहाँ अपना संदेश लिखें..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="😎"):
        st.markdown(prompt)

    bot_reply = f"अरे भाई, मैंने आपका संदेश सुन लिया है: '{prompt}'। जादुई सिस्टम पर इस पर काम चल रहा है!"
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    with st.chat_message("assistant", avatar="🔮"):
        st.markdown(bot_reply)
    
