import json
from datetime import datetime
import os

# Absolute path to project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_DIR = os.path.join(BASE_DIR, "data")
LOG_FILE = os.path.join(DATA_DIR, "user_logs.json")


def log_user_action(ip=None, page=None, query=None, extra_data=None):
    """
    Generic user activity logger
    """

    # Ensure data directory exists
    os.makedirs(DATA_DIR, exist_ok=True)

    log = {
        "time": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
        "ip": ip,
        "page": page,
        "query": query,
        "extra_data": extra_data
    }

    try:
        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
        else:
            data = []
    except Exception:
        data = []

    data.append(log)

    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
