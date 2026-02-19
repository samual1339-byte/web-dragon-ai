import datetime
import random

def get_live_transit():
    today = datetime.date.today()

    messages = [
        "Current Saturn transit advises patience.",
        "Jupiter transit supports financial growth.",
        "Mars transit suggests energy and action.",
        "Venus transit improves relationships."
    ]

    return {
        "date": str(today),
        "message": random.choice(messages)
    }
