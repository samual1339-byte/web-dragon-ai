from services.kundali_engine.engine import LalKitabEngine

birth_data = {
    "date": "1990-05-15",
    "time": "14:30"
}

engine = LalKitabEngine(birth_data)
result = engine.generate_kundali()

print(result)