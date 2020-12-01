import copy

import pygame

from display_objects.moveable_object import Moveable_object
from other.point import Rectangle, Point


class Coin(Moveable_object):
    def __init__(self, w, h, coordinate, values=(0, 0), name='test.png'):
        try:
            self.image = pygame.image.load('images/' + name)
        except:
            self.image = pygame.image.load('images/test.png')
        super().__init__(coordinate, w, h)
        self.values = values

    def lay(self) -> None:
            self.position = copy.deepcopy(self.start_coordinate)
            self.position = self.position * Point((self.screen_w, self.screen_h))
            self.is_clicked = False

