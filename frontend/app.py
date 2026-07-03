import streamlit as st
import requests
from pathlib import Path

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Personalized Networking Assistant",
    page_icon="🤖",
    layout="wide"
)

# -----------------------------
# Load CSS
# -----------------------------
css_file = Path(__file__).parent / "style.css"

with open(css_file) as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )
st.title("🤖 Personalized Networking Assistant")
st.markdown("""
### 🚀 Your AI Networking Companion

Generate personalized networking topics, professional introductions,
conversation starters, networking tips and AI-powered recommendations
for conferences, seminars, workshops and professional events.
""")

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

                            st.markdown(f"""
                            <div style="
                            background:white;
                            padding:15px;
                            border-radius:10px;
                            border-left:5px solid #2563eb;
                            margin-bottom:15px;
                            box-shadow:0px 2px 8px rgba(0,0,0,.08);
                            ">

                            <h4>{icon} {topic['topic']}</h4>

                            <b>Status:</b> {status}<br><br>

                            {topic["summary"]}

                            </div>
                            """, unsafe_allow_html=True)

                    # -----------------------------
                    # Tips
                    # -----------------------------

                    with st.expander("🤝 Networking Tips"):

                        for tip in result["networking_tips"]:
                            st.success(tip)

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
                            st.info(starter)

                    # -----------------------------
                    # History
                    # -----------------------------

                    with st.expander("📜 Recent History"):

                        if result["history"]:

                            for item in result["history"]:

                                st.markdown(f"""
                                <div style="
                                background:white;
                                padding:15px;
                                border-radius:10px;
                                border-left:4px solid #2563eb;
                                margin-bottom:10px;
                                ">

                                👤 <b>{item[0]}</b><br>
                                🎯 {item[1]}<br>
                                📅 {item[3]}

                                </div>
                                """, unsafe_allow_html=True)

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

st.markdown("""
<div style="text-align:center;color:gray">

### 🤖 Personalized Networking Assistant

Powered by **FastAPI • Groq AI • Streamlit • SQLite**

</div>
""", unsafe_allow_html=True)