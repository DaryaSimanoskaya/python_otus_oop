import pytest


@pytest.fixture
def rectangle_params():
    def _wrapper(type_scenario: str):
        if type_scenario == "positive":
            return [(3, 5, 15, 16),
                    (7, 2, 14, 18),
                    (4.5, 3.5, 15.75, 16),
                    (10, 10, 100, 40)]
        if type_scenario == "negative":
            return [
                (-1, 5),
                (3, -5),
                (0, 4),
                (4, 0),
                (-3, -3)
            ]

    yield _wrapper


