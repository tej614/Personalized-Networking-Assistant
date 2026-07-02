# 🤖 Personalized Networking Assistant

## 📌 Overview

Personalized Networking Assistant is an AI-powered application that helps users prepare for networking events by generating conversation topics, networking tips, self-introductions, and conversation starters using the Groq LLM.

---

## 🚀 Features

- AI Suggested Networking Topics
- AI Networking Tips
- AI Self Introduction
- AI Conversation Starters
- Event Analysis
- Fact Checking
- SQLite History Storage
- Feedback Logging
- Streamlit Frontend
- FastAPI Backend
- Unit Tests using Pytest

---

## 🛠️ Technologies Used

- Python
- FastAPI
- Streamlit
- Groq API
- SQLite
- Pytest
- Pydantic

---

## 📂 Project Structure

```
app/
    models/
    routers/
    services/

frontend/

tests/

README.md
requirements.txt
```

---

## ⚙️ Installation

```bash
git clone <repository-url>

cd Personalized-Networking-Assistant

pip install -r requirements.txt
```

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Run Backend

```bash
uvicorn app.main:app --reload
```

---

## ▶️ Run Frontend

```bash
streamlit run frontend/app.py
```

---

## 🧪 Run Tests

```bash
python -m pytest
```

---


## 👨‍💻 Author

Tej Gunturi