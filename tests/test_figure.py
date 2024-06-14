import math

import pytest

from src.rectangle import Rectangle
from src.square import Square
from src.circle import Circle
from src.triangle import Triangle


@pytest.mark.parametrize("figure1, figure2, area", [
    (Rectangle(3, 4), Square(2), 16),
    (Circle(1), Square(1), math.pi + 1),
    (Rectangle(2, 5), Triangle(3, 4, 5), 16)],
                         ids=["rectangle+square", "circle+square", "rectangle+triangle"])
def test_add_area_positive(figure1, figure2, area):
    assert figure1.add_area(figure2) == area


@pytest.mark.parametrize("figure1, figure2",
                         [(Rectangle(3, 4), "not_a_figure"),
                          (Square(2), 123),
                          (Circle(1), None)],
                         ids=["rectangle+string", "square+int", "circle+None"])
def test_add_area_negative(figure1, figure2):
    with pytest.raises(ValueError):
        figure1.add_area(figure2)
