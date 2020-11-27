import copy
import pygame
from level import Level
from other.point import Rectangle, Point
from display_objects.object_display import Object_display


class Recipe_button(Object_display):
    def __init__(self, receipe, clock, screen):
        super().__init__(screen, screen.get_size()[0], screen.get_size()[1])
        self.receipe = receipe
        self.ID = receipe.id
        self.frame = Rectangle(0, 0, self.screen_w // 10, self.screen_w // 10)
        self.frame.move(Point((self.frame.size.x * (self.ID % 10), self.frame.size.y * (self.ID // 10))))
        self.frame.scale(self.frame.size.x // 10, self.frame.size.y // 10)
        self.square = copy.deepcopy(self.frame)
        self.square.scale(self.square.size.x // 20, self.square.size.y // 20)
        self.color = (100, 0, 0)
        if receipe.difficulty == 0:
            self.color = (0, 80, 0)
        elif receipe.difficulty == 1:
            self.color = (80, 80, 0)
        self.clock = clock


    def draw(self):
        if self.receipe.completed:
            clr = (50, 255, 50)
        else:
            clr = (255, 50, 50)
        pygame.draw.rect(self.screen, clr, self.frame.rectangle(), 0)
        pygame.draw.rect(self.screen, self.color, self.square.rectangle(), 0)

    def click(self, pos):
        return self.frame.is_in_area(Point(pos))

    def run(self, data):
        data.insert_product_to_receipe(self.receipe.id)
        Level(self.screen, self.clock, data, self.receipe.id).run()

    def resize(self, w, h):
        pass
