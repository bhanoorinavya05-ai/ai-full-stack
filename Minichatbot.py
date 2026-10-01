from ollama import chat
import streamlit as st

st.set_page_config(page_title = "LlamaBot App" , page_icon = "bot")
st.title("LlamaBot - Here to talk!")

personality = "you are a strict and patient tutor named Llama. Answer warmly. Keep the answers within one sentence."
personality_2 = "you are a Singer. Answer in the form of poems. keep it simple."

if "history" not in st.session_state:
    st.session_state.history = [{"role" : "system", "content": personality}]

if "toast_msg" not in st.session_state:
    st.session_state.toast_msg = None

if st.session_state.toast_msg:
    st.toast(st.session_state.toast_msg[0], icon= st.session_state.toast_msg[1])

with st.sidebar:
    st.header("Chat Controls")
    if st.button("Clear Chat", type= "primary"):
        st.session_state.history = [{"role" : "system", "content": personality}]
        st.session_state.toast_msg = ("Chat cleared successfully!", "🗑️")
        st.rerun()
    if st.button("Change Personality"):
        st.session_state.history[0]["content"] = personality_2
        st.session_state.toast_msg = ("Bot personality changed successfully!", "😈")
        st.rerun()
    if st.button("reset personality"):
            st.session_state.history[0]["content"] = personality
            st.session_state.toast_msg = ("Bot personality has reset successfully","😡")
            st.rerun()


with st.chat_message("assistant"):
    st.write("Hello! I'm Llama. Ask something to get started.")

for msg in st.session_state.history[1:]:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

question = st.chat_input("Type something....")  
if question:
    st.session_state.history.append({"role" : "user", "content": question})

    with st.chat_message("user"):
        st.write(question)

    try:
        with st.spinner("Thinking..."):
            response = chat(model="llama3.2", messages = st.session_state.history)

        reply = response["message"]["content"]
        st.session_state.history.append({"role": "assistant", "content":reply})

        with st.chat_message("assistant"):
            st.write(reply)
    except Exception as e:
        st.write("Ollama is not working. Try again.")
        
        
        
        