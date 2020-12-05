from display_objects.counter import Counter
from display_objects.rack import Rack
from play import Play
import pygame as pg
import time


class Level(Play):

    def __init__(self, id):
        self.screen_w, self.screen_h = Play.screen.get_size()
        self.recipe_id = id
        self.__set_level()
        self.counter = Counter(self.screen_w, self.screen_h, (0.00, 0.7, 1, 0.9))
        self.rack = Rack(self.screen_w, self.screen_h, self.recipe_id)

    def __set_level(self):
        self.recipe = Play.data.recipes[self.recipe_id]
        self.recipe.set_price()

    def resize(self):
        self.rack.resize(self.screen_w, self.screen_h)
        self.counter.resize(self.screen_w, self.screen_h)
        time.sleep(0.01)

    def run(self):
        product = None
        running = True
        while running:
            Play.screen.fill((255, 255, 230))
            self.counter.draw()
            self.rack.draw()
            for event in pg.event.get():
                if event.type == pg.VIDEORESIZE:
                    try:
                        self.screen_w, self.screen_h = event.size
                        self.resize()
                    except:
                        pass
                elif event.type == pg.QUIT:
                    quit()
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        return
                elif event.type == pg.MOUSEBUTTONDOWN:
                    product = self.rack.click(pos=pg.mouse.get_pos())
                    if product is not None:
                        self.counter.test_product(product, lay=False)
                elif event.type == pg.MOUSEBUTTONUP:
                    if product is not None:
                        self.counter.test_product(product, lay=True)
                        product.lay()
                        product = None
                        print(self.recipe.check())
                        print(' ')
                if product is not None:
                    product.current_image.move(pg.mouse.get_pos())
                    product.current_image.draw()

            self.rack.click(event=event)
            pg.display.update()
            self.clock.tick(self.FPS)
