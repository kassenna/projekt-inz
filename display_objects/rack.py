import pygame

from display_objects.counter import Counter
from display_objects.object_display import Object_display
from display_objects.product_image import Product_image
from other.point import Point, Rectangle
from shelf import Shelf
from display_objects.recipe_widget import Recipe_widget


class Rack(Object_display):
    def __init__(self, w, h, screen, data, id):
        # print(id)
        super().__init__(screen, w, h)
        self.data = data
        self.recipe_widget = Recipe_widget(self.screen, self.screen_w, self.screen_h,
                                           self.data.recipes[id])
        self.move_element = []
        self.is_clicked = False
        self.shelves = list()
        self.__create_shelves()

    def __create_shelves(self):
        self.shelves.append(
            Shelf(0, 0.02, 0.1, 0.33, 0.15, self.screen, self.screen.get_size()[0], self.screen.get_size()[1]))
        self.shelves.append(
            Shelf(1, 0.02, 0.25, 0.33, 0.3, self.screen, self.screen.get_size()[0], self.screen.get_size()[1]))
        self.shelves.append(
            Shelf(2, 0.02, 0.4, 0.33, 0.45, self.screen, self.screen.get_size()[0], self.screen.get_size()[1]))
        self.shelves.append(
            Shelf(3, 0.02, 0.55, 0.33, 0.6, self.screen, self.screen.get_size()[0], self.screen.get_size()[1]))
        self.shelves.append(
            Shelf(4, 0.37, 0.1, 0.65, 0.15, self.screen, self.screen.get_size()[0], self.screen.get_size()[1]))
        self.shelves.append(
            Shelf(5, 0.37, 0.25, 0.65, 0.3, self.screen, self.screen.get_size()[0], self.screen.get_size()[1]))
        self.shelves.append(
            Shelf(6, 0.37, 0.4, 0.65, 0.45, self.screen, self.screen.get_size()[0], self.screen.get_size()[1]))
        self.shelves.append(
            Shelf(7, 0.37, 0.55, 0.65, 0.6, self.screen, self.screen.get_size()[0], self.screen.get_size()[1]))
        self.set_shelves()

    def draw(self):
        pygame.draw.rect(self.screen, (0, 77, 38), (10, 10, self.screen_w - 10, int(self.screen_h * 0.75)))
        self.recipe_widget.draw()
        for i in self.shelves:
            i.draw()

    def resize(self, w, h):
        self.recipe_widget.resize(w, h)
        self.screen_w = w
        self.screen_h = h
        for i in self.shelves:
            i.resize(w, h)

    def set_shelves(self):
        for i in self.data.products:
            self.move_element.append(self.shelves[i.shelf].add_product(i))

    def click(self, pos=None, event=None):
        if pos is not None:
            for i in self.shelves:
                product = i.click(pos)
                if product is not None:
                    return product
        if event is not None:
            self.recipe_widget.click(event)
