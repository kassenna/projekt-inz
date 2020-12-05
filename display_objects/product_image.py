import pygame
import copy

from data.product_data import Product_data
from display_objects.moveable_object import Moveable_object
from other.point import Point


class Product_image(Moveable_object):
    def __init__(self, coordinate, w:int, h:int, product, name='test.png'):
        try:
            self.image = pygame.image.load('images/' + name + '.png')
        except:
            self.image = pygame.image.load('images/test.png')
        super().__init__(coordinate, w, h)
        self.product = product
        self.price = product.price


    def click(self, pos):
        if self.position.is_in_area(Point(pos)):
            self.cursor = Point(pos)
            self.is_clicked = True
            self.product.is_clicked = True
            return self

    def return_to_shelf(self):
        self.position = copy.deepcopy(self.start_coordinate)
        self.position = self.position * Point((self.screen_w, self.screen_h))