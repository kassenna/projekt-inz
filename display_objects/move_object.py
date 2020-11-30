import copy

import pygame

from display_objects.object_display import Object_display
from other.point import Rectangle, Point


class Move_object(Object_display):
    def __init__(self, coordinate, screen, w, h):
        super().__init__(screen, w, h)
        self.is_lay = False
        self.start_coordinate = Rectangle(coordinate[0], coordinate[1], coordinate[2], coordinate[3])
        self.position = copy.deepcopy(self.start_coordinate)
        self.position = self.position * Point((w, h))
        self.resize(w, h)
        self.dp = Point((0, 0))
        self.is_clicked = False

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
            return self

    def lay(self):
        if not self.is_lay:
            self.position = copy.deepcopy(self.start_coordinate)
            self.position = self.position * Point((self.screen_w, self.screen_h))
            self.is_clicked = False

    def move(self, pos):
        if not self.is_clicked:
            return
        else:
            point = Point(pos)
            self.dp = Point(pos) - self.mouse_pos
            self.position.move(self.dp)
            self.mouse_pos = point
