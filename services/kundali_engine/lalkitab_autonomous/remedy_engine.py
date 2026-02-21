def generate_remedies(dosha, debt_cycle=None):
    """
    Deterministic Lal Kitab Remedy Generator.
    Stable ordering.
    Severity-aware.
    Structured logic.
    """

    remedies = []
    added = set()

    # -------------------------------
    # DOSHA BASED REMEDIES
    # -------------------------------
    if isinstance(dosha, dict):

        if dosha.get("is_pitru_dosha"):
            remedies.append("Offer water to Sun daily and perform Pitru Tarpan.")
            remedies.append("Donate wheat and jaggery on Sundays.")
            added.update(remedies)

        # Generic dosha handling (future safe)
        for key, value in dosha.items():
            if isinstance(value, dict):
                if value.get("active") is True:
                    remedy_text = f"Perform remedy for {key} as per Lal Kitab guidance."
                    if remedy_text not in added:
                        remedies.append(remedy_text)
                        added.add(remedy_text)

    # -------------------------------
    # DEBT (RIN) BASED REMEDIES
    # -------------------------------
    if isinstance(debt_cycle, dict):

        rin_details = debt_cycle.get("rin_details", {})

        for rin in sorted(rin_details.keys()):

            if rin == "Pitru Rin":
                remedy = "Feed cows and donate wheat on Sundays."
            elif rin == "Mata Rin":
                remedy = "Serve mother regularly and donate milk or rice."
            elif rin == "Stri Rin":
                remedy = "Respect women and donate white sweets on Fridays."
            elif rin == "Guru Rin":
                remedy = "Donate yellow items and respect teachers."
            else:
                remedy = f"Follow Lal Kitab discipline to neutralize {rin}."

            if remedy not in added:
                remedies.append(remedy)
                added.add(remedy)

    # -------------------------------
    # FINAL ORDER LOCK
    # -------------------------------
    remedies = sorted(remedies)

    return remedies