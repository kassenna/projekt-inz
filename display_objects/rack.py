import pygame

from display_objects.counter import Counter
from display_objects.object_display import Object_display
from shelf import Shelf
from point import Rectangle
from display_objects.receipe_image import Receipe_image
class Rack(Object_display):
    def __init__(self, w, h, screen):
        super().__init__(screen, w, h)
        self.elements = list()
        self.__create_shelves()
        self.counter = Counter(self.screen, self.screen_w, self.screen_h, 0.01, 0.77, 0.95, 0.9)


    def __create_shelves(self):
        self.elements.append(Shelf(0, 0.02, 0.1, 0.33, 0.15, self.screen.get_size()[0], self.screen.get_size()[1]))
        self.elements.append(Shelf(1, 0.02, 0.25, 0.33, 0.3, self.screen.get_size()[0], self.screen.get_size()[1]))
        self.elements.append(Shelf(2, 0.02, 0.4, 0.33, 0.45, self.screen.get_size()[0], self.screen.get_size()[1]))
        self.elements.append(Shelf(3, 0.02, 0.55, 0.33, 0.6, self.screen.get_size()[0], self.screen.get_size()[1]))
        self.elements.append(Shelf(4, 0.37, 0.1, 0.65, 0.15, self.screen.get_size()[0], self.screen.get_size()[1]))
        self.elements.append(Shelf(5, 0.37, 0.25, 0.65, 0.3, self.screen.get_size()[0], self.screen.get_size()[1]))
        self.elements.append(Shelf(6, 0.37, 0.4, 0.65, 0.45, self.screen.get_size()[0], self.screen.get_size()[1]))
        self.elements.append(Shelf(7, 0.37, 0.55, 0.65, 0.6, self.screen.get_size()[0], self.screen.get_size()[1]))

    def draw(self):
        pygame.draw.rect(self.screen, (0, 77, 38), (10, 10, self.screen_w - 10, int(self.screen_h * 0.75)))
        # self.screen.blit(self.sheve_image, (50, 40))
        self.receipe_image.draw()
        for i in self.elements:
            i.draw()
        self.counter.draw()
    def resize(self, w, h):
        self.counter.resize(w,h)
        self.receipe_image.resize(w, h)
        self.screen_w = w
        self.screen_h = h
        for i in self.elements:
            i.resize(w, h)

    def set_receipe(self, recipe):
        self.receipe_image = Receipe_image(self.screen, self.screen_w, self.screen_h, recipe)

    def set_shelves(self, product):
        pass
