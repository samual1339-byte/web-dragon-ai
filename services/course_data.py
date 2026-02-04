import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(BASE_DIR, "data", "serp_data.json")

def get_courses_data():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
        return data.get("courses", [])
