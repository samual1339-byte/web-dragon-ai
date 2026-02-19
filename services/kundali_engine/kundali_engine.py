from ..user_logger.user_logger import log_user_action

# ======================================
# IMPORTS (FROM YOUR MODULE FILES)
# ======================================

# SAME FOLDER IMPORTS
from .astronomy_calculator import calculate_planetary_positions
from .planetary_strength import calculate_strength
from .lagna_calculator import calculate_lagna
from .yoga_engine import detect_yogas
from .dosha_engine import detect_doshas
from .interpretation_engine import generate_interpretation

# SIBLING FOLDER IMPORTS
from ..ai_engine.ai_interpreter import enhance_with_ai
from ..transit_engine.live_transit import get_live_transit


# ======================================
# MAIN KUNDALI GENERATOR
# ======================================

def generate_kundali(name, dob, tob, place):

    # 1️⃣ Planetary Positions
    planets = calculate_planetary_positions(name, dob, tob, place)

    # 2️⃣ Add Strength Calculation
    planets = calculate_strength(planets)

    # 3️⃣ Lagna
    lagna = calculate_lagna(name, dob, tob, place)

    # 4️⃣ Yogas & Doshas
    yogas = detect_yogas(planets)
    doshas = detect_doshas(planets)

    # 5️⃣ Interpretation
    interpretation = generate_interpretation(name, lagna, planets, yogas, doshas)

    # 6️⃣ AI Enhancement
    interpretation = enhance_with_ai(interpretation)

    # 7️⃣ Live Transit
    transit = get_live_transit()

    # 8️⃣ Final Result Structure
    result = {
        "planets": planets,
        "lagna": lagna,
        "yogas": yogas,
        "doshas": doshas,
        "interpretation": interpretation,
        "live_transit": transit,

        # Keep old keys (so frontend doesn’t break)
        "vedic": [
            "Sun represents soul and authority",
            "Moon represents mind and emotions"
        ],
        "lal_kitab": [
            "Offer water to Sun on Sunday",
            "Feed cow on Monday"
        ]
    }

    # ✅ LOGGER ADDED HERE
    log_user_action(
        ip="system",
        page="generate_kundali",
        extra_data={
            "name": name,
            "dob": dob,
            "tob": tob,
            "place": place,
            "lagna": lagna,
            "yogas": yogas,
            "doshas": doshas
        }
    )

    return result


# ======================================
# MATCHMAKING ENGINE (WITH LOGGING ADDED)
# ======================================

def matchmaking_kundali():

    boy_nakshatra = 5
    girl_nakshatra = 12

    varna = 1 if boy_nakshatra % 4 >= girl_nakshatra % 4 else 0
    vashya = 2 if boy_nakshatra % 2 == girl_nakshatra % 2 else 1

    tara_distance = abs(boy_nakshatra - girl_nakshatra)
    tara = 3 if tara_distance % 9 in [0, 3, 5, 7] else 1

    yoni = 4 if (boy_nakshatra - girl_nakshatra) % 2 == 0 else 2

    graha_maitri = 5

    gana = 6 if (boy_nakshatra - 1) % 3 == (girl_nakshatra - 1) % 3 else 3

    rashi_diff = abs((boy_nakshatra % 12) - (girl_nakshatra % 12))
    bhakoot = 0 if rashi_diff in [6, 8] else 7

    nadi = 0 if (boy_nakshatra - 1) % 3 == (girl_nakshatra - 1) % 3 else 8

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

    if total_score >= 28:
        verdict = "Excellent Match"
    elif total_score >= 18:
        verdict = "Average Compatibility"
    else:
        verdict = "Low Compatibility"

    result = {
        "guna_milan": f"{total_score}/36",
        "score": total_score,
        "verdict": verdict
    }

    # ✅ LOGGER ADDED HERE
    log_user_action(
        ip="system",
        page="guna_milan",
        extra_data={
            "boy_nakshatra": boy_nakshatra,
            "girl_nakshatra": girl_nakshatra,
            "score": total_score,
            "verdict": verdict
        }
    )

    return result
