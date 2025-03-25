import requests

class ResearchAgent:
    def __init__(self):
        self.api_key = "012a35cfc982244ca495138a89841ec21e8e832085ad305a0f8bb7dab28f5811"
        self.endpoint = "https://serpapi.com/search"

    def research_topic(self, topic):
        """Fetch search results using SerpAPI (Google Search API)"""
        params = {
            "q": topic,
            "hl": "en",
            "gl": "us",
            "api_key": self.api_key
        }

        try:
            response = requests.get(self.endpoint, params=params)
            data = response.json()

            results = [res["snippet"] for res in data.get("organic_results", []) if "snippet" in res]
            return results if results else ["No relevant content found."]

        except requests.exceptions.RequestException as e:
            print(f"❌ Error fetching research: {e}")
            return ["Research could not be retrieved due to an error."]
