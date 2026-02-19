def generate_remedies(dosha, debt_cycle=None):

    remedies = []

    # Existing Dosha remedies
    for key in dosha:
        remedies.append(f"Remedy for {key}")

    # Rin based remedies
    if debt_cycle:
        for rin in debt_cycle.get("rin_details", {}):
            if rin == "Pitru Rin":
                remedies.append("Feed cows and donate wheat on Sundays.")
            elif rin == "Mata Rin":
                remedies.append("Serve mother and donate milk.")
            elif rin == "Stri Rin":
                remedies.append("Respect women and donate white sweets.")

    return list(set(remedies))