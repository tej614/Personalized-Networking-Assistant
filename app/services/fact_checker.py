import wikipedia

wikipedia.set_lang("en")

def check_facts(topics):
    verified_topics = []

    for topic in topics:
        try:
            summary = wikipedia.summary(topic, sentences=1)

            verified_topics.append({
                "topic": topic,
                "status": "Verified",
                "summary": summary
            })

        except wikipedia.exceptions.DisambiguationError as e:
            try:
                summary = wikipedia.summary(e.options[0], sentences=1)

                verified_topics.append({
                    "topic": topic,
                    "status": "Verified (Closest Match)",
                    "summary": summary
                })

            except Exception:
                verified_topics.append({
                    "topic": topic,
                    "status": "Multiple Results",
                    "summary": "Multiple Wikipedia articles match this topic."
                })

        except wikipedia.exceptions.PageError:
            verified_topics.append({
                "topic": topic,
                "status": "Not Found",
                "summary": "No Wikipedia article found."
            })

        except Exception as e:
            verified_topics.append({
                "topic": topic,
                "status": "Verification Failed",
                "summary": str(e)
            })

    return {
        "verified_topics": verified_topics,
        "status": "Completed"
    }