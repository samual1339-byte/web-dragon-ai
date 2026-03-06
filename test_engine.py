from services.kundali_engine.astronomy_calculator import calculate_planetary_positions

birth_data = {
    "date": "1990-05-15",
    "time": "14:30",
    "place": "Delhi"
}

result = calculate_planetary_positions(birth_data)

print("\nASCENDANT")
print(result["ascendant_rashi"])

print("\nPLANETS")
for p, data in result["by_planet"].items():
    print(p, data)

print("\nHOUSES")
print(result["by_house"])