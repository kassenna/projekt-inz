import copy
import pygame
from data.recipe_data import Recipe_data
from shop.level import Level
from other.point import Rectangle, Point
from abstract_class.object_display import Object_display
from pygameAssets import Button


class Recipe_button(Object_display):
    def __init__(self, receipe:Recipe_data, w:int, h:int):
        Button.screen = Object_display.screen
        super().__init__(w, h)
        self.receipe = receipe
        self.ID = receipe.id
        self.frame = Rectangle((0, 0, self.screen_w // 10, self.screen_w // 10))
        self.frame.move(Point((self.frame.size.x * (self.ID % 10), self.frame.size.y * (self.ID // 10))))
        self.frame.scale(self.frame.size.x // 10, self.frame.size.y // 10)
        self.square = copy.deepcopy(self.frame)
        self.square.scale(self.square.size.x // 20, self.square.size.y // 20)
        self.square.move(Point((self.square.size.x//2, self.square.size.y//2)))
        self.color = (100, 0, 0)
        if receipe.difficulty == 0:
            self.color = (0, 80, 0)
        elif receipe.difficulty == 1:
            self.color = (80, 90, 0)

        self.button = Button(self.square.point.x, self.square.point.y, self.square.size.x, self.square.size.y,
                             text = receipe.name, color=self.color)

    def draw(self) -> None:
        if self.receipe.completed:
            clr = (50, 255, 50)
        else:
            clr = (255, 50, 50)
        pygame.draw.rect(Object_display.screen, clr, self.frame.rectangle(), 0)
        self.button.draw()

    def click(self, pos:tuple) -> bool:
        return self.frame.is_in_area(Point(pos))

    def run(self):
        Object_display.data.insert_product_to_receipe(self.receipe.id)
        Level(self.receipe.id).run()

    def resize(self, w, h):
        pass
