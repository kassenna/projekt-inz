import copy

import pygame

from display_objects.object_display import Object_display
import pygameAssets

from other.point import Point, Rectangle
from pay import Pay


class List_recipe(Object_display):

    def __init__(self, coordinate, w, h, name, i=0, fontsize=40, is_title=False):
        super().__init__(None, w, h)
        self.coordinate = copy.deepcopy(coordinate)
        self.coordinate.move(Point((self.coordinate.size.x / 2, 0.05 * (i + 1))))
        if is_title is True:
            self.name = name.upper()
        else:
            self.name = name
        self.font_size = fontsize
        self.resize(w, h)

    def draw(self):
        self.widget.draw()

    def resize(self, w, h):
        self.point = copy.copy(self.coordinate.point) * Point((w, h))
        self.widget = pygameAssets.TextBox(self.point.x, self.point.y, self.name, fontSize=self.font_size)


class Product_list(List_recipe):
    def __init__(self, coordinate, product, i, w, h):
        super().__init__(coordinate, w, h, product.name + ' ' + str(product.price) + ' zł', i, fontsize=32)
        self.product = product

    def draw(self):
        if self.product.is_checked:
            self.widget.setColor((0, 120, 0))
        else:
            if self.product.is_clicked:
                self.widget.setColor((0, 0, 200))
            else:
                self.widget.setColor((0, 0, 0))
        super().draw()


class Button_ok(Object_display):
    def __init__(self, coordinate, w, h, screen):
        super().__init__(screen, w, h)
        pygameAssets.Button.setScreen(screen)
        self.coordinate = copy.deepcopy(coordinate)
        self.coordinate.move(Point((self.coordinate.size.x / 2, self.coordinate.size.y - 0.1)))
        self.resize(w, h)

    #        def __init__(self, x, y, w, h, color=(102, 102, 102), activeColor=(150, 150, 150), text='',
    #                    textColor=(255, 255, 255), fontSize=30, fontFamily=None, align='center', screen=None):

    def draw(self):
        self.widget.draw()

    def resize(self, w, h):
        self.rec = copy.copy(self.coordinate) * Point((w, h))
        self.widget = pygameAssets.Button(self.rec.point.x, self.rec.point.y, self.rec.size.x // 2, 40,
                                          color=(150, 150, 159), text='zapłać', textColor=(0, 0, 0),
                                          activeColor=(0, 0, 100), fontSize=40)

    def click(self, event):
        if self.widget.isPressed(event):
            Pay(None, self.screen, pygame.time.Clock(), self.screen_w, self.screen_h).run()
