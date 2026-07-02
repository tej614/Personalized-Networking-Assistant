from app.models.schemas import Event
from app.services.topic_generator import generate_topics


def test_topic_generator():
    event = Event(
        title="AI Summit",
        domain="Artificial Intelligence",
        location="Hyderabad"
    )

    topics = generate_topics(event)

    assert len(topics) > 0