# --------------------------------------------------
# FULL 36-POINT ASHTAKOOTA GUNA MATCHING DATABASE
# ENGINE READY – EXPANDED VERSION
# --------------------------------------------------

GUNA_MATCHING_DB = {

    # --------------------------------------------------
    # 1. VARNA (1 Point)
    # --------------------------------------------------
    "varna": {
        "points": 1,
        "hierarchy": ["Shudra", "Vaishya", "Kshatriya", "Brahmin"],
        "rule": "Boy varna should be equal or higher than girl varna"
    },

    # --------------------------------------------------
    # 2. VASHYA (2 Points)
    # --------------------------------------------------
    "vashya": {
        "points": 2,
        "categories": {
            "Chatushpada": ["Aries", "Taurus", "Capricorn"],
            "Dwipada": ["Gemini", "Virgo", "Libra", "Aquarius"],
            "Jalachara": ["Cancer", "Pisces"],
            "Vanachara": ["Leo"],
            "Keeta": ["Scorpio"]
        },
        "rule": "Same category full points"
    },

    # --------------------------------------------------
    # 3. TARA (3 Points)
    # --------------------------------------------------
    "tara": {
        "points": 3,
        "nakshatra_total": 27,
        "favorable_mod": [0, 3, 5, 7],
        "calculation_method": "Distance between nakshatras % 9"
    },

    # --------------------------------------------------
    # 4. YONI (4 Points)
    # --------------------------------------------------
    "yoni": {
        "points": 4,
        "nakshatra_to_yoni": {
            "Ashwini": "Horse",
            "Bharani": "Elephant",
            "Krittika": "Sheep",
            "Rohini": "Serpent",
            "Mrigashira": "Serpent",
            "Ardra": "Dog",
            "Punarvasu": "Cat",
            "Pushya": "Sheep",
            "Ashlesha": "Cat",
            "Magha": "Rat",
            "Purva Phalguni": "Rat",
            "Uttara Phalguni": "Cow",
            "Hasta": "Buffalo",
            "Chitra": "Tiger",
            "Swati": "Buffalo",
            "Vishakha": "Tiger",
            "Anuradha": "Deer",
            "Jyeshtha": "Deer",
            "Mula": "Dog",
            "Purva Ashadha": "Monkey",
            "Uttara Ashadha": "Mongoose",
            "Shravana": "Monkey",
            "Dhanishta": "Lion",
            "Shatabhisha": "Horse",
            "Purva Bhadrapada": "Lion",
            "Uttara Bhadrapada": "Cow",
            "Revati": "Elephant"
        }
    },

    # --------------------------------------------------
    # 5. GRAHA MAITRI (5 Points)
    # --------------------------------------------------
    "graha_maitri": {
        "points": 5,
        "planetary_friendship": {
            "Sun": ["Moon", "Mars", "Jupiter"],
            "Moon": ["Sun", "Mercury"],
            "Mars": ["Sun", "Moon", "Jupiter"],
            "Mercury": ["Sun", "Venus"],
            "Jupiter": ["Sun", "Moon", "Mars"],
            "Venus": ["Mercury", "Saturn"],
            "Saturn": ["Mercury", "Venus"]
        },
        "neutral_partial_points": 3
    },

    # --------------------------------------------------
    # 6. GANA (6 Points)
    # --------------------------------------------------
    "gana": {
        "points": 6,
        "nakshatra_to_gana": {
            "Ashwini": "Deva",
            "Bharani": "Manushya",
            "Krittika": "Rakshasa",
            "Rohini": "Manushya",
            "Mrigashira": "Deva",
            "Ardra": "Manushya",
            "Punarvasu": "Deva",
            "Pushya": "Deva",
            "Ashlesha": "Rakshasa",
            "Magha": "Rakshasa",
            "Purva Phalguni": "Manushya",
            "Uttara Phalguni": "Manushya",
            "Hasta": "Deva",
            "Chitra": "Rakshasa",
            "Swati": "Deva",
            "Vishakha": "Rakshasa",
            "Anuradha": "Deva",
            "Jyeshtha": "Rakshasa",
            "Mula": "Rakshasa",
            "Purva Ashadha": "Manushya",
            "Uttara Ashadha": "Manushya",
            "Shravana": "Deva",
            "Dhanishta": "Rakshasa",
            "Shatabhisha": "Rakshasa",
            "Purva Bhadrapada": "Manushya",
            "Uttara Bhadrapada": "Manushya",
            "Revati": "Deva"
        },
        "partial_compatibility": [
            ("Deva", "Manushya"),
            ("Manushya", "Deva")
        ],
        "partial_points": 3
    },

    # --------------------------------------------------
    # 7. BHAKOOT (7 Points)
    # --------------------------------------------------
    "bhakoot": {
        "points": 7,
        "dosha_distances": [2, 6, 8, 12],
        "rule": "Distance between Moon signs should not fall in dosha list"
    },

    # --------------------------------------------------
    # 8. NADI (8 Points)
    # --------------------------------------------------
    "nadi": {
        "points": 8,
        "nakshatra_to_nadi": {
            "Ashwini": "Adi",
            "Bharani": "Madhya",
            "Krittika": "Antya",
            "Rohini": "Antya",
            "Mrigashira": "Madhya",
            "Ardra": "Adi",
            "Punarvasu": "Adi",
            "Pushya": "Madhya",
            "Ashlesha": "Antya",
            "Magha": "Antya",
            "Purva Phalguni": "Madhya",
            "Uttara Phalguni": "Adi",
            "Hasta": "Adi",
            "Chitra": "Madhya",
            "Swati": "Antya",
            "Vishakha": "Antya",
            "Anuradha": "Madhya",
            "Jyeshtha": "Adi",
            "Mula": "Adi",
            "Purva Ashadha": "Madhya",
            "Uttara Ashadha": "Antya",
            "Shravana": "Antya",
            "Dhanishta": "Madhya",
            "Shatabhisha": "Adi",
            "Purva Bhadrapada": "Adi",
            "Uttara Bhadrapada": "Madhya",
            "Revati": "Antya"
        }
    }
}