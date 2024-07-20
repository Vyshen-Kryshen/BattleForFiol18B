"""

"""
from abc import ABC, abstractmethod

import pygame
from pygame.image import load
from pygame.transform import scale
from pygame.mixer import Sound
from pygame.event import Event, EventType
from pygame.surface import Surface
from pygame.time import Clock
from pygame.key import ScancodeWrapper
from pygame.sprite import Sprite
from pygame.font import SysFont, Font
from pygame.constants import FULLSCREEN

from buildings import Building, Farm, EnergyStation, Mine, MilitaryFactory, Laboratory
from combat_units import (CombatUnit, GroundEquipment, AirForce, SpecialUnit, Ship, Engineer, Spy, Tank, Robot, Drone,
                          Bomber, Fighter, Infantry)
from territory import Territory, City, Base
from resources import Resource, Metal, Mineral, Food, Energy, Aluminium, Titan, Iron, Silicon, Coal, Uran
from ui import MyUIWidget, MyLabelWidget, MyButtonWidget, MyCheckButtonWidgets, MyMenuWidgets
from map_and_camera import Map, Camera
from game_constants import BACKGROUND_TEXTURE_PATH, MAIN_THEME_AUDIO_PATH, TITLE, MAX_VOLUME_VALUE
pygame.init()


class Scene(ABC, Surface):
    sprites: list[Sprite] = []
    bg_color: str = ""

    def __init__(self, scene_size: tuple[int, int], sprites: list[Sprite], bg_color: str) -> None:
        """

        :param scene_size: tuple-type object value with two integral objects value.
        :param sprites: list-type object value with Sprite-type objects value.
        :param bg_color: string-type object value.
        """
        super().__init__(scene_size)
        self.window: Surface = pygame.display.set_mode(scene_size, flags=FULLSCREEN)
        pygame.display.set_caption(TITLE)
        self.sprites = sprites
        self.clock_time: Clock = Clock()
        self.fps: float = 60.0
        self.bg_color = bg_color

    def add_sprite(self, some: Sprite) -> None:
        """

        :param some: Sprite-type object value.
        :return: None-type object value.
        """
        self.sprites.append(some)

    def del_sprite(self, exist: Sprite) -> None:
        """

        :param exist: Sprite-type object value.
        :return: None-type object value.
        """
        self.sprites.remove(exist)
        exist.kill()

    def blit_game_objects(self) -> None:
        """

        :return: None-type object value.
        """
        if self.sprites:
            for sprite in self.sprites:
                if isinstance(sprite, CombatUnit) or isinstance(sprite, Building):
                    self.blit(sprite.texture, sprite.position)

    @abstractmethod
    def event_handler(self) -> None:
        """

        :return: None-type object value.
        """
        pass


class MainMenuScene(Scene):
    """

    """

    def __init__(self, game_objects: list[Sprite | Surface], bg_color: str) -> None:
        """

        :param game_objects: list-type object value with Sprite-type objects value.
        :param bg_color: string-type object value.
        """
        super().__init__((1600, 900), game_objects, bg_color)
        self.bg_image: Surface = load(BACKGROUND_TEXTURE_PATH)
        self.bg_image = scale(self.bg_image, (self.get_width(), self.get_height())).convert_alpha()
        self.music: Sound = Sound(MAIN_THEME_AUDIO_PATH)
        self.music.set_volume(0.01)
        self.blit(self.bg_image, (0, 0))
        font1: Font = SysFont("SporedomRUS", 90, False, False)
        font2: Font = SysFont("SporedomRUS", 93, False, False)
        self.text1: Surface = font1.render("Битва за Fiol-18B", True, "white")
        self.text2: Surface = font2.render("Битва за Fiol-18B", True, "white")
        self.text2.set_alpha(63)

    def handle_game_objects(self, event: Event = None) -> None:
        """

        :param event: Event-type object value.
        :return: None-type object value.
        """
        if self.sprites:
            for sprite in self.sprites:
                if event:
                    if isinstance(sprite, MyUIWidget):
                        self.window.blit(sprite.texture, sprite.position)
                        sprite.action_if_to_focussed()
                        sprite.action_if_to_click(event)

    def dark_preview(self, surface: Surface, alpha_channel: int) -> tuple[Surface, int]:
        """

        :param surface: Surface-type object value.
        :param alpha_channel: integral-type object value.
        :return: tuple-type object value with Surface-type object value and integral-type object value.
        """
        if alpha_channel > 0:
            alpha_channel -= 1
            surface.set_alpha(int(round(alpha_channel, 0)))
            self.window.blit(surface, (0, 0))
            surface.fill("black")
        if self.music.get_volume() <= MAX_VOLUME_VALUE:
            self.music.set_volume(self.music.get_volume() + self.music.get_volume())
        return surface, alpha_channel

    def event_handler(self, debug: bool = False) -> None:
        """

        :param debug: boolean-type object value.
        :return: None-type object value.
        """
        current_event: Event = None
        dark_surface: Surface = Surface(self.window.get_size())
        dark_surface_alpha: int = 255
        black_surface: Surface = Surface((1600, 120))
        black_surface.fill("black")
        while True:
            self.music.play()
            self.window.fill(self.bg_color)
            self.window.blit(self, (0, 0))
            self.window.blit(black_surface, (0, 0))
            self.handle_game_objects(current_event)
            keys: ScancodeWrapper = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                pass
            elif keys[pygame.K_s]:
                pass
            if keys[pygame.K_a]:
                pass
            elif keys[pygame.K_d]:
                pass
            for event in pygame.event.get():
                current_event = event
                if event.type == pygame.QUIT:
                    pygame.quit()
                    break
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        break
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 0:
                        pass
            else:
                self.window.blit(self.text1, (300, 30))
                self.window.blit(self.text2, (285, 30))
                if debug:
                    self.window.blit(pygame.font.SysFont("Arial", 50).render(str(self.clock_time.get_fps()), True, "white"), (100, 100))
                if dark_surface_alpha > 0:
                    dark_surface, dark_surface_alpha = self.dark_preview(dark_surface, dark_surface_alpha)
                pygame.display.flip()
                self.clock_time.tick(self.fps)


if __name__ == '__main__':
    buttons: list[MyButtonWidget] = [MyButtonWidget((i, 720), 180, 120, 0.1) for i in range(270, 1080 + 270, 270)]
    mms: MainMenuScene = MainMenuScene(buttons, "black")
    mms.event_handler()
