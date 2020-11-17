import copy
import pygame
from display_objects.receipe_image import Receipe_image
from level import Level
from point import Rectangle, Point
from display_objects.object_display import Object_display

class Receipe_lvl(Object_display):
    def __init__(self, receipe, clock, screen):
        screen_size =  screen.get_size()
        super().__init__(screen, screen_size[0],screen_size[1])
        self.receipe = receipe
        self.frame = Rectangle(0, 0, screen_size[0] // 10, screen_size[0] // 10)
        self.frame.move(Point((self.frame.size.x * (receipe.id % 10), self.frame.size.y * (receipe.id // 10))))
        self.frame.resize(self.frame.size.x // 10, self.frame.size.y // 10)
        self.square = copy.deepcopy(self.frame)
        self.square.resize(self.square.size.x // 20, self.square.size.y//20)
        self.color = (100, 0, 0)
        if receipe.difficulty == 0:
            self.color = (0, 80, 0)
        elif receipe.difficulty == 1:
            self.color = (80, 80, 0)
        self.clock = clock
        self.receipe_image = Receipe_image(self.screen, screen_size[0], screen_size[1], receipe.ingredient)
    def draw(self):
        if self.receipe.completed:
            clr = (50, 255, 50)
        else:
            clr = (255, 50, 50)
        pygame.draw.rect(self.screen, clr, self.frame.rectangle(), 0)
        pygame.draw.rect(self.screen, self.color, self.square.rectangle(), 0)

    def click(self, pos):
        if self.frame == Point(pos):
           return True
        return False

    def run(self, data, id):
            Level(self.screen, self.clock, data, id).run()

    def resize(self, w, h):
        pass

