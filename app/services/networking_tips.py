from app.models.schemas import User, Event
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_networking_tips(user: User, event: Event):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": f"""
Generate exactly 3 networking tips for a {user.profession} attending an event about {event.domain}.

Rules:
- Each tip should be less than 10 words.
- Be practical.
- Do not add numbering.
- Return one tip per line.
"""
            }
        ]
    )

    content = response.choices[0].message.content

    tips = [tip.strip() for tip in content.split("\n") if tip.strip()]

    return tips