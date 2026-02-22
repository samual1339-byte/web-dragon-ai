"""
Deep Interpretation Engine
Fully Expanded Narrative Generator
Designed for Birth Chart & Current Transit Interpretation
Author: Web Dragon System
"""

from datetime import datetime


def generate_deep_interpretation(planetary_data, mode="birth"):

    if not planetary_data or not isinstance(planetary_data, dict):
        return (
            "The planetary data required for interpretation is currently unavailable. "
            "This may indicate missing calculation input or incomplete planetary mapping. "
            "Please ensure birth details and planetary computation modules are functioning correctly."
        )

    interpretation = ""

    # =========================
    # INTRODUCTION SECTION
    # =========================

    if mode == "birth":
        interpretation += (
            "This interpretation represents the karmic blueprint active at the exact "
            "moment of birth. The planetary positions form a permanent energetic matrix "
            "that shapes personality, life direction, psychological tendencies, "
            "relationships, career orientation, emotional responses, and spiritual evolution. "
            "These placements do not randomly influence life — they describe the inner design "
            "with which the soul has chosen to experience this incarnation.\n\n"
        )
    else:
        interpretation += (
            "This interpretation reflects the current planetary transits influencing "
            "your life at this moment. Unlike the birth chart which remains fixed, "
            "transits are dynamic and represent temporary waves of cosmic activation. "
            "They influence decisions, emotional climate, external events, "
            "mental focus, financial movement, and relational shifts. "
            "Understanding these influences allows conscious navigation.\n\n"
        )

    # =========================
    # PLANETARY NARRATIVE LOOP
    # =========================

    for planet, details in planetary_data.items():

        house = details.get("house", "an unknown")
        core_nature = details.get("core_nature", "")
        positive_effects = details.get("positive_effects", [])
        negative_effects = details.get("negative_effects", [])
        remedy = details.get("suggested_remedy", "")
        strength = details.get("strength_score", None)

        paragraph = f"When {planet} occupies the {house} house, "

        if mode == "birth":
            paragraph += (
                "this placement becomes a foundational karmic imprint influencing "
                "long-term life themes. "
            )
        else:
            paragraph += (
                "this transit activates specific life domains during the current period. "
            )

        # Core Nature
        if core_nature:
            paragraph += (
                f"The intrinsic energy of this placement expresses as {core_nature}. "
            )

        # Positive Effects
        if positive_effects:
            paragraph += (
                "When functioning harmoniously, it may manifest through "
                + ", ".join(positive_effects)
                + ". "
            )

        # Negative Effects
        if negative_effects:
            paragraph += (
                "However, if afflicted, weak, or misaligned, challenges may arise in the form of "
                + ", ".join(negative_effects)
                + ". "
            )

        # Strength Interpretation
        if strength is not None:
            if strength >= 75:
                paragraph += (
                    "This planet is considered strongly placed, amplifying its constructive potential. "
                )
            elif strength >= 40:
                paragraph += (
                    "This planet holds moderate strength, requiring conscious effort for optimal expression. "
                )
            else:
                paragraph += (
                    "This planet appears weak or afflicted, suggesting karmic lessons in this area of life. "
                )

        # Remedy
        if remedy:
            paragraph += (
                f"To harmonize this planetary influence, it is advisable to {remedy}. "
                "Remedies symbolically recalibrate internal alignment with cosmic principles. "
            )

        paragraph += (
            "Spiritually, this placement encourages self-awareness, responsibility, "
            "and disciplined alignment with higher values.\n\n"
        )

        interpretation += paragraph

    # =========================
    # CONCLUSION SECTION
    # =========================

    if mode == "birth":
        interpretation += (
            "In summary, the birth chart represents a fixed karmic structure designed "
            "for evolutionary growth. Strengths indicate natural gifts, while challenges "
            "indicate areas for conscious refinement. Astrology does not impose destiny — "
            "it reveals patterns. Through awareness, discipline, and corrective measures, "
            "one can elevate the expression of planetary forces toward constructive life outcomes."
        )
    else:
        interpretation += (
            "In summary, current planetary transits are temporary energetic waves. "
            "Favorable periods should be utilized for expansion and growth, while "
            "challenging periods require patience, introspection, and strategic action. "
            "Awareness of transits allows transformation of difficulty into maturity."
        )

    return interpretation.strip()