from enum import StrEnum


class AqiCategory(StrEnum):
    GOOD = "Good"
    MODERATE = "Moderate"
    UNHEALTHY_SENSITIVE = "Unhealthy for Sensitive Groups"
    UNHEALTHY = "Unhealthy"
    VERY_UNHEALTHY = "Very Unhealthy"
    HAZARDOUS = "Hazardous"


_BREAKPOINTS: list[tuple[int, AqiCategory]] = [
    (50, AqiCategory.GOOD),
    (100, AqiCategory.MODERATE),
    (150, AqiCategory.UNHEALTHY_SENSITIVE),
    (200, AqiCategory.UNHEALTHY),
    (300, AqiCategory.VERY_UNHEALTHY),
]


def classify_aqi(aqi: int) -> AqiCategory:
    """
    Classifies the given AQI value into its corresponding category.

    Args:
        aqi (int): The Air Quality Index value to classify.

    Raises:
        ValueError: If the AQI value is negative.

    Returns:
        AqiCategory: The category corresponding to the given AQI value.
    """
    if aqi < 0:
        raise ValueError("AQI value cannot be negative.")
    for breakpoint, category in _BREAKPOINTS:
        if aqi <= breakpoint:
            return category
    return AqiCategory.HAZARDOUS
