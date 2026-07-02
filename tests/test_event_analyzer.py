from app.models.schemas import Event
from app.services.event_analyzer import analyze_event


def test_event_analyzer():
    event = Event(
        title="AI Summit",
        domain="Artificial Intelligence",
        location="Hyderabad"
    )

    result = analyze_event(event)

    assert result is not None