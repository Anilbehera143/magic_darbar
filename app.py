import streamlit as st

st.set_page_config(page_title="MAYA OS v7.0", page_icon="🌐", layout="wide")


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
