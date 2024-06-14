import pytest

from src.rectangle import Rectangle


@pytest.mark.parametrize("type_scenario", ["positive"])
def test_area_rectangle_positive(rectangle_params, type_scenario):
    for side_a, side_b, expected_area, _ in rectangle_params(type_scenario):
        rect = Rectangle(side_a, side_b)
        assert rect.get_area == expected_area


@pytest.mark.parametrize("type_scenario", ["negative"])
def test_rectangle_negative(rectangle_params, type_scenario):
    for side_a, side_b in rectangle_params(type_scenario):
        with pytest.raises(ValueError):
            Rectangle(side_a, side_b)


@pytest.mark.parametrize("side_a, side_b, expected_perimeter", [
    (3, 5, 16),
    (7, 2, 18),
    (4.5, 3.5, 16),
    (10, 10, 40)
], ids=["3x5", "7x2", "4.5x3.5", "10x10"])
def test_rectangle_positive_perimeter(side_a, side_b, expected_perimeter):
    rect = Rectangle(side_a, side_b)
    assert rect.get_perimeter == expected_perimeter



