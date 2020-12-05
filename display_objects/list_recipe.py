import copy
import pygame

from data.product_data import Product_data
from display_objects.object_display import Object_display
import pygameAssets
from other.point import Point, Rectangle
from pay import Pay
from product import Product


class List_recipe(Object_display):
    def __init__(self, rec: Rectangle, w: int, h: int, name: str, i: int = 0, fontsize: int = 40,
                 is_title: bool = False):
        super().__init__(w, h)
        self.coordinate = copy.deepcopy(rec)
        self.coordinate.move(Point((self.coordinate.size.x / 2, 0.05 * (i + 1))))
        if is_title is True:
            self.name = name.upper()
        else:
            self.name = name
        self.font_size = fontsize
        self.resize(w, h)

    def draw(self) -> None:
        self.widget.draw()

    def resize(self, w: int, h: int) -> None:
        self.point = copy.copy(self.coordinate.point) * Point((w, h))
        self.widget = pygameAssets.TextBox(self.point.x, self.point.y, self.name, fontSize=self.font_size)


class Product_list(List_recipe):

    def __init__(self, rec: Rectangle, product: Product_data, i: int, w: int, h: int):
        name = str(product.number_recipe) + ' ' + product.name + str(product.price)
        super().__init__(rec, w, h, name, i, fontsize=32)
        self.product = product

    def draw(self):
        if self.product.is_checked:
            self.widget.setColor((0, 120, 0))
        else:
            Product_list.complete = False
            if self.product.is_clicked:
                self.widget.setColor((0, 0, 200))
            else:
                self.widget.setColor((0, 0, 0))
        super().draw()


class Button(Object_display):
    def __init__(self, coordinate, w, h, receipe):
        super().__init__(w, h)
        pygameAssets.Button.setScreen(Object_display.screen)
        self.coordinate = copy.deepcopy(coordinate)
        self.coordinate.move(Point((self.coordinate.size.x / 2, self.coordinate.size.y - 0.1)))
        self.resize(w, h)
        self.receipe = receipe

    def draw(self):
        if self.receipe.ingredient_completed:
            self.widget.setColor((0, 200, 0))
        else:
            self.widget.setColor((200, 0, 0))
        self.widget.draw()

    def resize(self, w: int, h: int):
        self.rec = copy.copy(self.coordinate) * Point((w, h))
        self.widget = pygameAssets.Button(self.rec.point.x, self.rec.point.y, self.rec.size.x // 2, 40,
                                          color=(0, 200, 0), text='zapłać', textColor=(0, 0, 0),
                                          activeColor=(0, 0, 100), fontSize=40)

    def click(self, event: pygame.event):
        if self.receipe.ingredient_completed:
            if self.widget.isPressed(event):
                Pay(self.screen_w, self.screen_h, 2.12).run()



