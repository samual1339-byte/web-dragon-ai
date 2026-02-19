def detect_yogas(planets):
    yogas = []

    # Surya-Mangal Yoga
    if planets["Sun"]["house"] == planets["Mars"]["house"]:
        yogas.append("Surya-Mangal Yoga")

    # Gaja Kesari Yoga
    if planets["Jupiter"]["house"] in [1, 4, 7, 10] and planets["Moon"]["house"] in [1, 4, 7, 10]:
        yogas.append("Gaja Kesari Yoga")

    return yogas
