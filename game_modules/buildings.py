"""

"""
from random import randint
from abc import ABC
from pygame.image import load
from pygame.transform import scale
from pygame.surface import Surface
from pygame.sprite import Sprite
from combat_units import Tank, Ship, Bomber, Robot, Drone, Fighter, CombatUnit
from game_modules.game_constants import FARMS_TEXTURES_PATHS


class Building(ABC, Sprite):
    """

    """
    texture: Surface
    position: tuple[int, int] = (0, 0)
    size: int = 0
    strength: float = 0.0
    _is_improved: bool = False
    is_attacked: bool = False

    def __init__(self, texture: Surface, position: tuple[int, int], size: int, strength: float) -> None:
        """

        :param texture:  Surface-type object value.
        :param position: tuple-type object value with two integrals objects value.
        :param size: integral-type object value.
        :param strength: float_point-type object value
        """
        Sprite.__init__(self)
        self.texture = texture
        self.texture = scale(self.texture, (size, size))
        self.position = position
        self.size = size
        self.__is_improved = False
        self.is_attacked = False
        self.strength = strength
        self._max_strength: float = self.strength
        self._i: int = 0
        self.__j: int = 0

    def heal(self, to_print: bool = False) -> None:
        """

        :param to_print: boolean-type object value.
        :return: None-type object value.
        """
        if not self.is_attacked:
            if self._is_improved:
                if self._i % 50 == 0 and self.strength + 10 <= self._max_strength:
                    self.strength += 10
                    if to_print:
                        print(self.strength)
            else:
                if self._i % 100 == 0 and self.strength + 5 <= self._max_strength:
                    self.strength += 5
                    if to_print:
                        print(self.strength)
            if self.strength > self._max_strength:
                self.strength = self._max_strength
            self._i += 1

    def upgrade(self, to_print: bool = False) -> None:
        """

        :param to_print: boolean-type object value.
        :return: None-type object value.
        """
        if self.__j == 0:
            self.__is_improved = True
            self.strength *= 2
            self._max_strength *= 2
            if to_print:
                print(self.strength)
        self.__j += 1

    def produce(self) -> int:
        """

        :return: integral-type object value.
        """
        if self._is_improved:
            if self._i % 50 == 0:
                return 10
        else:
            if self._i % 100 == 0:
                return 5
        self._i += 1


class Farm(Building):
    """

    """

    def __init__(self, position: tuple[int, int], size: int, strength: float) -> None:
        """

        :param position: tuple-type object value with two integrals objects value.
        :param size: integral-type object value.
        :param strength: float_point-type object value.
        """
        self.texture_path_number: int = randint(0, 3)
        self.texture: Surface = load(FARMS_TEXTURES_PATHS[self.texture_path_number])
        super().__init__(self.texture, position, size, strength)


class Mine(Building):
    """

    """

    def __init__(self, texture: Surface, position: tuple[int, int], size: int, strength: float) -> None:
        """

        :param texture:  Surface-type object value.
        :param position: tuple-type object value with two integrals objects value.
        :param size: integral-type object value.
        :param strength: float_point-type object value.
        """
        super().__init__(texture, position, size, strength)


class Laboratory(Building):
    """

    """

    def __init__(self, texture: Surface, position: tuple[int, int], size: int, strength: float) -> None:
        """

        :param texture:  Surface-type object value.
        :param position: tuple-type object value with two integrals objects value.
        :param size: integral-type object value.
        :param strength: float_point-type object value.
        """
        super().__init__(texture, position, size, strength)


class EnergyStation(Building):
    """

    """

    def __init__(self, texture: Surface, position: tuple[int, int], size: int, strength: float) -> None:
        """

        :param texture:  Surface-type object value.
        :param position: tuple-type object value with two integrals objects value.
        :param size: integral-type object value.
        :param strength: float_point-type object value.
        """
        super().__init__(texture, position, size, strength)


class MilitaryFactory(Building):
    """

    """
    product: str = ""

    def __init__(self, texture: Surface, position: tuple[int, int], size: int, strength: float, product: str) -> None:
        """

        :param texture:  Surface-type object value.
        :param position: tuple-type object value with two integrals objects value.
        :param size: integral-type object value.
        :param strength: float_point-type object value.
        :param product: string-type object value.
        """
        super().__init__(texture, position, size, strength)
        self.product = product

    def produce(self) -> CombatUnit | None:
        """

        :return: None-type object value.
        """
        if self._is_improved:
            if self._i % 500 == 0:
                match self.product:
                    case "TANK" | "Tank" | "tank":
                        pass
        else:
            if self._i % 1000 == 0:
                pass
        self._i += 1


if __name__ == '__main__':
    b1: EnergyStation = EnergyStation(Surface((100, 200)), (0, 0), 10, 50.6)
    b1.upgrade()
    b1.strength -= 15
    print(b1.strength)
    while True:
        b1.heal(True)
