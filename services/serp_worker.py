import requests
from bs4 import BeautifulSoup
import json
import time

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def fetch_serp(query):
    url = f"https://duckduckgo.com/html/?q={query}"
    res = requests.get(url, headers=HEADERS, timeout=10)

    soup = BeautifulSoup(res.text, "html.parser")
    results = []

    for r in soup.select(".result__body")[:5]:
        title = r.select_one(".result__title").get_text(strip=True)
        snippet = r.select_one(".result__snippet")
        results.append({
            "title": title,
            "snippet": snippet.get_text(strip=True) if snippet else ""
        })

    return results


def run_autonomous_serp():
    while True:
        data = {
            "astrology": fetch_serp("daily horoscope astrology"),
            "courses": fetch_serp("best programming courses 2026"),
            "marketing": fetch_serp("stock market trends today")
        }

        with open("data/serp_data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

        time.sleep(60 * 60)  # 🔁 refresh every 1 hour
