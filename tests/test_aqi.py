import pytest

from airecivico.aqi import AqiCategory, classify_aqi


@pytest.mark.parametrize(
    ("values,expected"),
    [
        (0, AqiCategory.GOOD),
        (50, AqiCategory.GOOD),
        (100, AqiCategory.MODERATE),
        (150, AqiCategory.UNHEALTHY_SENSITIVE),
        (200, AqiCategory.UNHEALTHY),
        (300, AqiCategory.VERY_UNHEALTHY),
        (400, AqiCategory.HAZARDOUS),
    ],
)
def test_classify_aqi(values, expected) -> None:
    assert classify_aqi(values) == expected


def test_classify_aqi_negative() -> None:
    with pytest.raises(ValueError):
        classify_aqi(-1)
