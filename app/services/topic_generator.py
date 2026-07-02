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
                "content": f"""
                Generate exactly 3 short networking topics for an event about {event.domain}.

                Rules:
                -Each topic should be less then 6 words.
                -Do not ask questions.
                -Do not add numbering.
                -Do not add explanations.
                -Return one topic per line.
                """
            }
        ]
    )
    content=response.choices[0].message.content
    
    topics=content.split("\n")

    return topics