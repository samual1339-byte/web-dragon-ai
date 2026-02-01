def astrology_agent(user_input):
    text = user_input.lower()

    # SHOW ASTROLOGY MENU
    if text in ["astrology", "menu", "start"]:
        return (
            "🔮 *Astrology Services*\n\n"
            "Choose a service:\n"
            "1️⃣ Lal Kitab Remedies\n"
            "2️⃣ Daily Horoscope\n"
            "3️⃣ Weekly Horoscope\n"
            "4️⃣ Monthly Horoscope\n"
            "5️⃣ Kundli Creation\n"
            "6️⃣ Kundli Matching\n\n"
            "Reply with *1–6*"
        )

    # LAL KITAB
    if text == "1":
        return (
            "🔮 *Lal Kitab Remedies*\n\n"
            "• Offer water to Sun daily\n"
            "• Feed cows on Monday\n"
            "• Keep silver square with you\n"
            "• Avoid lies and ego"
        )

    # DAILY
    if text == "2":
        return "🌞 *Daily Horoscope*\nToday favors discipline, patience, and honesty."

    # WEEKLY
    if text == "3":
        return "📅 *Weekly Horoscope*\nGood time for planning and health focus."

    # MONTHLY
    if text == "4":
        return "🗓️ *Monthly Horoscope*\nCareer improves after mid-month."

    # KUNDLI
    if text == "5":
        return (
            "📜 *Kundli Creation*\n\n"
            "Please provide:\n"
            "• Date of Birth\n"
            "• Time of Birth\n"
            "• Place of Birth"
        )

    # MATCHING
    if text == "6":
        return (
            "❤️ *Kundli Matching*\n\n"
            "Please provide both persons:\n"
            "• DOB\n"
            "• Time\n"
            "• Place"
        )

    return "⚠️ Please choose a valid astrology option (1–6)."
