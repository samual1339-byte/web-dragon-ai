def detect_doshas(planets):
    doshas = []

    mars_house = planets["Mars"]["house"]

    if mars_house in [1, 4, 7, 8, 12]:
        doshas.append("Mangal Dosha")

    if planets["Rahu"]["house"] == planets["Ketu"]["house"]:
        doshas.append("Kaal Sarp Dosha")

    return doshas
