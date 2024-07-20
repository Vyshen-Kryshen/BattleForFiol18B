"""

"""
from abc import ABC


class Resource(ABC):
    """

    """
    amount: int = 0

    def __init__(self, amount: int) -> None:
        """

        :param amount: integral-type object value.
        """
        self.amount = amount


class Mineral(Resource, ABC):
    """

    """
    rarity: int = 0

    def __init__(self, amount: int, rarity: int) -> None:
        """

        :param amount: integral-type object value.
        :param rarity: integral-type object value.
        """
        super().__init__(amount)
        self.rarity = rarity


class Silicon(Mineral):
    """

    """
    def __init__(self, amount: int) -> None:
        """

        :param amount: integral-type object value.
        """
        super().__init__(amount, 1)


class Coal(Mineral):
    """

    """
    def __init__(self, amount: int) -> None:
        """

        :param amount: integral-type object value.
        """
        super().__init__(amount, 5)


class Uran(Mineral):
    """

    """
    def __init__(self, amount: int) -> None:
        """

        :param amount: integral-type object value.
        """
        super().__init__(amount, 5000)


class Metal(Resource, ABC):
    """

    """
    mass: float = 0.0
    strength: int = 0
    rarity: int = 0

    def __init__(self, amount: int, mass: float, strength: int, rarity: int) -> None:
        """

        :param amount: integral-type object value.
        :param mass: float_point-type object value.
        :param strength: integral-type object value.
        :param rarity: integral-type object value.
        """
        super().__init__(amount)
        self.mass = mass
        self.strength = strength
        self.rarity = rarity


class Iron(Metal):
    """

    """

    def __init__(self, amount: int) -> None:
        """

        :param amount: integral-type object value.
        """
        super().__init__(amount, 0.55, 250, 12)


class Aluminium(Metal):
    """

    """

    def __init__(self, amount: int) -> None:
        """

        :param amount: integral-type object value.
        """
        super().__init__(amount, 0.25, 100, 25)


class Titan(Metal):
    """

    """

    def __init__(self, amount: int) -> None:
        """

        :param amount: integral-type object value.
        """
        super().__init__(amount, 0.50, 150, 500)


class Energy(Resource):
    """

    """

    def __init__(self, amount: int) -> None:
        """

        :param amount: integral-type object value.
        """
        super().__init__(amount)


class Food(Resource):
    """

    """

    def __init__(self, amount: int) -> None:
        """

        :param amount: integral-type object value.
        """
        super().__init__(amount)


if __name__ == '__main__':
    al1: Aluminium = Aluminium(5)
