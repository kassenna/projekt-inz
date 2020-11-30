import copy

import pygame

from display_objects.object_display import Object_display
from other.point import Parallelogram


class Counter(Object_display):
    def __init__(self, screen, w, h, x, y, xmax, ymax):
        super().__init__(screen, w, h)
        self.par = Parallelogram(x, y, xmax, ymax, 60)
        self.resize(w, h)

    def draw(self):
        #print(self.position.polygon())
        pygame.draw.polygon(self.screen, (0, 153, 153), self.position.polygon())

    def resize(self, w, h):
        self.position = copy.deepcopy(self.par)
        self.position.multiply(w, h)

    def test_product(self, element):
        if self.position.points.is_in_area(element.position.point):
            element.is_lay = True
        else:
            element.is_lay = False

