from src.circle import Circle
from src.figure import Figure


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        if side_a <= 0 or side_b <= 0 or side_c < 0:
            raise ValueError("Sides can't be less than or equal to 0")
        if not (side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a):
            raise ValueError("These sides do not form a triangle")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    @property
    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c

    @property
    def get_area(self):
        s = self.get_perimeter / 2
        return (s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c)) ** 0.5
