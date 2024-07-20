"""

"""
from scenes import *


class Game:
    """

    """
    scenes: tuple[Scene, ...] = ()

    def __init__(self, *scenes) -> None:
        """

        :param scenes: tuple-type object value with Scene-type objects values.
        """
        self.scenes = scenes

    def mainloop(self) -> None:
        """

        :return: None-type object value.
        """
        for scene in self.scenes:
            scene.event_handler()


if __name__ == '__main__':
    game: Game = Game()
