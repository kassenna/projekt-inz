import copy

import pygame

from abstract_class.moveable_object import Moveable_object
from other.point import Rectangle, Point


class Coin_image(Moveable_object):
    def __init__(self, w, h, coordinate, values=None, name='test.png'):
        try:
            self.image = pygame.image.load('images/' + name)
        except:
            self.image = pygame.image.load('images/test.png')
        super().__init__(coordinate, w, h)
        self.price = values


