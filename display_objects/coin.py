import copy

import pygame

from display_objects.move_object import Move_object
from other.point import Rectangle, Point


class Coin(Move_object):
    def __init__(self, screen, w, h, coordinate, values=(0, 0), name='test.png'):
        try:
            self.image = pygame.image.load('images/' + name)
        except:
            self.image = pygame.image.load('images/test.png')
        super().__init__(coordinate, screen, w, h)
        self.values = values
