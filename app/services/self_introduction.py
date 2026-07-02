from app.models.schemas import User, Event
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_self_introduction(user: User, event: Event):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": f"""
Generate a professional self introduction.

Name: {user.name}
Profession: {user.profession}
Interests: {", ".join(user.interests)}
Event: {event.title}

Rules:
- Maximum 60 words.
- Friendly and professional.
- Ready to speak at a networking event.
"""
            }
        ]
    )

    intro = response.choices[0].message.content.strip()
    intro = intro.strip('"')

    return intro