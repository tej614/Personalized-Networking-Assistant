from .conftest import client


def test_generate_route():
    payload = {
        "user": {
            "name": "Tej",
            "profession": "Student",
            "interests": ["Python", "AI"]
        },
        "event": {
            "title": "AI Summit",
            "domain": "Artificial Intelligence",
            "location": "Hyderabad"
        }
    }

    response = client.post("/generate", json=payload)

    assert response.status_code == 200

    data = response.json()

    assert "suggested_topics" in data
    assert "networking_tips" in data
    assert "self_introduction" in data
    assert "conversation_starters" in data
    assert "history" in data
    assert "fact_check_status" in data