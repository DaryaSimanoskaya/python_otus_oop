import math

import pytest

from src.circle import Circle


@pytest.mark.parametrize("radius, expected_area",
                         [(1, math.pi * 1 ** 2),
                          (2, math.pi * 2 ** 2)], ids=["radius 1", "radius 2"])
def test_circle_area_positive(radius, expected_area):
    c = Circle(radius)
    assert c.get_area == expected_area


@pytest.mark.parametrize("radius, expected_perimeter", [(1, 2 * math.pi * 1),
                                                        (2, 2 * math.pi * 2)],
                         ids=["radius 1", "radius 2"])
def test_circle_perimeter_positive(radius, expected_perimeter):
    c = Circle(radius)
    assert c.get_perimeter == expected_perimeter


@pytest.mark.parametrize("radius", [-1, 0], ids=["negative value -1", "zero value 0"])
def test_circle_negative(radius):
    with pytest.raises(ValueError):
        Circle(radius)

