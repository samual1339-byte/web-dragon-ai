from modes.marketing import marketing_agent
from modes.coding import coding_agent
from modes.astrology import astrology_agent

# Simple in-memory user state
user_mode = {}

def dragon_agent(user_input, user_id="default"):
    text = user_input.lower().strip()

    # SHOW MENU
    if text in ["menu", "start", "hi", "hello"]:
        return (
            "🐉 *Web Dragon AI*\n\n"
            "Choose a mode:\n"
            "1️⃣ Digital Marketing\n"
            "2️⃣ Coding\n"
            "3️⃣ Astrology\n\n"
            "Reply with *1, 2, or 3*"
        )

    # MODE SELECTION
    if text == "1":
        user_mode[user_id] = "marketing"
        return "✅ Digital Marketing mode activated."

    if text == "2":
        user_mode[user_id] = "coding"
        return "✅ Coding mode activated."

    if text == "3":
        user_mode[user_id] = "astrology"
        return "✅ Astrology mode activated."

    # HANDLE MODE
    mode = user_mode.get(user_id)

    if mode == "marketing":
        return marketing_agent(user_input)

    if mode == "coding":
        return coding_agent(user_input)

    if mode == "astrology":
        return astrology_agent(user_input)

    return "⚠️ Please type *menu* to choose a mode."
