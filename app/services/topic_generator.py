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
                Generate exactly 3 networking discussion topics for an event in the {event.domain} domain.

                Rules:
                - Each topic must be 1 to 3 words only.
                - Each topic should correspond to an existing Wikipedia article.
                - Use well-known technical concepts, technologies, industries, or research fields.
                - Avoid phrases like "AI in Business", "Future of AI Systems", "Tech Trends", or "Market Trends".
                - Do not ask questions.
                - Do not add numbering.
                - Do not add explanations.
                - Return only one topic per line.

                Examples for AI:
                Artificial Intelligence
                Machine Learning
                Robotics

                Examples for Python:
                Python Programming
                Data Science
                Flask

                Examples for Agriculture:
                Tomato
                Agriculture
                Horticulture
                """
            }
        ]
    )
    content=response.choices[0].message.content
    
    topics= [topic.strip() for topic in content.split("\n") if topic.strip()]

    return topics