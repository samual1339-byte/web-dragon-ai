"""
test_engine.py

Local Functional Test Runner
Structured validation for LalKitabEngine
Run BEFORE Git push.
"""

import json
import traceback

from services.kundali_engine.engine import LalKitabEngine


# ======================================================
# TEST DATA
# ======================================================

birth_data = {
    "name": "Test User",
    "date": "1990-05-15",
    "time": "14:30",
    "place": "Delhi"
}


# ======================================================
# STRUCTURED VALIDATOR
# ======================================================

def validate_output_structure(result: dict):

    print("\n🔍 Validating Structure...\n")

    required_top_keys = [
        "meta",
        "birth_details",
        "birth_chart",
        "current_transit",
        "interpretation_layers",
        "remedies",
        "final_destiny_score"
    ]

    for key in required_top_keys:
        if key not in result:
            print(f"❌ Missing top-level key: {key}")
        else:
            print(f"✅ Found key: {key}")

    # Check Birth Chart Layer
    birth_chart = result.get("birth_chart", {})
    if birth_chart.get("planetary_positions", {}).get("by_planet"):
        print("✅ Birth planetary data exists")
    else:
        print("❌ Birth planetary data missing")

    # Check Interpretation Layer
    interpretation = result.get("interpretation_layers", {})
    birth_layer = interpretation.get("birth_chart", {})

    if birth_layer.get("personality_summary"):
        print("✅ Personality summary generated")
    else:
        print("❌ Personality summary missing")

    # Check AI Layer
    ai_layer = interpretation.get("ai_analysis", {})
    if isinstance(ai_layer, dict):
        print("✅ AI layer exists")
    else:
        print("❌ AI layer missing")

    print("\nValidation Complete.\n")


# ======================================================
# MAIN TEST EXECUTION
# ======================================================

def run_test():

    try:
        print("\n🚀 Running LalKitabEngine Test...\n")

        engine = LalKitabEngine(birth_data)
        result = engine.generate_kundali()

        print("\n========== STRUCTURED OUTPUT ==========\n")
        print(json.dumps(result, indent=4))

        validate_output_structure(result)

        print("\n🎯 Final Destiny Score:",
              result.get("final_destiny_score"))

        print("\n✅ Test Completed Successfully\n")

    except Exception as e:
        print("\n❌ ENGINE CRASHED\n")
        traceback.print_exc()


# ======================================================
# ENTRY POINT
# ======================================================

if __name__ == "__main__":
    run_test()