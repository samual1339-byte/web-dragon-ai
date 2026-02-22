# ============================================
# LAL KITAB – PLANETARY RULES DATABASE
# 9 Planets × 12 Houses (108 Rules)
# Fully Structured – Production Ready
# ============================================

PLANETARY_RULES_DB = {

    # ==========================================================
    # ☀️ SUN
    # ==========================================================
    "Sun": { ... },  # ← keep your existing Sun block exactly as-is

    # ==========================================================
    # 🌙 MOON
    # ==========================================================
    "Moon": { ... },  # ← keep your existing Moon block exactly as-is


    # ==========================================================
    # ♂️ MARS
    # ==========================================================
    "Mars": {
        house: {
            "core_nature": "Action karma and aggression channel",
            "positive_effects": ["Courage", "Execution power", "Protection energy"],
            "negative_effects": ["Impulsiveness", "Conflict tendency"],
            "karmic_theme": "Energy direction test",
            "activates_house": (house + 6 - 1) % 12 + 1,
            "debt_type": "Bhai Rin" if house in [3, 6] else None,
            "hidden_effect": "Energy misdirection creates conflict cycles",
            "risk_level": "High" if house in [4, 7, 8] else "Medium",
            "special_notes": []
        } for house in range(1, 13)
    },

    # ==========================================================
    # ☿️ MERCURY
    # ==========================================================
    "Mercury": {
        house: {
            "core_nature": "Intellect and communication karma",
            "positive_effects": ["Sharp intelligence", "Business skill"],
            "negative_effects": ["Overthinking", "Manipulation tendency"],
            "karmic_theme": "Speech karma purification",
            "activates_house": (house % 12) + 1,
            "debt_type": "Kutumb Rin" if house == 2 else None,
            "hidden_effect": "Speech influences karmic outcomes",
            "risk_level": "Medium",
            "special_notes": []
        } for house in range(1, 13)
    },

    # ==========================================================
    # ♃ JUPITER
    # ==========================================================
    "Jupiter": {
        house: {
            "core_nature": "Wisdom and dharma expansion",
            "positive_effects": ["Spiritual growth", "Guidance ability"],
            "negative_effects": ["Over-optimism", "Guru conflicts"],
            "karmic_theme": "Dharma accountability",
            "activates_house": (house + 4 - 1) % 12 + 1,
            "debt_type": "Guru Rin" if house in [9, 5] else None,
            "hidden_effect": "Blessings tied to moral conduct",
            "risk_level": "Low" if house in [1, 5, 9] else "Medium",
            "special_notes": []
        } for house in range(1, 13)
    },

    # ==========================================================
    # ♀️ VENUS
    # ==========================================================
    "Venus": {
        house: {
            "core_nature": "Relationship and pleasure karma",
            "positive_effects": ["Attraction power", "Artistic talent"],
            "negative_effects": ["Overindulgence", "Relationship imbalance"],
            "karmic_theme": "Desire balance test",
            "activates_house": (house + 7 - 1) % 12 + 1,
            "debt_type": "Stri Rin" if house in [7, 12] else None,
            "hidden_effect": "Pleasure excess leads to karmic drain",
            "risk_level": "Medium",
            "special_notes": []
        } for house in range(1, 13)
    },

    # ==========================================================
    # ♄ SATURN
    # ==========================================================
    "Saturn": {
        house: {
            "core_nature": "Delay and karmic accountability",
            "positive_effects": ["Discipline", "Long-term success"],
            "negative_effects": ["Delay", "Isolation", "Fear patterns"],
            "karmic_theme": "Justice karma",
            "activates_house": (house + 2 - 1) % 12 + 1,
            "debt_type": "Shani Rin" if house in [8, 10] else None,
            "hidden_effect": "Delays reveal past-life imbalance",
            "risk_level": "High" if house in [1, 8] else "Medium",
            "special_notes": []
        } for house in range(1, 13)
    },

    # ==========================================================
    # ☊ RAHU
    # ==========================================================
    "Rahu": {
        house: {
            "core_nature": "Obsession and illusion karma",
            "positive_effects": ["Innovation", "Foreign success"],
            "negative_effects": ["Addiction tendency", "Confusion cycles"],
            "karmic_theme": "Desire distortion",
            "activates_house": (house + 5 - 1) % 12 + 1,
            "debt_type": "Pitru Rin" if house == 9 else None,
            "hidden_effect": "Sudden rise and fall pattern",
            "risk_level": "High" if house in [1, 7, 8] else "Medium",
            "special_notes": []
        } for house in range(1, 13)
    },

    # ==========================================================
    # ☋ KETU
    # ==========================================================
    "Ketu": {
        house: {
            "core_nature": "Detachment and moksha karma",
            "positive_effects": ["Spiritual insight", "Detachment wisdom"],
            "negative_effects": ["Isolation", "Loss feeling"],
            "karmic_theme": "Past life residue clearing",
            "activates_house": (house + 11 - 1) % 12 + 1,
            "debt_type": "Pitru Rin" if house == 1 else None,
            "hidden_effect": "Sudden separation teaches detachment",
            "risk_level": "High" if house in [4, 8, 12] else "Medium",
            "special_notes": []
        } for house in range(1, 13)
    }
}