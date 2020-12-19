import pygame

from uml.moveable_object import Moveable_object


class Coin_image(Moveable_object):
    def __init__(self, w, h, coordinate, values=None, name='test.png'):
        try:
            self.image = pygame.image.load('images/' + name)
        except:
            self.image = pygame.image.load('images/test.png')
        super().__init__(coordinate, w, h)
        self.price = values


