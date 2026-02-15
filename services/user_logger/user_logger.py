import json
from datetime import datetime
import os

LOG_FILE = "data/user_logs.json"

def log_user_action(ip, page, query=None):
    # Ensure data folder exists
    os.makedirs("data", exist_ok=True)

    log = {
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "ip": ip,
        "page": page,
        "query": query
    }

    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    except:
        data = []

    data.append(log)

    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
