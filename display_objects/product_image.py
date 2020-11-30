import pygame
import copy

from display_objects.move_object import Move_object
from other.point import Point

from other.point import Rectangle


class Product_image(Move_object):
    def __init__(self, coordinate, screen, w, h, product=None, name = 'test.png'):
        try:
            self.image = pygame.image.load('images/' + name + '.png')
        except:
            self.image = pygame.image.load('images/test.png')
        super().__init__(coordinate, screen, w, h)
        self.product = product
        self.is_lay = True


    def click(self, pos):
        if self.position.is_in_area(Point(pos)):
            self.is_clicked = True
            self.mouse_pos = Point(pos)
            self.product.is_clicked = True
            return self

    def lay(self):
        if not self.is_lay:
            self.position = copy.deepcopy(self.start_coordinate)
            self.position = self.position * Point((self.screen_w, self.screen_h))
            self.is_clicked = False
            self.product.is_clicked = False
            self.product.is_checked = False
        else:
            self.product.is_checked = True
