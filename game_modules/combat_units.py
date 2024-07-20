"""

"""
from abc import ABC, abstractmethod
from pygame.surface import Surface
from pygame.sprite import Sprite
from pygame.rect import Rect


class CombatUnit(ABC, Sprite):
    """

    """
    texture: Surface
    position: tuple[int, int] = (0, 0)
    size: int = 0
    health: float = 0
    speed: tuple[int, int] = (0, 0)
    power: float = 0
    rect: Rect

    def __init__(self, texture: Surface, position: tuple[int, int], size: int, health: float,
                 speed: tuple[int, int], power: float) -> None:
        """

        :param texture: Surface-type object value.
        :param position: tuple-type object value with two integrals objects value.
        :param size: integral-type object value.
        :param health: float_point-type object value.
        :param speed: tuple-type object value with two integrals objects value.
        :param power: float_point-type object value.
        """
        Sprite.__init__(self)
        self.texture = texture
        self.position = position
        self.size = size
        self.health = health
        self.speed = speed
        self.power = power
        self.rect = self.texture.get_rect(topleft=self.position)


class GroundEquipment(CombatUnit, ABC):
    cross_country_ability: str = ""
    load_capacity: int = 0
    weapons: list[str] = []

    def __init__(self, texture: Surface, position: tuple[int, int], size: int, armor_protection: float,
                 speed: tuple[int, int], power: float, cross_country_ability: str, load_capacity: int,
                 weapons: list[str]) -> None:
        """

        :param texture: Surface-type object value.
        :param position: tuple-type object value with two integrals objects value.
        :param size: integral-type object value.
        :param armor_protection: float_point-type object value.
        :param speed: tuple-type object value with two integrals objects value.
        :param power: float_point-type object value.
        :param cross_country_ability: string-type object value.
        :param load_capacity: integral-type object value.
        :param weapons: list-type object value with some count of string-type objects value.
        """
        super().__init__(texture, position, size, armor_protection, speed, power)
        self.cross_country_ability = cross_country_ability
        self.load_capacity = load_capacity
        self.weapons = weapons


class Tank(GroundEquipment):
    def __init__(self, texture: Surface, position: tuple[int, int], size: int, armor_protection: float,
                 speed: tuple[int, int], power: float, load_capacity: int,
                 weapons: list[str]) -> None:
        """

        :param texture: Surface-type object value.
        :param position: tuple-type object value with two integrals objects value.
        :param size: integral-type object value.
        :param armor_protection: float_point-type object value.
        :param speed: tuple-type object value with two integrals objects value.
        :param power: float_point-type object value.
        :param load_capacity: integral-type object value.
        :param weapons: list-type object value with some count of string-type objects value.
        """
        super().__init__(texture, position, size, armor_protection, speed, power, "tracked", load_capacity,
                         weapons)


class Robot(GroundEquipment):
    def __init__(self, texture: Surface, position: tuple[int, int], size: int, armor_protection: float,
                 speed: tuple[int, int], power: float, load_capacity: int,
                 weapons: list[str]) -> None:
        """

        :param texture: Surface-type object value.
        :param position: tuple-type object value with two integrals objects value.
        :param size: integral-type object value.
        :param armor_protection: float_point-type object value.
        :param speed: tuple-type object value with two integrals objects value.
        :param power: float_point-type object value.
        :param load_capacity: integral-type object value.
        :param weapons: list-type object value with some count of string-type objects value.
        """
        super().__init__(texture, position, size, armor_protection, speed, power, "walking", load_capacity,
                         weapons)


class AirForce(CombatUnit, ABC):
    def __init__(self, texture: Surface, position: tuple[int, int], size: int, health: float,
                 speed: tuple[int, int], power: float) -> None:
        """

        :param texture: Surface-type object value.
        :param position: tuple-type object value with two integrals objects value.
        :param size: integral-type object value.
        :param health: float_point-type object value.
        :param speed: tuple-type object value with two integrals objects value.
        :param power: float_point-type object value.
        """
        super().__init__(texture, position, size, health,speed, power)


class Fighter(AirForce):
    def __init__(self, texture: Surface, position: tuple[int, int], size: int, health: float,
                 speed: tuple[int, int], power: float) -> None:
        """

        :param texture: Surface-type object value.
        :param position: tuple-type object value with two integrals objects value.
        :param size: integral-type object value.
        :param health: float_point-type object value.
        :param speed: tuple-type object value with two integrals objects value.
        :param power: float_point-type object value.
        """
        super().__init__(texture, position, size, health, speed, power)


class Bomber(AirForce):
    def __init__(self, texture: Surface, position: tuple[int, int], size: int, health: float,
                 speed: tuple[int, int], power: float) -> None:
        """

        :param texture: Surface-type object value.
        :param position: tuple-type object value with two integrals objects value.
        :param size: integral-type object value.
        :param health: float_point-type object value.
        :param speed: tuple-type object value with two integrals objects value.
        :param power: float_point-type object value.
        """
        super().__init__(texture, position, size, health, speed, power)


class Drone(AirForce):
    def __init__(self, texture: Surface, position: tuple[int, int], size: int, health: float,
                 speed: tuple[int, int], power: float) -> None:
        """

        :param texture: Surface-type object value.
        :param position: tuple-type object value with two integrals objects value.
        :param size: integral-type object value.
        :param health: float_point-type object value.
        :param speed: tuple-type object value with two integrals objects value.
        :param power: float_point-type object value.
        """
        super().__init__(texture, position, size, health, speed, power)


class SpecialUnit(CombatUnit, ABC):
    def __init__(self, texture: Surface, position: tuple[int, int], size: int, health: float,
                 speed: tuple[int, int], power: float) -> None:
        """

        :param texture: Surface-type object value.
        :param position: tuple-type object value with two integrals objects value.
        :param size: integral-type object value.
        :param health: float_point-type object value.
        :param speed: tuple-type object value with two integrals objects value.
        :param power: float_point-type object value.
        """
        super().__init__(texture, position, size, health, speed, power)


class Spy(SpecialUnit):
    def __init__(self, texture: Surface, position: tuple[int, int], size: int, health: float,
                 speed: tuple[int, int], power: float) -> None:
        """

        :param texture: Surface-type object value.
        :param position: tuple-type object value with two integrals objects value.
        :param size: integral-type object value.
        :param health: float_point-type object value.
        :param speed: tuple-type object value with two integrals objects value.
        :param power: float_point-type object value.
        """
        super().__init__(texture, position, size, health, speed, power)


class Engineer(SpecialUnit):
    def __init__(self, texture: Surface, position: tuple[int, int], size: int, health: float,
                 speed: tuple[int, int], power: float) -> None:
        """

        :param texture: Surface-type object value.
        :param position: tuple-type object value with two integrals objects value.
        :param size: integral-type object value.
        :param health: float_point-type object value.
        :param speed: tuple-type object value with two integrals objects value.
        :param power: float_point-type object value.
        """
        super().__init__(texture, position, size, health, speed, power)


class Infantry(CombatUnit):
    endurance: int = 0
    dexterity: int = 0
    weapon: str = ""

    def __init__(self, texture: Surface, position: tuple[int, int], size: int, health: float,
                 speed: tuple[int, int], power: float, endurance: int, dexterity: int, weapon: str) -> None:
        """

        :param texture: Surface-type object value.
        :param position: tuple-type object value with two integrals objects value.
        :param size: integral-type object value.
        :param health: float_point-type object value.
        :param speed: tuple-type object value with two integrals objects value.
        :param power: float_point-type object value.
        :param endurance: integral-type object value.
        :param dexterity: integral-type object value.
        :param weapon: string-type object value.
        """
        super().__init__(texture, position, size, health, speed, power)
        self.endurance = endurance
        self.dexterity = dexterity
        self.weapon = weapon


class Ship(CombatUnit):
    weapon: str = ""
    maneuverability: int = 0
    cargo_compartment_volume: int = 0
    is_transports_equipment: bool = False
    is_transports_infantry: bool = False

    def __init__(self, texture: Surface, position: tuple[int, int], size: int, strength: float,
                 speed: tuple[int, int], power: float, weapon: str, maneuverability: int,
                 cargo_compartment_volume: int, is_transports_equipment: bool, is_transports_infantry: bool) -> None:
        """

        :param texture: Surface-type object value.
        :param position: tuple-type object value with two integrals objects value.
        :param size: integral-type object value.
        :param strength: float_point-type object value.
        :param speed: tuple-type object value with two integrals objects value.
        :param power: float_point-type object value.
        :param weapon: string-type object value.
        :param maneuverability: integral-type object value.
        :param cargo_compartment_volume: integral-type object value.
        :param is_transports_equipment: boolean-type object value.
        :param is_transports_infantry: boolean-type object value.
        """
        super().__init__(texture, position, size, strength, speed, power)
        self.weapon = weapon
        self.maneuverability = maneuverability
        self.cargo_compartment_volume = cargo_compartment_volume
        self.is_transports_equipment = is_transports_equipment
        self.is_transports_infantry = is_transports_infantry
