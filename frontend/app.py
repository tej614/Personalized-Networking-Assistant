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

    if response.status_code ==200:
        result=response.json()

        st.subheader("Suggested Topics")
        for topic in result["suggested_topics"]:
            st.write("•", topic)
        st.subheader("🤝 Networking Tips")

        for tip in result["networking_tips"]:
            st.write("•", tip)

        st.subheader("👤 AI Self Introduction")
        st.info(result["self_introduction"])

        st.subheader("Fact Check Status")
        st.success(result["fact_check_status"])

        st.subheader("Fact Check Status")

        st.success(result["fact_check_status"])
    else:
        st.error("Failed to connect to the FastAPI backend.")