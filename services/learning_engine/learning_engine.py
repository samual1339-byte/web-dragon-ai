import json
import os

FILE = "data/user_learning.json"

def learn_from_user(ip, key, value):
    # Ensure file exists
    if not os.path.exists(FILE):
        data = {}
    else:
        try:
            with open(FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
        except:
            data = {}

    # 🔑 CRITICAL FIX: ensure dict, not list
    if isinstance(data, list):
        data = {}

    if ip not in data:
        data[ip] = {}

    data[ip][key] = value

    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
