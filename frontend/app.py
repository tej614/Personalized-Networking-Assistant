import streamlit as st
import requests

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Personalized Networking Assistant",
    page_icon="🤖",
    layout="wide"
)

# -----------------------------
# Header
# -----------------------------
st.title("🤖 Personalized Networking Assistant")
st.markdown(
    """
Welcome! Generate AI-powered networking suggestions, conversation starters,
self introductions and professional networking tips for your next event.
"""
)

st.divider()

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:

    st.title("⚙️ Input Details")

    st.subheader("👤 User Information")

    name = st.text_input("Name")
    profession = st.text_input("Profession")
    interests = st.text_input("Interests (comma separated)")

    st.divider()

    st.subheader("📅 Event Information")

    event_title = st.text_input("Event Title")
    domain = st.text_input("Domain")
    location = st.text_input("Location")

    st.divider()

    generate = st.button(
        "🚀 Generate Networking Plan",
        use_container_width=True
    )

# -----------------------------
# Generate
# -----------------------------
if generate:

    if not name or not profession or not event_title or not domain:

        st.warning("⚠️ Please fill all required fields.")

    else:

        data = {
            "user": {
                "name": name,
                "profession": profession,
                "interests": [
                    i.strip()
                    for i in interests.split(",")
                    if i.strip()
                ]
            },
            "event": {
                "title": event_title,
                "domain": domain,
                "location": location
            }
        }

        with st.spinner("🤖 AI is preparing your networking assistant..."):

            try:

                response = requests.post(
                    "https://personalized-networking-assistant-9p63.onrender.com/generate",
                    json=data,
                    timeout=60
                )

                if response.status_code == 200:

                    result = response.json()

                    st.success("✅ Networking Plan Generated Successfully!")

                    # -----------------------------
                    # Metrics
                    # -----------------------------

                    c1, c2, c3 = st.columns(3)

                    c1.metric(
                        "🎯 Topics",
                        len(result["suggested_topics"])
                    )

                    c2.metric(
                        "🤝 Tips",
                        len(result["networking_tips"])
                    )

                    c3.metric(
                        "💬 Starters",
                        len(result["conversation_starters"])
                    )

                    st.divider()

                    # -----------------------------
                    # Topics
                    # -----------------------------

                    with st.expander("🎯 Suggested Networking Topics", expanded=True):

                        for topic in result["suggested_topics"]:

                            status = topic["status"]

                            if status == "Verified":
                                icon = "✅"
                            elif status == "Not Found":
                                icon = "❌"
                            else:
                                icon = "⚠️"

                            st.markdown(f"### {icon} {topic['topic']}")
                            st.write(f"**Status:** {status}")
                            st.info(topic["summary"])

                    # -----------------------------
                    # Tips
                    # -----------------------------

                    with st.expander("🤝 Networking Tips"):

                        for tip in result["networking_tips"]:
                            st.markdown(f"✅ {tip}")

                    # -----------------------------
                    # Self Introduction
                    # -----------------------------

                    with st.expander("👤 AI Self Introduction"):

                        st.success(result["self_introduction"])

                    # -----------------------------
                    # Conversation Starters
                    # -----------------------------

                    with st.expander("💬 Conversation Starters"):

                        for starter in result["conversation_starters"]:
                            st.markdown(f"➡️ {starter}")

                    # -----------------------------
                    # History
                    # -----------------------------

                    with st.expander("📜 Recent History"):

                        if result["history"]:

                            for item in result["history"]:

                                st.markdown(
                                    f"""
**👤 User:** {item[0]}

**🎯 Event:** {item[1]}

**📅 Date:** {item[3]}

---
"""
                                )

                        else:
                            st.info("No previous history found.")

                    # -----------------------------
                    # Fact Check
                    # -----------------------------

                    if result["fact_check_status"] == "Completed":

                        st.success(
                            "✅ AI Validation Completed Successfully"
                        )

                    else:

                        st.warning(
                            result["fact_check_status"]
                        )

                else:

                    st.error(
                        "❌ Backend returned an unexpected response."
                    )

            except requests.exceptions.ConnectionError:

                st.error(
                    "❌ Unable to connect to the backend server."
                )

            except Exception as e:

                st.error(str(e))

# -----------------------------
# Footer
# -----------------------------
st.divider()

st.markdown(
    """
<center>

Developed using ❤️

**FastAPI • Streamlit • Groq AI • SQLite**

</center>
""",
    unsafe_allow_html=True
)