"""
Модуль для реализации внутреигровой камеры и карты.
"""
from dataclasses import dataclass
from pygame.surface import Surface
from pygame.image import load
from pygame.transform import scale
from game_modules.game_constants import DIRECTORY_PATH


@dataclass
class Camera:
    x: int
    y: int
    coefficient: float

    def move_on_x(self, add_to_x_value: int) -> None:
        """

        :param add_to_x_value: integral-type object value.
        :return: None-type object.
        """
        self.x += add_to_x_value

    def move_on_y(self, add_to_y_value: int) -> None:
        """

        :param add_to_y_value: integral-type object value.
        :return: None-type object value.
        """
        self.y += add_to_y_value

    def zoom_scaling(self, add_new_value: float) -> None:
        """

        :param add_new_value: float point value.
        :return: None-type object.
        """
        self.coefficient += add_new_value


class Map:
    parent_window: Surface
    texture: Surface

    def __init__(self, parent_window: Surface) -> None:
        """

        :param parent_window: surface-type object value.
        """
        self.parent_window = parent_window
        self.texture = load(FR"{DIRECTORY_PATH}\IronFist.png").convert_alpha(self.texture)
        self.texture = scale(self.texture, self.parent_window.get_size())
        self.camera_zoom: float = 0.0

    def subject_perception(self, camera: Camera) -> None:
        """

        :param camera: Camera-type object value.
        :return: None-type object value.
        """
        self.camera_zoom = camera.coefficient
        self.parent_window.blit(self.texture, (camera.x, camera.y))
        self.texture = scale(self.texture, (self.parent_window.get_width() * self.camera_zoom,
                                            self.parent_window.get_height() * self.camera_zoom))
