import math
import datetime
import copy


# ==========================================================
# ASTRONOMY ENGINE (Deterministic planetary positions)
# ==========================================================

class AstronomyEngine:

    @staticmethod
    def julian_day(date_obj):
        y = date_obj.year
        m = date_obj.month
        d = date_obj.day

        if m <= 2:
            y -= 1
            m += 12

        A = int(y / 100)
        B = 2 - A + int(A / 4)

        jd = int(365.25 * (y + 4716)) \
             + int(30.6001 * (m + 1)) \
             + d + B - 1524.5

        return jd

    @staticmethod
    def simple_planet_degree(jd, base_speed):
        return (jd * base_speed) % 360

    @staticmethod
    def get_planet_positions(birth_data):

        date_obj = birth_data.get("date_object")
        jd = AstronomyEngine.julian_day(date_obj)

        # Simplified deterministic speeds
        speeds = {
            "Sun": 0.9856,
            "Moon": 13.1764,
            "Mars": 0.524,
            "Mercury": 1.607,
            "Jupiter": 0.083,
            "Venus": 1.174,
            "Saturn": 0.033,
            "Rahu": -0.052,
            "Ketu": -0.052
        }

        planets = {}

        for planet, speed in speeds.items():
            degree = AstronomyEngine.simple_planet_degree(jd, speed)
            planets[planet] = {
                "degree": round(degree, 4)
            }

        return planets


# ==========================================================
# HOUSE ENGINE
# ==========================================================

class HouseEngine:

    @staticmethod
    def map_to_houses(planets):

        house_map = {}

        for planet, data in planets.items():
            degree = data["degree"]
            house = int(degree // 30) + 1

            if house > 12:
                house = 12
            if house < 1:
                house = 1

            house_map[planet] = {
                "degree": degree,
                "house": house
            }

        return dict(sorted(house_map.items()))


# ==========================================================
# LAL KITAB RULES (STRUCTURED FROM YOUR PDF)
# ==========================================================

class LalKitabRules:

    HOUSE_IMPACT = {
        "Saturn": {
            1: {"effect": "Life struggles early", "remedy": "Donate mustard oil"},
            8: {"effect": "Heavy karmic debt", "remedy": "Serve elders"}
        },
        "Mars": {
            4: {"effect": "Property conflict", "remedy": "Keep red cloth"}
        }
    }

    DOSHA_RULES = {
        "Pitru Dosha": {
            "condition": lambda hm: hm.get("Sun", {}).get("house") == 9
        }
    }

    YOGA_RULES = {
        "Raj Yoga": lambda hm: hm.get("Jupiter", {}).get("house") == 10
    }


# ==========================================================
# LAGNA ENGINE
# ==========================================================

class LagnaEngine:

    @staticmethod
    def calculate_lagna(house_map):
        for planet, data in house_map.items():
            if data["house"] == 1:
                return planet
        return None


# ==========================================================
# DOSHA ENGINE
# ==========================================================

class DoshaEngine:

    @staticmethod
    def detect_dosha(house_map):

        doshas = []

        for name, rule in LalKitabRules.DOSHA_RULES.items():
            if rule["condition"](house_map):
                doshas.append(name)

        return doshas


# ==========================================================
# YOGA ENGINE
# ==========================================================

class YogaEngine:

    @staticmethod
    def detect_yoga(house_map):

        yogas = []

        for name, rule in LalKitabRules.YOGA_RULES.items():
            if rule(house_map):
                yogas.append(name)

        return yogas


# ==========================================================
# IMPACT ENGINE
# ==========================================================

class ImpactEngine:

    @staticmethod
    def analyze_impact(house_map):

        impact = {}

        for planet, data in house_map.items():
            house = data["house"]

            rule = LalKitabRules.HOUSE_IMPACT.get(planet, {}).get(house)

            if rule:
                impact[planet] = {
                    "house": house,
                    "effect": rule["effect"],
                    "remedy": rule["remedy"]
                }

        return impact


# ==========================================================
# REMEDY ENGINE
# ==========================================================

class RemedyEngine:

    @staticmethod
    def generate_remedies(impact):

        remedies = []

        for planet, data in impact.items():
            remedies.append({
                "planet": planet,
                "remedy": data.get("remedy")
            })

        return remedies


# ==========================================================
# MASTER ENGINE
# ==========================================================

class LalKitabEngine:

    def __init__(self, birth_data):
        self.birth_data = birth_data

    def generate_kundali(self):

        # 1️⃣ Astronomy
        planets = AstronomyEngine.get_planet_positions(self.birth_data)

        # 2️⃣ Houses
        house_map = HouseEngine.map_to_houses(planets)

        # 3️⃣ Lagna
        lagna = LagnaEngine.calculate_lagna(house_map)

        # 4️⃣ Dosha
        doshas = DoshaEngine.detect_dosha(house_map)

        # 5️⃣ Yoga
        yogas = YogaEngine.detect_yoga(house_map)

        # 6️⃣ Impact
        impact = ImpactEngine.analyze_impact(house_map)

        # 7️⃣ Remedies
        remedies = RemedyEngine.generate_remedies(impact)

        return {
            "birth_data": self.birth_data,
            "planets": house_map,
            "lagna": lagna,
            "doshas": doshas,
            "yogas": yogas,
            "impact_analysis": impact,
            "remedies": remedies
        }