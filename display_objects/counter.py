import copy
import pygameAssets
import pygame

from display_objects.object_display import Object_display
from other.point import Rectangle, Point
from other.price import Price


class Counter(Object_display):
    def __init__(self, w: int, h: int, cord: tuple):
        super().__init__(w, h)
        self.par = Rectangle(cord)
        self.counter_cor = Rectangle((cord[0] + 0.1, cord[1] + 0.1, cord[0] + 0.18, cord[1] + 0.15))
        self.resize(w, h)
        pygameAssets.Button.screen = self.screen
        self.price = Price()
        self.counter = pygameAssets.Button(self.counter_pos.rectangle()[0],
                                           self.counter_pos.rectangle()[1],
                                           self.counter_pos.rectangle()[2],
                                           self.counter_pos.rectangle()[3],
                                           color=(0, 0, 0), text='%s zł, %s gr' % self.price.to_tuple())
        self.elements = []

    def draw(self) -> None:
        pygame.draw.rect(Object_display.screen, (0, 153, 153), self.position.rectangle())
        self.counter.draw()

    def resize(self, w: int, h: int) -> None:
        self.position = copy.deepcopy(self.par) * Point((w, h))
        self.counter_pos = copy.deepcopy(self.counter_cor) * Point((w, h))

    def test_product(self, element, lay=None) -> None:
        if self.position.is_in_area(element.current_image.position.point):
            element.current_image.is_lay = True
            if lay is True:
                self.elements.append(element.current_image)
            elif lay is False:
                self.elements.remove(element.current_image)

            self.price = Point((0, 0))
            for i in self.elements:
                if i.is_lay:
                    self.price = self.price + i.price

            self.counter.setText(str(self.price))

        else:
            element.current_image.is_lay = False
