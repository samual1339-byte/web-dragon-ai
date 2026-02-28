# ============================================
# LAL KITAB – PLANETARY RULES DATABASE v2.0
# Structured for Autonomous Kundali Engine
# ============================================

PLANETARY_RULES_DB = {

    # ==========================================================
    # ☀️ SUN
    # ==========================================================
    "Sun": {
        "planet_meta": {
            "element": "Fire",
            "guna": "Satva",
            "category": "Soul Authority",
            "natural_risk_bias": "Medium"
        },
        "house_rules": { ... }  # ← keep your existing Sun house rules here
    },

    # ==========================================================
    # 🌙 MOON
    # ==========================================================
    "Moon": {
        "planet_meta": {
            "element": "Water",
            "guna": "Satva",
            "category": "Emotional Mind",
            "natural_risk_bias": "Medium"
        },
        "house_rules": { ... }  # ← keep your existing Moon house rules here
    },

    # ==========================================================
    # ♂️ MARS
    # ==========================================================
    "Mars": {
        "planet_meta": {
            "element": "Fire",
            "guna": "Tamas",
            "category": "Action & Conflict",
            "natural_risk_bias": "High"
        },
        "house_rules": {
            house: {
                "core_nature": "Action karma and aggression channel",
                "positive_effects": ["Courage", "Execution power", "Protection energy"],
                "negative_effects": ["Impulsiveness", "Conflict tendency"],
                "karmic_theme": "Energy direction test",
                "karma_axis": "Action",
                "activates_house": (house + 6 - 1) % 12 + 1,
                "debt_type": "Bhai Rin" if house in [3, 6] else None,
                "hidden_effect": "Energy misdirection creates conflict cycles",
                "risk_level": "High" if house in [4, 7, 8] else "Medium",
                "severity_weight": 3 if house in [4, 7, 8] else 2,
                "special_notes": []
            } for house in range(1, 13)
        }
    },

    # ==========================================================
    # ☿️ MERCURY
    # ==========================================================
    "Mercury": {
        "planet_meta": {
            "element": "Earth",
            "guna": "Rajas",
            "category": "Intellect & Speech",
            "natural_risk_bias": "Medium"
        },
        "house_rules": {
            house: {
                "core_nature": "Intellect and communication karma",
                "positive_effects": ["Sharp intelligence", "Business skill"],
                "negative_effects": ["Overthinking", "Manipulation tendency"],
                "karmic_theme": "Speech karma purification",
                "karma_axis": "Communication",
                "activates_house": (house % 12) + 1,
                "debt_type": "Kutumb Rin" if house == 2 else None,
                "hidden_effect": "Speech influences karmic outcomes",
                "risk_level": "Medium",
                "severity_weight": 2,
                "special_notes": []
            } for house in range(1, 13)
        }
    },

    # ==========================================================
    # ♃ JUPITER
    # ==========================================================
    "Jupiter": {
        "planet_meta": {
            "element": "Ether",
            "guna": "Satva",
            "category": "Wisdom & Dharma",
            "natural_risk_bias": "Low"
        },
        "house_rules": {
            house: {
                "core_nature": "Wisdom and dharma expansion",
                "positive_effects": ["Spiritual growth", "Guidance ability"],
                "negative_effects": ["Over-optimism", "Guru conflicts"],
                "karmic_theme": "Dharma accountability",
                "karma_axis": "Ethics",
                "activates_house": (house + 4 - 1) % 12 + 1,
                "debt_type": "Guru Rin" if house in [9, 5] else None,
                "hidden_effect": "Blessings tied to moral conduct",
                "risk_level": "Low" if house in [1, 5, 9] else "Medium",
                "severity_weight": 1 if house in [1, 5, 9] else 2,
                "special_notes": []
            } for house in range(1, 13)
        }
    },

    # ==========================================================
    # ♄ SATURN
    # ==========================================================
    "Saturn": {
        "planet_meta": {
            "element": "Air",
            "guna": "Tamas",
            "category": "Karmic Judge",
            "natural_risk_bias": "High"
        },
        "house_rules": {
            house: {
                "core_nature": "Delay and karmic accountability",
                "positive_effects": ["Discipline", "Long-term success"],
                "negative_effects": ["Delay", "Isolation", "Fear patterns"],
                "karmic_theme": "Justice karma",
                "karma_axis": "Accountability",
                "activates_house": (house + 2 - 1) % 12 + 1,
                "debt_type": "Shani Rin" if house in [8, 10] else None,
                "hidden_effect": "Delays reveal past-life imbalance",
                "risk_level": "High" if house in [1, 8] else "Medium",
                "severity_weight": 3 if house in [1, 8] else 2,
                "special_notes": []
            } for house in range(1, 13)
        }
    },

    # ==========================================================
    # ☊ RAHU
    # ==========================================================
    "Rahu": {
        "planet_meta": {
            "element": "Air",
            "guna": "Tamas",
            "category": "Illusion Amplifier",
            "natural_risk_bias": "High"
        },
        "house_rules": {
            house: {
                "core_nature": "Obsession and illusion karma",
                "positive_effects": ["Innovation", "Foreign success"],
                "negative_effects": ["Addiction tendency", "Confusion cycles"],
                "karmic_theme": "Desire distortion",
                "karma_axis": "Obsession",
                "activates_house": (house + 5 - 1) % 12 + 1,
                "debt_type": "Pitru Rin" if house == 9 else None,
                "hidden_effect": "Sudden rise and fall pattern",
                "risk_level": "High" if house in [1, 7, 8] else "Medium",
                "severity_weight": 3 if house in [1, 7, 8] else 2,
                "special_notes": []
            } for house in range(1, 13)
        }
    },

    # ==========================================================
    # ☋ KETU
    # ==========================================================
    "Ketu": {
        "planet_meta": {
            "element": "Fire",
            "guna": "Satva",
            "category": "Detachment Engine",
            "natural_risk_bias": "Medium"
        },
        "house_rules": {
            house: {
                "core_nature": "Detachment and moksha karma",
                "positive_effects": ["Spiritual insight", "Detachment wisdom"],
                "negative_effects": ["Isolation", "Loss feeling"],
                "karmic_theme": "Past life residue clearing",
                "karma_axis": "Liberation",
                "activates_house": (house + 11 - 1) % 12 + 1,
                "debt_type": "Pitru Rin" if house == 1 else None,
                "hidden_effect": "Sudden separation teaches detachment",
                "risk_level": "High" if house in [4, 8, 12] else "Medium",
                "severity_weight": 3 if house in [4, 8, 12] else 2,
                "special_notes": []
            } for house in range(1, 13)
        }
    }
}