import swisseph as swe

# Tell Swiss Ephemeris where ephemeris files are located
swe.set_ephe_path("services/kundali_engine/ephemeris")

# Julian Day calculation
jd = swe.julday(1990, 5, 15, 14.5)

# Calculate Sun position
sun = swe.calc_ut(jd, swe.SUN)

print("Sun longitude:", sun[0])