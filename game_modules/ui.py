"""

"""
from abc import ABC, abstractmethod
import pygame
from pygame.event import Event
from pygame.transform import scale
from pygame.image import load
from pygame.font import SysFont, Font
from pygame.color import Color
from pygame.rect import Rect
from pygame.surface import Surface
from game_constants import BUTTON_TEXTURES_PATHS


class MyUIWidget(Surface, ABC):
    """

    """

    def __init__(self, texture: Surface, position: tuple[int, int], width: int, height: int) -> None:
        """

        :param texture: Surface-type object value.
        :param position: tuple-type object value with two integrals-type objects values.
        :param width: integral-type object value.
        :param height: integral-type object value.
        """
        super().__init__((width, height))
        self.texture = texture
        self.texture = scale(self.texture, (width, height))
        self.position = position
        self.width = width
        self.height = height
        self.rect: Rect = self.texture.get_rect(topleft=self.position)
        self.is_clicked: bool = False
        self.is_focussed: bool = False

    @abstractmethod
    def action_if_to_focussed(self) -> None:
        """

        :return: None-type object value.
        """

    @abstractmethod
    def action_if_to_click(self, event: Event) -> None:
        """

        :param event: Event-type object value.
        :return: None-type object value.
        """


class MyLabelWidget(MyUIWidget):
    """

    """

    def __init__(self, text: str, position: tuple[int, int], width: int,
                 height: int) -> None:
        """

        :param text: string-type object value.
        :param position: tuple-type object value with two integrals-type objects values.
        :param width: integral-type object value.
        :param height: integral-type object value.
        """
        self.text = text
        self.color = "darkgrey"
        self.__old_color: str | Color | tuple[int, int, int] = self.color
        self.font: Font = SysFont("Arial", (width * height) // 8, False, False)
        self.texture: Surface = self.font.render(self.text, True, self.color)
        super().__init__(self.texture, position, width, height)

    def _update_text_ure(self) -> None:
        """

        :return: None-type object value.
        """
        self.texture = self.font.render(self.text, True, self.color)

    def action_if_to_focussed(self) -> None:
        """

        :return: None-type object value.
        """
        mouse_rect: Rect = Rect(pygame.mouse.get_pos(), (1, 1))
        if mouse_rect.colliderect(self.rect) and not self.is_clicked:
            self.color = "grey"
            self._update_text_ure()
            self.is_focussed = True
        else:
            self.color = self.__old_color
            self.is_focussed = False

    def action_if_to_click(self, event: Event) -> None:
        """

        :param event: Event-type object value.
        :return: None-type object value.
        """
        if self.is_focussed:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.color = "white"
                    self._update_text_ure()
                    self.is_clicked = True
                else:
                    self.color = "grey"
                self.is_clicked = False


class MyButtonWidget(MyUIWidget):
    """

    """

    def __init__(self, position: tuple[int, int], width: int, height: int, delay: float = 0.0) -> None:
        """

        :param position: tuple-type object value with two integrals-type objects values.
        :param width: integral-type object value.
        :param height: integral-type object value.
        :param delay: float_point-type object value.
        """
        self.texture: Surface = load(BUTTON_TEXTURES_PATHS[0])
        super().__init__(self.texture, position, width, height)
        self.delay = delay

    def action_if_to_focussed(self) -> None:
        """

        :return: None-type object value.
        """
        mouse_rect: Rect = Rect(pygame.mouse.get_pos(), (1, 1))
        if mouse_rect.colliderect(self.rect) and not self.is_clicked:
            self.texture = load(BUTTON_TEXTURES_PATHS[1])
            self.texture = scale(self.texture, (self.width, self.height))
            self.is_focussed = True
        else:
            self.texture = load(BUTTON_TEXTURES_PATHS[0])
            self.texture = scale(self.texture, (self.width, self.height))
            self.is_focussed = False

    def action_if_to_click(self, event: Event) -> None:
        """

        :param event: Event-type object value.
        :return: None-type object value.
        """
        if self.is_focussed:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.texture = load(BUTTON_TEXTURES_PATHS[2])
                    self.texture = scale(self.texture, (self.width, self.height))
                    self.is_clicked = True
                else:
                    self.texture = load(BUTTON_TEXTURES_PATHS[1])
                    self.texture = scale(self.texture, (self.width, self.height))
                self.is_clicked = False


class MyMenuWidgets(MyUIWidget):
    """

    """

    def __init__(self, position: tuple[int, int], width: int, height: int) -> None:
        """

        :param position: tuple-type object value with two integrals-type objects values.
        :param width: integral-type object value.
        :param height: integral-type object value.
        """
        self.texture: Surface = load("")
        super().__init__(self.texture, position, width, height)

    def action_if_to_focussed(self) -> None:
        """

        :return: None-type object value.
        """
        pass

    def action_if_to_click(self, event: Event) -> None:
        """

        :param event: Event-type object value.
        :return: None-type object value.
        """
        pass


class MyCheckButtonWidgets(MyButtonWidget):
    """

    """

    def __init__(self, position: tuple[int, int], width: int, height: int, delay: float = 0.0) -> None:
        """

        :param position: tuple-type object value with two integrals-type objects values.
        :param width: integral-type object value.
        :param height: integral-type object value.
        :param delay: float_point-type object value.
        """
        super().__init__(position, width, height, delay)

    def action_if_to_focussed(self) -> None:
        """

        :return: None-type object value.
        """
        pass

    def action_if_to_click(self, event: Event) -> None:
        """

        :param event: Event-type object value.
        :return: None-type object value.
        """
        pass


if __name__ == '__main__':
    pass
