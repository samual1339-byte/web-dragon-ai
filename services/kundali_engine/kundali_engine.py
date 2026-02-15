def generate_kundali(name, dob, tob, place):
    return {
        "vedic": [
            "Sun represents soul and authority",
            "Moon represents mind and emotions",
            "Strong Jupiter indicates wisdom and prosperity"
        ],
        "lal_kitab": [
            "Offer water to Sun on Sunday",
            "Feed cow on Monday",
            "Avoid lies and anger"
        ]
    }

def matchmaking_kundali():
    return {
        "guna_milan": "18/36",
        "score": 18,
        "verdict": "Average compatibility"
    }

def matchmaking_kundali():

    # Temporary sample Nakshatra values
    # (Later you can dynamically pass real ones)
    boy_nakshatra = 5
    girl_nakshatra = 12

    # --------------------------
    # ASHTA KOOTA LOGIC
    # --------------------------

    # 1️⃣ VARNA (1 point)
    varna = 1 if boy_nakshatra % 4 >= girl_nakshatra % 4 else 0

    # 2️⃣ VASHYA (2 points)
    vashya = 2 if boy_nakshatra % 2 == girl_nakshatra % 2 else 1

    # 3️⃣ TARA (3 points)
    tara_distance = abs(boy_nakshatra - girl_nakshatra)
    tara = 3 if tara_distance % 9 in [0, 3, 5, 7] else 1

    # 4️⃣ YONI (4 points)
    yoni = 4 if (boy_nakshatra - girl_nakshatra) % 2 == 0 else 2

    # 5️⃣ GRAHA MAITRI (5 points)
    graha_maitri = 5  # simplified but realistic base scoring

    # 6️⃣ GANA (6 points)
    gana = 6 if (boy_nakshatra - 1) % 3 == (girl_nakshatra - 1) % 3 else 3

    # 7️⃣ BHAKOOT (7 points)
    rashi_diff = abs((boy_nakshatra % 12) - (girl_nakshatra % 12))
    bhakoot = 0 if rashi_diff in [6, 8] else 7

    # 8️⃣ NADI (8 points)
    nadi = 0 if (boy_nakshatra - 1) % 3 == (girl_nakshatra - 1) % 3 else 8

    # --------------------------
    # TOTAL SCORE
    # --------------------------
    total_score = (
        varna +
        vashya +
        tara +
        yoni +
        graha_maitri +
        gana +
        bhakoot +
        nadi
    )

    # --------------------------
    # VERDICT
    # --------------------------
    if total_score >= 28:
        verdict = "Excellent Match"
    elif total_score >= 18:
        verdict = "Average Compatibility"
    else:
        verdict = "Low Compatibility"

    # --------------------------
    # RETURN (UNCHANGED STRUCTURE)
    # --------------------------
    return {
        "guna_milan": f"{total_score}/36",
        "score": total_score,
        "verdict": verdict
    }

