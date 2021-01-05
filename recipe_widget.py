import pygame
from button import Button_ok
from object_display import Object_display
from points import Point, Rectangle
from list_recipe import Product_list, List_recipe


class Recipe_widget(Object_display):
    def __init__(self, w, h, recipe):
        super().__init__(w, h)
        self.coordinate = Rectangle((0.75, 0.1, 0.9, 0.7))
        self.recipe = recipe
        self.recipe_widget = []
        self.position = self.coordinate.copy()

        self.position *= Point((w, h))
        self.recipe_widget.append(List_recipe(self.coordinate, w, h, self.recipe.name, is_title=True,
                                              fontsize=int(self.coordinate.size.y * 38)))

        for i, product in enumerate(self.recipe.ingredient):
            self.recipe_widget.append(Product_list(self.coordinate, product, i + 1, w, h))
        self.button = Button_ok(self.coordinate, w, h, recipe)
        self.recipe_widget.append(self.button)

    def draw(self):
        pygame.draw.rect(self.screen, (150, 160, 200), (self.position.to_rectangle()))
        for i in self.recipe_widget:
            i.draw()

    def resize(self, w: int, h: int):
        self.position = self.coordinate.copy()
        self.position = self.position * Point((w, h))

        for i in self.recipe_widget:
            i.resize(w, h)

    def click(self, event):
        return self.button.click(event)
