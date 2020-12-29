import pygameAssets
import pygame
from element import Element
from object_display import Object_display
from points import Rectangle, Point
from price import Price


class Counter(Object_display):
    def __init__(self, w: int, h: int, cord: tuple):
        super().__init__(w, h)
        self.par = Rectangle(cord)
        self.counter_cor = Rectangle((0.8, 0.9, 1, 0.99))
        self.price = Price()
        self.resize(w, h)
        pygameAssets.Button.screen = self.screen
        self.elements = []

    def draw(self) -> None:
        pygame.draw.rect(Object_display.screen, (0, 153, 153), self.position.to_rectangle())
        self.counter.draw()

    def resize(self, w: int, h: int) -> None:
        self.position = self.par.copy() * Point((w, h))
        self.counter_pos = self.counter_cor.copy() * Point((w, h))
        self.counter = pygameAssets.Button(self.counter_pos[0],
                                           self.counter_pos[1],
                                           self.counter_pos[2],
                                           self.counter_pos[3],
                                           color=(0, 0, 0), text=str(self.price))

    def test_product(self, element: Element, lay: bool = None) -> None:
        if self.position.is_in_area(element.current_image.position.point):
            if lay is True:
                self.elements.append(element.current_image)
                element.current_image.on_counter = True
                element.lay()
            elif lay is False:
                element.current_image.on_counter = False
                self.elements.remove(element.current_image)
            self.price.clear()
            for i in self.elements:
                if i.on_counter:
                    self.price += i.price
            self.counter.setText(str(self.price))
        else:
            element.current_image.on_counter = False
            if lay is True:
                element.lay()
