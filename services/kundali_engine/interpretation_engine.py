def generate_interpretation(name, lagna, planets, yogas, doshas):

    text = f"{name}, with {lagna} ascendant, "

    if lagna in ["Leo", "Aries"]:
        text += "you are bold and leadership-driven. "
    elif lagna in ["Cancer", "Pisces"]:
        text += "you are emotional and intuitive. "
    else:
        text += "you are practical and analytical. "

    if yogas:
        text += f"You have powerful yogas like {', '.join(yogas)}. "

    if doshas:
        text += f"However, caution due to {', '.join(doshas)}. "

    return text
