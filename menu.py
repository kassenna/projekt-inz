from play import Play
from display_objects.receipe_lvl import Receipe_lvl
import pygame as pg
from pygame_menu import widgets
from screen import Screen



class Menu(Play):
    def __init__(self, data, screen,  clock):
        super().__init__(data, screen, clock)
        self.levels = list()
    def set_levels(self):
        for receipe in self.data.receipes:
            self.levels.append(Receipe_lvl(receipe, self.clock, self.screen))

    def run(self):

        while True:
            self.screen.fill((50, 50, 50))
            for lvl in self.levels:
                lvl.draw()

            for event in pg.event.get():
                 if event.type == pg.QUIT:
                    quit()
                 elif event.type == pg.KEYDOWN:
                    if event.type == pg.K_ESCAPE:
                        quit()
                 elif event.type == pg.MOUSEBUTTONDOWN:
                    for lvl in self.levels:
                        if lvl.click(pg.mouse.get_pos()):
                            pg.display.set_mode(Screen.get_size(), pg.RESIZABLE | pg.VIDEORESIZE)
                            lvl.run(self.data, 0)
                 elif event.type == pg.VIDEORESIZE:
                    self.screen.self.screen_width, self.screen_height = event.size

                #print(pg.mouse.get_pos())
            pg.display.update()

