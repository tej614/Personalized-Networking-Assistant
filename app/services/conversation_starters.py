from app.models.schemas import User, Event
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_conversation_starters(user: User, event: Event):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": f"""
Generate exactly 3 conversation starters for a {user.profession}
attending an event about {event.domain}.

Rules:
- Each starter should be one sentence.
- Be friendly and professional.
- Do not add numbering.
- Return one starter per line.
"""
            }
        ]
    )

    content = response.choices[0].message.content

    starters = [
        starter.strip()
        for starter in content.split("\n")
        if starter.strip()
    ]

    return starters