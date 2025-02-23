import math
import numpy
import pygame
from object_display import Object_display
from points import Rectangle, Point


class Shelf_image(Object_display):
    def __init__(self, coordinate, screen_w: int, screen_h: int):
        super().__init__(screen_w, screen_h)
        self.color0 = (82, 33, 0, 50)
        self.color1 = (65, 33, 0, 0)
        self.color2 = (90, 40, 0, 0)
        self.rectangle = Rectangle(coordinate)
        self.resize(screen_w, screen_h)

    def resize(self, w, h):
        self.screen_w, self.screen_h = w, h
        rec = self.rectangle.copy() * Point((w, h))
        self.tempx = (rec.end_coordinate.y - rec.point.y) / math.tan(0.5)
        temp_depth = (rec.end_coordinate.y - rec.point.y) * 0.3
        self.points0 = numpy.array([(rec.point.x, rec.point.y), (rec.end_coordinate.x, rec.point.y),
                                    (rec.end_coordinate.x + self.tempx, rec.end_coordinate.y),
                                    (rec.point.x + self.tempx, rec.end_coordinate.y)])
        self.points1 = numpy.array([(rec.point.x, rec.point.y), (rec.point.x + self.tempx, rec.end_coordinate.y),
                                    (rec.point.x + self.tempx, rec.end_coordinate.y + temp_depth),
                                    (rec.point.x, rec.point.y + temp_depth)])
        self.points2 = numpy.array([(rec.point.x + self.tempx, rec.end_coordinate.y),
                                    (rec.end_coordinate.x + self.tempx, rec.end_coordinate.y),
                                    (rec.end_coordinate.x + self.tempx, rec.end_coordinate.y + temp_depth),
                                    (rec.point.x + self.tempx, rec.end_coordinate.y + temp_depth)])

    def draw(self):
        surface = pygame.display.get_surface()
        pygame.draw.polygon(surface, self.color0, self.points0)
        pygame.draw.polygon(surface, self.color1, self.points1)
        pygame.draw.polygon(surface, self.color2, self.points2)
