import pytest

from src.triangle import Triangle


@pytest.mark.parametrize("side_a, side_b, side_c, expected_area", [(6, 8, 10, 24), (3, 4, 5, 6)],
                         ids=["rectangular", "rectangular"])
def test_triangle_area_positive(side_a, side_b, side_c, expected_area):
    t = Triangle(side_a, side_b, side_c)
    assert t.get_area == expected_area


@pytest.mark.parametrize("side_a, side_b, side_c, expected_perimeter", [(3, 4, 5, 12),
                                                                        (5, 5, 5, 15)],
                         ids=["rectangular", "equilateral"])
def test_triangle_perimeter_positive(side_a, side_b, side_c, expected_perimeter):
    t = Triangle(side_a, side_b, side_c)
    assert t.get_perimeter == expected_perimeter


@pytest.mark.parametrize("side_a, side_b, side_c", [(3, -5, 5),
                                                    (0, 4, 5)],
                         ids=["negative value 3", "zero value 0"])
def test_triangle_negative_sides(side_a, side_b, side_c):
    with pytest.raises(ValueError):
        Triangle(side_a, side_b, side_c)


@pytest.mark.parametrize("side_a, side_b, side_c", [(1, 2, 3),
                                                    (1, 10, 12)],
                         ids=["not a triangle 1-2-3", "not a triangle 1-10-12"])
def test_sides_cant_make_triangle(side_a, side_b, side_c):
    with pytest.raises(ValueError):
        Triangle(side_a, side_b, side_c)
