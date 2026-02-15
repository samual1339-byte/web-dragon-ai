import requests
from bs4 import BeautifulSoup
import json
import time
import os
from datetime import datetime

HEADERS = {"User-Agent": "Mozilla/5.0"}
DATA_FILE = "data/serp_data.json"
CACHE_TIME = 3600  # 1 hour


# ==========================================
# BASIC SERP FETCH
# ==========================================
def fetch_serp(query):
    try:
        url = f"https://duckduckgo.com/html/?q={query}"
        res = requests.get(url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(res.text, "html.parser")

        results = []
        for r in soup.select(".result__body")[:5]:
            title = r.select_one(".result__title")
            snippet = r.select_one(".result__snippet")

            results.append({
                "title": title.get_text(strip=True) if title else "",
                "snippet": snippet.get_text(strip=True) if snippet else ""
            })

        return results

    except Exception as e:
        return [{"title": "Error", "snippet": str(e)}]


# ==========================================
# AI STYLE SUMMARY GENERATOR
# ==========================================
def generate_summary(results):
    combined_text = " ".join([r["snippet"] for r in results if r["snippet"]])

    if not combined_text:
        return "No major planetary updates available."

    # Simple intelligent keyword scan
    if "retrograde" in combined_text.lower():
        return "Current planetary retrograde movements may cause delays but favor inner reflection."

    if "transit" in combined_text.lower():
        return "Major planetary transits indicate transformative life phases and career movement."

    if "eclipse" in combined_text.lower():
        return "Eclipse cycles suggest karmic shifts and unexpected developments."

    return "Planetary movements indicate gradual growth, stability, and opportunity."


# ==========================================
# ADVANCED ASTROLOGY INTELLIGENCE BUILDER
# ==========================================
def build_astrology_data():
    kundali_data = fetch_serp("vedic kundali planetary transits 2026")
    matchmaking_data = fetch_serp("guna milan astrology compatibility trends")
    daily_data = fetch_serp("today horoscope vedic astrology")
    weekly_data = fetch_serp("weekly horoscope vedic astrology")
    monthly_data = fetch_serp("monthly horoscope astrology")
    yearly_data = fetch_serp("yearly horoscope 2026 astrology")

    return {
        "kundali": {
            "results": kundali_data,
            "summary": generate_summary(kundali_data),
            "last_updated": str(datetime.now())
        },
        "matchmaking": {
            "results": matchmaking_data,
            "summary": generate_summary(matchmaking_data),
            "last_updated": str(datetime.now())
        },
        "daily": {
            "results": daily_data,
            "summary": generate_summary(daily_data),
            "last_updated": str(datetime.now())
        },
        "weekly": {
            "results": weekly_data,
            "summary": generate_summary(weekly_data),
            "last_updated": str(datetime.now())
        },
        "monthly": {
            "results": monthly_data,
            "summary": generate_summary(monthly_data),
            "last_updated": str(datetime.now())
        },
        "yearly": {
            "results": yearly_data,
            "summary": generate_summary(yearly_data),
            "last_updated": str(datetime.now())
        }
    }


# ==========================================
# COURSE INTELLIGENCE
# ==========================================
def build_courses_data():
    python = fetch_serp("python roadmap beginner to expert 2026")
    java = fetch_serp("java roadmap programming 2026")
    marketing = fetch_serp("digital marketing roadmap 2026")
    html = fetch_serp("html css learning roadmap")

    return {
        "python": {
            "results": python,
            "summary": generate_summary(python)
        },
        "java": {
            "results": java,
            "summary": generate_summary(java)
        },
        "digital_marketing": {
            "results": marketing,
            "summary": generate_summary(marketing)
        },
        "html_css": {
            "results": html,
            "summary": generate_summary(html)
        }
    }


# ==========================================
# MARKETING INTELLIGENCE
# ==========================================
def build_marketing_data():
    stock = fetch_serp("stock market trends india 2026")
    business = fetch_serp("business news india 2026")
    trends = fetch_serp("digital marketing trends 2026")

    return {
        "stock_trends": {
            "results": stock,
            "summary": generate_summary(stock)
        },
        "business_news": {
            "results": business,
            "summary": generate_summary(business)
        },
        "marketing_trends": {
            "results": trends,
            "summary": generate_summary(trends)
        }
    }


# ==========================================
# MAIN SERP UPDATE FUNCTION
# ==========================================
def update_serp_data(force=False):

    if os.path.exists(DATA_FILE) and not force:
        last_updated = os.path.getmtime(DATA_FILE)
        if time.time() - last_updated < CACHE_TIME:
            return  # Skip update safely

    data = {
        "astrology": build_astrology_data(),
        "courses": build_courses_data(),
        "marketing": build_marketing_data(),
        "system_last_updated": str(datetime.now())
    }

    os.makedirs("data", exist_ok=True)

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
