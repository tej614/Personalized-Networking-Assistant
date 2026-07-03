import requests

def check_facts(topics):
    verified_topics = []

    for topic in topics:
        try:
            # Search Wikipedia
            search_url = "https://en.wikipedia.org/w/api.php"

            params = {
                "action": "query",
                "list": "search",
                "srsearch": topic,
                "format": "json"
            }

            response = requests.get(search_url, params=params, timeout=10)
            data = response.json()

            results = data["query"]["search"]

            if results:
                title = results[0]["title"]

                summary_url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{title}"
                summary = requests.get(summary_url, timeout=10).json()

                verified_topics.append({
                    "topic": topic,
                    "status": "Verified",
                    "summary": summary.get("extract", "Summary not available.")
                })

            else:
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