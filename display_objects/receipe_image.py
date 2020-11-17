import copy
import pygame
from display_objects.object_display import Object_display
from point import Point, Rectangle

class Receipe_image(Object_display):
    def __init__(self, screen, w, h, receipe):
        super().__init__(screen, w, h)
        self.coordinate = Rectangle(0.75, 0.1, 0.9, 0.5)
        self.resize(w, h)
        pygame.font.init()
        self.font = pygame.font.SysFont('FONT_FRANCHISE', 30)
        self.receipe = receipe

    def draw(self):
        pygame.draw.rect(self.screen, (150, 160, 200), (self.position.rectangle()))
        pos = copy.deepcopy(self.position.point)
        pos.move(self.position.size.x//4, self.position.size.y//16)
        for rec in self.receipe.ingredient:
            if rec.is_clicked:
                self.font.set_bold(1)
            self.screen.blit(self.font.render(str(rec.name), False, (0, 0, 0)), pos.to_tuple())
            pos.move(0, 60)
        pass
    def resize(self, w, h):
        self.position = copy.deepcopy(self.coordinate)
        self.position * Point((w, h))


