import streamlit as st
import requests
st.set_page_config(page_title="Personalized Networking Assistant")
st.title("🤖 Personalized Networking Assistant")

name=st.text_input("Name")
profession=st.text_input("Profession")
interests=st.text_input("Interests (comma separated)")

event_title=st.text_input("Event Title")
domain=st.text_input("Domain")
location=st.text_input("Location")

generate=st.button("Generate")

if generate:
    data={
        "user":{
            "name":name,
            "profession":profession,
            "interests":interests.split(",")
        },
        "event":{
            "title":event_title,
            "domain":domain,
            "location":location
        }
    }

    response=requests.post(
        "http://127.0.0.1:8000/generate",
        json=data
    )

    st.write(response.json())