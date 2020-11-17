import copy

import pygame

from display_objects.object_display import Object_display
from point import Rectangle, Parallelogram


class Counter(Object_display):
    def __init__(self, screen, w, h, x, y, xmax, ymax ):
        super().__init__(screen, w, h)
        self.par = Parallelogram(x, y, xmax, ymax, 30)
        self.resize(w, h)

    def draw(self):
        pygame.draw.polygon(self.screen, (0, 0, 0), self.par.polygon())

    def resize(self, w, h):
        self.position = copy.deepcopy(self.par)
        #self.position.multiply(w, h)

