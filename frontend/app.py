import streamlit as st
st.set_page_config(page_title="Personalized Networking Assistant")
st.title("🤖 Personalized Networking Assistant")

name=st.text_input("Name")
profession=st.text_input("Profession")
interests=st.text_input("Interests (comma separated)")

event_title=st.text_input("Event Title")
domain=st.text_input("Domain")
location=st.text_input("Location")

generate=st.button("Generate")
