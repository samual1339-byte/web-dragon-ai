from .kundali_engine import generate_kundali, matchmaking_kundali

# -------------------------
# TEST KUNDALI GENERATION
# -------------------------

kundali = generate_kundali(
    name="Rahul",
    dob="1995-08-15",
    tob="10:30",
    place="Delhi"
)

print("=== KUNDALI RESULT ===")
print(kundali)


# -------------------------
# TEST MATCHMAKING
# -------------------------

match = matchmaking_kundali()

print("\n=== MATCHMAKING RESULT ===")
print(match)
