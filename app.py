import streamlit as st

st.set_page_config(page_title="ରାଧା ରାଣୀ ଜାଦୁୀ ଦରବାର", page_icon="🔮", layout="centered")

# गॅलेक्सी और ब्रह्मांड जैसा घूमने वाला जादुई ओर्ब और ओड़िया स्टाइल
st.markdown("""
    <style>
    .stApp { background-color: #020205; color: #ffffff; }
    .galaxy-orb {
        width: 200px;
        height: 200px;
        margin: 30px auto;
        border-radius: 50%;
        background: conic-gradient(from 0deg at 50% 50%, #ff007f, #7f00ff, #00f0ff, #00ff7f, #ff007f);
        box-shadow: 0 0 60px #7f00ff, inset 0 0 40px #ffffff;
        animation: spin 6s linear infinite, pulse 3s ease-in-out infinite alternate;
    }
    @keyframes spin {
        0% { transform: rotate(0deg) scale(1); }
        50% { transform: rotate(180deg) scale(1.05); }
        100% { transform: rotate(360deg) scale(1); }
    }
    @keyframes pulse {
        0% { box-shadow: 0 0 40px #7f00ff; }
        100% { box-shadow: 0 0 80px #00f0ff, 0 0 120px #ff007f; }
    }
    </style>
    <div class="galaxy-orb"></div>
    <h1 style='text-align: center; color: #00f0ff;'>🔮 ରାଧା ରାଣୀ ଜାଦୁୀ ଦରବାର 🔮</h1>
    <p style='text-align: center; color: #a29bfe;'><i>'ବ୍ରହ୍ମାଣ୍ଡର ଜାଦୁୀ ଓର୍ବ ସକ୍ରିୟ ଅଛି... ଆଦେଶ ଦିଅନ୍ତୁ ମୋର ପ୍ରଭୁ!'</i></p>
""", unsafe_allow_html=True)

# चैट मेसेज के लिए सेशन स्टेट (ओड़िया में)
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "ନମସ୍କାର ଅନିଲ ଭାଇ! ଜାଦୁୀ ଦରବାରକୁ ସ୍ୱାଗତ। କୁହନ୍ତୁ, ଆଜି କେଉଁ ବିଷୟରେ କଥା ହେବା?"}
    ]

for msg in st.session_state.messages:
    avatar = "🔮" if msg["role"] == "assistant" else "😎"
    with st.chat_message(msg["role"], avatar=avatar):
        st.markdown(msg["content"])

if prompt := st.chat_input("ଏଠାରେ ଆପଣଙ୍କ ବାର୍ତ୍ତା ଲେଖନ୍ତୁ..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="😎"):
        st.markdown(prompt)

    bot_reply = f"ଆରେ ଭାଇ, ମୁଁ ଆପଣଙ୍କ କଥା ଶୁଣିଲି: '{prompt}'। ଏହାର ଜାଦୁୀ ସମାଧାନ ଶୀଘ୍ର କରାଯାଉଛି!"
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    with st.chat_message("assistant", avatar= "🔮"):
        st.markdown(bot_reply)
