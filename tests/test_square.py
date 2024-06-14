import pytest

from src.square import Square


@pytest.mark.parametrize("side_a, expected_area", [(3, 9),
                                                   (5, 25)], ids=["side 3", "side 5"])
def test_square_area_positive(side_a, expected_area):
    s = Square(side_a)
    assert s.get_area == expected_area


@pytest.mark.parametrize("side_a, expected_perimeter", [(3, 12),
                                                        (5, 20)], ids=["3x5", "7x2"])
def test_square_perimeter_positive(side_a, expected_perimeter):
    s = Square(side_a)
    assert s.get_perimeter == expected_perimeter


@pytest.mark.parametrize("side_a", [-1, 0, ], ids=["negative side -1", "negative side 0"])
def test_square_negative(side_a):
    with pytest.raises(ValueError):
        Square(side_a)
