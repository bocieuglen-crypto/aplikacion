import streamlit as st.title
import google.generativeai as genai

# Çelësi yt
genai.configure(api_key="AIzaSyAaC3E9yvo_i8hP5EKi-naocH8DpwOqOPE")
model = genai.GenerativeModel("gemini-1.5-flash")

st.title("AI-ja Ime")
pye = st.text_input("Pyet diçka:")

if st.button("Dërgo"):
    if pye:
        r = model.generate_content(pye)
        st.write(r.text)