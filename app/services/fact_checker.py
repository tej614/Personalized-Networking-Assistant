import wikipedia

def check_facts(topics):
    verified_topics = []

    for topic in topics:
        try:
            # Check if Wikipedia has a page for the topic
            wikipedia.summary(topic, sentences=1)
            verified_topics.append(f"✅ {topic}")

        except wikipedia.exceptions.DisambiguationError:
            verified_topics.append(f"⚠️ {topic} (Multiple matches found)")

        except wikipedia.exceptions.PageError:
            verified_topics.append(f"❌ {topic} (Not found on Wikipedia)")

        except Exception:
            verified_topics.append(f"⚠️ {topic} (Unable to verify)")

    return {
        "verified_topics": verified_topics,
        "status": "Verification Completed"
    }