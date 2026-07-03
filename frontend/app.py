import streamlit as st
import requests

# -----------------------------
# Backend URL
# -----------------------------
BASE_URL = "http://127.0.0.1:8000"

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Personalized Networking Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("Personalized Networking Assistant")
st.write("Generate personalized networking suggestions for professional events.")

# -----------------------------
# Session State
# -----------------------------
if "result" not in st.session_state:
    st.session_state.result = None

if "history" not in st.session_state:
    st.session_state.history = []

if "feedback_history" not in st.session_state:
    st.session_state.feedback_history = []

# -----------------------------
# User Information
# -----------------------------
st.header("👤 User Information")

name = st.text_input("Name")
profession = st.text_input("Profession")
interests_input = st.text_input(
    "Interests (comma separated)",
    placeholder="AI, Machine Learning, Python"
)

# -----------------------------
# Event Information
# -----------------------------
st.header("📅 Event Information")

event_title = st.text_input("Event Title")
domain = st.text_input("Domain")
location = st.text_input("Location")

# -----------------------------
# Generate Button
# -----------------------------
generate = st.button("Generate Conversation")

# -----------------------------
# Generate Conversation
# -----------------------------
if generate:

    if not all([name, profession, event_title, domain]):
        st.warning("Please fill in all required fields.")

    else:

        interests = [
            i.strip()
            for i in interests_input.split(",")
            if i.strip()
        ]

        data = {
            "user": {
                "name": name,
                "profession": profession,
                "interests": interests
            },
            "event": {
                "title": event_title,
                "domain": domain,
                "location": location
            }
        }

        with st.spinner("Generating conversation suggestions..."):

            try:

                response = requests.post(
                    f"{BASE_URL}/generate-conversation",
                    json=data
                )

                if response.status_code == 200:

                    st.session_state.result = response.json()

                    st.success("Conversation generated successfully!")

                else:

                    st.error("Backend returned an error.")

            except Exception as e:

                st.error(f"Error: {e}")

# -----------------------------
# Display Results
# -----------------------------
if st.session_state.result:

    result = st.session_state.result

    st.header("🎯 Suggested Topics")

    for topic in result["suggested_topics"]:
        st.write(f"**Topic:** {topic['topic']}")
        st.write(f"Status: {topic['status']}")
        st.write(f"Summary: {topic['summary']}")
        st.divider()

    st.header("🤝 Networking Tips")

    for tip in result["networking_tips"]:
        st.write(f"• {tip}")

    st.header("👋 Self Introduction")

    st.write(result["self_introduction"])

    st.header("💬 Conversation Starters")

    for starter in result["conversation_starters"]:
        st.write(f"• {starter}")

    st.header("📜 Conversation History")

    if result["history"]:

        history = result["history"][-5:]

        for item in reversed(history):

            st.subheader(f"👤 {item[0]}")
            st.write(f"**📅 Event:** {item[1]}")

            st.write("**🎯 Topics:**")
            for topic in item[2].split(","):
                st.write(f"- {topic.strip()}")

            st.caption(f"🕒 {item[3]}")
            st.divider()

    else:
        st.info("No conversation history available.")

    st.header("✅ Fact Check Status")

    st.success(result["fact_check_status"])

# -----------------------------
# Feedback
# -----------------------------
st.header("👍 Feedback")

col1, col2 = st.columns(2)

if col1.button("👍 Good"):

    response = requests.post(
        f"{BASE_URL}/feedback",
        json={
            "user_name": name,
            "feedback": "Good"
        }
    )

    if response.status_code == 200:
        st.success("Thank you for your feedback!")

if col2.button("👎 Bad"):

    response = requests.post(
        f"{BASE_URL}/feedback",
        json={
            "user_name": name,
            "feedback": "Bad"
        }
    )

    if response.status_code == 200:
        st.success("Thank you for your feedback!")

# -----------------------------
# Feedback History
# -----------------------------
st.header("📝 Feedback History")

try:
    response = requests.get(f"{BASE_URL}/feedback-history")

    if response.status_code == 200:

        feedbacks = response.json()

        if feedbacks:

            for item in reversed(feedbacks[-10:]):

                icon = "👍" if item["feedback"] == "Good" else "👎"

                st.write(f"{icon} {item['user']} - {item['feedback']}")

        else:
            st.info("No feedback history available.")

except Exception as e:
    st.error(f"Unable to load feedback history: {e}")