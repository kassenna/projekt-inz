import copy
import pygame
from display_objects.object_display import Object_display
from other.point import Point, Rectangle
from display_objects.list_recipe import Product_list, List_recipe


class Recipe_widget(Object_display):
    def __init__(self, screen, w, h, recipe):
        super().__init__(screen, w, h)
        self.coordinate = Rectangle(0.75, 0.1, 0.9, 0.5)
        self.recipe = recipe
        self.recipe_widget = []
        self.position = copy.deepcopy(self.coordinate)
        self.position = self.position * Point((w, h))
        self.recipe_widget.append(List_recipe(self.coordinate, w, h, self.recipe.name, is_title= True))

        for i, product in enumerate(self.recipe.ingredient):
            self.recipe_widget.append(Product_list(self.coordinate, product, i+1, w, h))


    def draw(self):
        pygame.draw.rect(self.screen, (150, 160, 200), (self.position.rectangle()))
        for i in self.recipe_widget:
            i.draw()

    def resize(self, w, h):
        self.position = copy.deepcopy(self.coordinate)
        self.position = self.position * Point((w, h))
        for i in self.recipe_widget:
            i.resize(w, h)

