import copy
import pygame
from display_objects.object_display import Object_display
from other.point import Rectangle, Point


class Moveable_object(Object_display):
    def __init__(self, coordinate, w, h):
        super().__init__(w, h)
        self.is_lay = False
        self.start_coordinate = Rectangle(coordinate)
        self.position = copy.deepcopy(self.start_coordinate) * Point((self.screen_w, self.screen_h))
        self.im = pygame.transform.scale(self.image, self.position.size.to_tuple())
        self.dp = Point((0, 0))
        self.is_clicked = False

    def resize(self, w: int, h: int) -> None:
        self.position = self.position * Point((1 / self.screen_w, 1 / self.screen_h))
        self.position = self.position * Point((w, h))
        self.im = pygame.transform.scale(self.image, self.position.size.to_tuple())
        self.screen_w, self.screen_h = w, h

    def draw(self) -> None:
        Object_display.screen.blit(self.im, self.position.point.to_tuple())

    def click(self, pos: tuple):
        if self.position.is_in_area(Point(pos)):
            self.is_clicked = True
            self.cursor = Point(pos)
            return self

    def lay(self) -> None:
        if not self.is_lay:
            self.position = copy.deepcopy(self.start_coordinate)
            self.position = self.position * Point((self.screen_w, self.screen_h))
            self.is_clicked = False

    def move(self, pos: tuple):
        if self.is_clicked:
            point = Point(pos)
            self.dp = Point(pos) - self.cursor
            self.position.move(self.dp)
            self.cursor = point
