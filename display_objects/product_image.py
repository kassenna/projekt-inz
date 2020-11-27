import pygame
import copy
from other.point import Point
from display_objects.object_display import Object_display
from other.point import Rectangle


class Product_image(Object_display):
    def __init__(self, coordinate, screen, w, h, product=None, name='test.png'):
        super().__init__(screen, w, h)
        try:
            self.image = pygame.image.load('images/' + name + '.png')
        except:
            self.image = pygame.image.load('images/test.png')
        self.product = product
        self.start_coordinate = Rectangle(coordinate[0], coordinate[1], coordinate[2], coordinate[3])
        self.position = copy.deepcopy(self.start_coordinate)
        # print(self.position.get_coordinate())
        self.position = self.position * Point((w, h))
        #print("abc" + str(self.position.get_coordinate()))
        self.resize(w, h)
        self.is_clicked = False
        self.dponit = Point((0, 0))
        self.is_lay = True

    def resize(self, w, h):

        self.position = self.position * Point((1 / self.screen_w, 1 / self.screen_h))
        self.position = self.position * Point((w, h))
        self.current_image = pygame.transform.scale(self.image, self.position.size.to_tuple())
        self.screen_w, self.screen_h = w, h

    def draw(self):
        self.screen.blit(self.current_image, self.position.point.to_tuple())

    def click(self, pos):
        if self.position.is_in_area(Point(pos)):
            self.is_clicked = True
            self.mouse_pos = Point(pos)
            self.product.is_clicked = True
            return self

    def lay(self):
        if not self.is_lay:
            self.position = copy.deepcopy(self.start_coordinate)
            self.position = self.position* Point((self.screen_w, self.screen_h))
            self.is_clicked = False
            self.product.is_clicked = False
            self.product.is_checked = False
        else:
            self.product.is_checked = True

        #print(self.is_lay)

    def move(self, pos):
        if not self.is_clicked:
            return
        else:
            point = Point(pos)
            self.dponit = Point(pos) - self.mouse_pos
            self.position.move(self.dponit)
            self.mouse_pos = point
