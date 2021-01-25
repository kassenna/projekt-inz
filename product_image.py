import pygame
from moveable_object import Moveable_object
from product_data import Product_data
from points import Point, Rectangle


class Product_image(Moveable_object):
    def __init__(self, coordinate: Rectangle, w: int, h: int, product: Product_data, name: str = None):
        try:
            self.image = pygame.image.load('images/' + name + '.png')
        except:
            self.image = pygame.image.load('images/test.png')
        super().__init__(coordinate, w, h)
        self.product = product
        self.price = product.price
        self.cursor = Point((0, 0))

    def click(self, pos: tuple):
        if self.position.is_in_area(Point(pos)):
            self.cursor = Point(pos)
            self.is_clicked = True
            self.product.is_clicked = True
            return self
