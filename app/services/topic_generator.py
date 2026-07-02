from app.models.schemas import Event
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client=Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_topics(event:Event):
    response=client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role":"user",
                "content": f"Generate 3 networking conversation topics for an event in {event.domain}. Return each topic on a new line."
            }
        ]
    )
    print(response)