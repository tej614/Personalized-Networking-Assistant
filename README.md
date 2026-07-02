# 🤖 Personalized Networking Assistant

An AI-powered networking companion that helps users prepare for conferences, seminars, workshops, and professional networking events by generating personalized networking topics, self-introductions, conversation starters, and networking tips using the Groq Large Language Model (LLM).

---

# 🌐 Live Demo

### 🚀 Frontend (Streamlit)

https://personalized-networking-assistant-sfh4ukgpsyn97gpeafimapp.streamlit.app

### ⚡ Backend API (Render)

https://personalized-networking-assistant-9p63.onrender.com

### 📖 Swagger API Documentation

https://personalized-networking-assistant-9p63.onrender.com/docs

### 💻 GitHub Repository

https://github.com/tej614/Personalized-Networking-Assistant

---

# 📌 Project Overview

Networking can be challenging, especially for students and professionals attending conferences, seminars, workshops, or technical events.

The Personalized Networking Assistant uses Artificial Intelligence to help users confidently interact with others by generating:

- 🎯 Personalized discussion topics
- 🤝 Networking tips
- 👤 Professional self-introduction
- 💬 Conversation starters
- 📜 Networking history
- ✅ Fact-checked suggestions

---

# ✨ Features

## AI Features

- AI Suggested Topics
- AI Networking Tips
- AI Self Introduction
- AI Conversation Starters

## Backend Features

- FastAPI REST API
- SQLite Database
- Event Analysis
- Fact Checking
- History Logging
- Feedback Logging

## Frontend Features

- Streamlit User Interface
- Interactive Forms
- Loading Spinner
- Networking History Display

## Testing

- Unit Testing using Pytest
- API Testing
- Backend Service Testing

---

# 🛠️ Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| FastAPI | Backend Framework |
| Streamlit | Frontend UI |
| Groq API | AI Response Generation |
| SQLite | Database |
| Pydantic | Data Validation |
| Requests | API Communication |
| Pytest | Unit Testing |
| Git & GitHub | Version Control |
| Render | Backend Deployment |
| Streamlit Community Cloud | Frontend Deployment |

---

# 📂 Project Structure

```
Personalized-Networking-Assistant
│
├── app
│   ├── models
│   ├── routers
│   ├── services
│   ├── config.py
│   └── main.py
│
├── frontend
│   └── app.py
│
├── tests
│
├── requirements.txt
├── README.md
├── .env.example
└── .gitignore
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/tej614/Personalized-Networking-Assistant.git
```

Move into the project directory

```bash
cd Personalized-Networking-Assistant
```

## Create Virtual Environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Configure Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

---

# ▶️ Run Locally

## Start Backend

```bash
uvicorn app.main:app --reload
```

Backend URL

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

## Start Frontend

Open another terminal

```bash
streamlit run frontend/app.py
```

Frontend URL

```
http://localhost:8501
```

---

# 🧪 Run Tests

```bash
python -m pytest
```

Expected Output

```
4 passed
```

---

# 🚀 Deployment

## Backend Deployment

Hosted using **Render**

### Build Command

```bash
pip install -r requirements.txt
```

### Start Command

```bash
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

Environment Variable

```
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

---

## Frontend Deployment

Hosted using **Streamlit Community Cloud**

Repository

```
tej614/Personalized-Networking-Assistant
```

Branch

```
main
```

Main File

```
frontend/app.py
```

---

# 📚 Project Documentation

The complete project submission contains the following documentation:

```
1. Brainstorming & Ideation
2. Requirement Analysis
3. Project Design Phase
4. Project Planning Phase
5. Project Development Phase
6. Project Testing
7. Project Documentation
8. Project Demonstration
```

---

# 📈 Future Enhancements

- User Authentication
- Resume Analysis
- LinkedIn Integration
- PDF Report Export
- Email Summary
- Multi-language Support
- AI Event Recommendation System

---

# 👥 Authors

This project was developed collaboratively by:

| Team Member | Role / Contribution |
|-------------|---------------------|
| **Garudappagari Pallavi** (Team Lead) | Project planning, coordination, and overall project management |
| **Dandu Thanishka Reddy** | Major contributor to development, implementation, and testing |
| **Gunturi Teja Sekhar Naidu** | Backend development, AI integration, deployment, GitHub management, and documentation |
| **Chandana Ganuga** | Documentation, testing support, and project assistance |


---

# 📄 License

This project is developed for educational, learning, and internship purposes.