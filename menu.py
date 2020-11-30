import play
from display_objects.recipe_button import Recipe_button
import pygame as pg
from other.screen import Screen


class Menu(play.Play):
    def __init__(self, data, screen, clock):
        super().__init__(data, screen, clock)
        self.levels = list()
        self.__set_levels()
        self.run()

    def __set_levels(self):
        for recipe in self.data.recipes:
            self.levels.append(Recipe_button(recipe, self.clock, self.screen))

    def run(self):
        while True:
            self.screen.fill((100, 100, 150))
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
                            lvl.run(self.data)
                elif event.type == pg.VIDEORESIZE:
                    self.screen.self.screen_width, self.screen_height = event.size
            pg.display.update()
