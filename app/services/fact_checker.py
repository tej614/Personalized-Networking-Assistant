import wikipedia

wikipedia.set_lang("en")


def check_facts(topics):
    verified_topics = []

    for topic in topics:
        try:
            # Search for the closest matching Wikipedia page
            results = wikipedia.search(topic)

            if results:
                summary = wikipedia.summary(results[0], sentences=1)

                verified_topics.append({
                    "topic": topic,
                    "status": "Verified",
                    "summary": summary
                })
            else:
                verified_topics.append({
                    "topic": topic,
                    "status": "Not Found",
                    "summary": "No Wikipedia article found."
                })

        except wikipedia.exceptions.DisambiguationError:
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