import json
import os

DATA_FILE = "data/serp_data.json"

def get_astrology_data():
    if not os.path.exists(DATA_FILE):
        return {}

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    return data.get("astrology", {})
