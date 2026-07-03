import requests
from urllib.parse import quote

HEADERS = {
    "User-Agent": "PersonalizedNetworkingAssistant/1.0"
}

def check_facts(topics):
    verified_topics = []

    for topic in topics:
        try:
            search_url = "https://en.wikipedia.org/w/api.php"

            params = {
                "action": "query",
                "list": "search",
                "srsearch": topic,
                "format": "json"
            }

            response = requests.get(
                search_url,
                params=params,
                headers=HEADERS,
                timeout=10
            )

            response.raise_for_status()

            data = response.json()

            results = data.get("query", {}).get("search", [])

            if not results:
                verified_topics.append({
                    "topic": topic,
                    "status": "Not Found",
                    "summary": "No Wikipedia article found."
                })
                continue

            title = quote(results[0]["title"])

            summary_response = requests.get(
                f"https://en.wikipedia.org/api/rest_v1/page/summary/{title}",
                headers=HEADERS,
                timeout=10
            )

            if summary_response.status_code == 200:
                summary_data = summary_response.json()

                verified_topics.append({
                    "topic": topic,
                    "status": "Verified",
                    "summary": summary_data.get(
                        "extract",
                        "Summary not available."
                    )
                })
            else:
                verified_topics.append({
                    "topic": topic,
                    "status": "Verified",
                    "summary": "Wikipedia page found."
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