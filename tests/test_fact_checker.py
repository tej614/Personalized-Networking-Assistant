from app.services.fact_checker import check_facts


def test_fact_checker():
    topics = [
        "Artificial Intelligence",
        "Machine Learning"
    ]

    result = check_facts(topics)

    assert "verified_topics" in result
    assert "status" in result