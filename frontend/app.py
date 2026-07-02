import streamlit as st
import requests
st.set_page_config(page_title="Personalized Networking Assistant")
st.title("🤖 Personalized Networking Assistant")
st.caption("AI-powered networking companion for conferences, seminars, and professional events.")

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

    with st.spinner("🤖 AI is generating your networking assistant..."):
        response = requests.post(
            "http://127.0.0.1:8000/generate",
            json=data
        )

    if response.status_code ==200:
        result=response.json()

        st.markdown("## 🎯 Suggested Topics")
        for topic in result["suggested_topics"]:
            st.write("•", topic)
        st.markdown("## 🤝 Networking Tips")

        for tip in result["networking_tips"]:
            st.write("•", tip)

        st.markdown("## 👤 AI Self Introduction")
        st.info(result["self_introduction"])
        st.markdown("## 💬 Conversation Starters")

        for starter in result["conversation_starters"]:
            st.write("•", starter)


        st.markdown("## ✅ Fact Check Status")
        st.success(result["fact_check_status"])
        st.markdown("## 📜 Recent History")

        for item in result["history"]:
            st.write(
                f"👤 {item[0]} | 📅 {item[3]} | 🎯 {item[1]}"
            )

    else:
        st.error("Failed to connect to the FastAPI backend.")