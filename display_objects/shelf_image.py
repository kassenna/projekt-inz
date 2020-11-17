import copy

import numpy
import pygame
import math
from display_objects.object_display import Object_display
from point import Rectangle, Point

class Shelf_image(Object_display):
    def __init__(self, x:float, y:float, xmax:float, ymax:float, s_width:int, s_height:int, screen):
        super().__init__(screen, s_width, s_height)
        self.color0 = (82, 33, 0)
        self.color1 = (65, 33, 0)
        self.color2 = (90, 40, 0)
        self.rectangle = Rectangle(x, y, xmax, ymax )
        self.resize(s_width, s_height)

    def resize(self, w, h):
        self.screen_w, self.screen_h = w, h
        rec = copy.deepcopy(self.rectangle)
        rec * Point((w, h))
        rec.end_coordinate.y
        tempx = (rec.end_coordinate.y- rec.point.y) / math.tan(0.5)
        temp_depth = (rec.end_coordinate.y - rec.point.y) * 0.3
        self.points0 = numpy.array([(rec.point.x, rec.point.y), ( rec.end_coordinate.x, rec.point.y), ( rec.end_coordinate.x + tempx, rec.end_coordinate.y), (rec.point.x + tempx, rec.end_coordinate.y)])
        self.points1 = numpy.array([(rec.point.x, rec.point.y), (rec.point.x + tempx, rec.end_coordinate.y), (rec.point.x + tempx, rec.end_coordinate.y + temp_depth), (rec.point.x, rec.point.y + temp_depth)])
        self.points2 = numpy.array([(rec.point.x + tempx, rec.end_coordinate.y), ( rec.end_coordinate.x + tempx, rec.end_coordinate.y), ( rec.end_coordinate.x + tempx, rec.end_coordinate.y + temp_depth),
                                    (rec.point.x+ tempx, rec.end_coordinate.y + temp_depth)])

    def draw(self):
        surface = pygame.display.get_surface()
        pygame.draw.polygon(surface, self.color0, self.points0)
        pygame.draw.polygon(surface, self.color1, self.points1)
        pygame.draw.polygon(surface, self.color2, self.points2)
