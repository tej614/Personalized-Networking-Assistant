from app.models.schemas import Event

def generate_topics(event:Event):
    topics=[
        f"Latest trends in {event.domain}",
        f"Career opurtunities in {event.domain}",
        f"Innovations in {event.domain}"
    ]
    return topics