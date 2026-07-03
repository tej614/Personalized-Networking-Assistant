import streamlit as st
import requests

st.set_page_config(
    page_title="Personalized Networking Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Personalized Networking Assistant")
st.caption("AI-powered networking companion for conferences, seminars, workshops, and professional events.")
st.divider()

# =======================
# Sidebar
# =======================
with st.sidebar:
    st.header("👤 User Details")

    name = st.text_input("Name")
    profession = st.text_input("Profession")
    interests = st.text_input("Interests (comma separated)")

    st.header("📅 Event Details")

    event_title = st.text_input("Event Title")
    domain = st.text_input("Domain")
    location = st.text_input("Location")

    generate = st.button("🚀 Generate Networking Plan")

# =======================
# Generate Response
# =======================

if generate:

    data = {
        "user": {
            "name": name,
            "profession": profession,
            "interests": [i.strip() for i in interests.split(",") if i.strip()]
        },
        "event": {
            "title": event_title,
            "domain": domain,
            "location": location
        }
    }

    with st.spinner("🤖 AI is generating your networking assistant..."):

        response = requests.post(
            "https://personalized-networking-assistant-9p63.onrender.com/generate",
            json=data
        )

    if response.status_code == 200:

        result = response.json()

        col1, col2, col3 = st.columns(3)

        col1.metric("Topics", len(result["suggested_topics"]))
        col2.metric("Tips", len(result["networking_tips"]))
        col3.metric("Starters", len(result["conversation_starters"]))

        st.divider()

        with st.expander("🎯 Suggested Topics", expanded=True):
            for topic in result["suggested_topics"]:
                st.markdown(f"### ✅ {topic['topic']}")
                st.write(f"**Status:** {topic['status']}")
                st.info(topic["summary"])
        with st.expander("🤝 Networking Tips"):
            for tip in result["networking_tips"]:
                st.write("•", tip)

        with st.expander("👤 AI Self Introduction"):
            st.info(result["self_introduction"])

        with st.expander("💬 Conversation Starters"):
            for starter in result["conversation_starters"]:
                st.write("•", starter)

        with st.expander("📜 Recent History"):
            for item in result["history"]:
                st.write(
                    f"👤 **{item[0]}** | 🎯 **{item[1]}** | 📅 {item[3]}"
                )

        st.success(f"✅ Fact Check Status: {result['fact_check_status']}")

    else:
        st.error("❌ Failed to connect to the FastAPI backend.")

st.divider()
st.caption("Built with ❤️ using FastAPI • Streamlit • Groq AI • SQLite")