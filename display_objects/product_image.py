import pygame
import copy
from point import Point
from display_objects.object_display import Object_display
from point import Rectangle
from product import Product


class Product_image(Object_display):
    def __init__(self, coordinate, screen, w, h, product=None, name='test.png'):
        super().__init__(screen, w, h)
        self.image = pygame.image.load('data/images/' + name)
        self.product = product
        self.start_coordinate = Rectangle(coordinate[0], coordinate[1], coordinate[2], coordinate[3])
        self.position = copy.copy(self.start_coordinate)
        self.position * Point((w, h))
        self.size = self.image.get_rect().size
        self.resize(w, h)
        self.is_clicked = False
        self.dponit = Point((0, 0))

    def resize(self, w, h):
        self.position * Point((1 / self.screen_w, 1 / self.screen_h))
        self.position * Point((w, h))
        self.current_image = pygame.transform.scale(self.image, self.position.size.to_tuple())
        self.screen_w, self.screen_h = w, h

    def draw(self):
        self.screen.blit(self.current_image, self.position.point.to_tuple())

    def click(self, pos, clicked=True):
        if clicked:
            if self.position == Point(pos):
                self.is_clicked = True
                self.mouse_pos = Point(pos)
                self.product.is_clicked = True

        else:
            self.is_clicked = False
            self.product.is_clicked = False

    def move(self, pos):
        if not self.is_clicked:
            return
        else:
            point = Point(pos)
            self.dponit = Point(pos) - self.mouse_pos
            self.position.move(self.dponit)
            self.mouse_pos = point
