from play import Play
from recipe_button import Recipe_button
import pygame as pg
from screen import Screen


class Menu(Play):
    def __init__(self):
        super().__init__()
        self.screen_w: int = Play.screen.get_size()[0]
        self.screen_h: int = Play.screen.get_size()[1]
        self.levels = list()
        self.__set_levels()
        pg.display.set_mode(Screen.get_size(), pg.RESIZABLE | pg.VIDEORESIZE)
        self.run()

    def __set_levels(self):
        for recipe in Play.data.recipes:
            self.levels.append(Recipe_button(recipe, self.screen_w, self.screen_h))

    def resize(self):
        for i in self.levels:
            i.resize(self.screen_w, self.screen_h)

    def run(self):
        while True:
            Play.screen.fill((100, 100, 150))
            for lvl in self.levels:
                lvl.draw()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    quit()
                elif event.type == pg.VIDEORESIZE:
                    try:
                        self.screen_w, self.screen_h = event.size
                        self.resize()
                    except:
                        pass
                elif event.type == pg.KEYDOWN:
                    if event.type == pg.K_ESCAPE:
                        quit()
                elif event.type == pg.MOUSEBUTTONUP:
                    for lvl in self.levels:
                        if lvl.click(pg.mouse.get_pos()):
                            lvl.run()
                            Play.data.reset()
                elif event.type == pg.VIDEORESIZE:
                    self.screen_w, self.screen_h = event.size
            pg.display.update()
