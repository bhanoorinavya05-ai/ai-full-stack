import streamlit as from django.conf import settings

st.set_page_config(page_title = "Text Input Demo")
st.title ("text Input Demo")

name = st.text_input("Enter your name:", placeholder="e.g.bappa")
st.write(f"Hello, {name}!")

secret =  st.text_input("Enter your password:", type="password")
st.write(f"your password has {len(secret)} charatcer.")

comments * st.text_area("Any additional comments?",height = 150)
st.write(f"your wrote{len(comments)} characters.")

if.st.button ("submit"):
    st.write("You clicked on submit")
    
    show _message = st.chckbox ("Do you want an extra message?")
    if show_message:
        st.write("This is the message. Have a good day")c
        
        
        
        
        