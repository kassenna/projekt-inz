from display_objects.counter import Counter
from display_objects.rack import Rack
from play import Play
import pygame as pg
import _thread
import time
from display_objects.product_image import Product_image


class Level(Play):

    def __init__(self, screen, clock, data, id):
        super().__init__(data, screen, clock)
        self.screen_width, self.screen_height = self.screen.get_size()
        self.id = id
        self.__set_level()
        self.counter = Counter(self.screen, self.screen_width, self.screen_height, 0.01, 0.77, 1, 0.9)

    def __set_level(self):
        self.recipe = self.data.recipes[self.id]
        self.rack = Rack(self.screen_width, self.screen_height, self.screen, self.data, self.id)
        # self.rack.set_receipe()

    def resize(self):
        self.rack.resize(self.screen_width, self.screen_height)
        self.counter.resize(self.screen_width, self.screen_height)
        time.sleep(0.01)

    def run(self):
        product = None
        running = True
        self.screen.fill((50, 50, 50))

        while running:
            self.screen.fill((255, 255, 230))
            self.counter.draw()
            self.rack.draw()

            for event in pg.event.get():

                if event.type == pg.VIDEORESIZE:
                    try:
                        self.screen_width, self.screen_height = event.size
                        _thread.start_new_thread(self.resize())
                    except:
                        pass

                elif event.type == pg.QUIT:
                    quit()
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        return
                elif event.type == pg.MOUSEBUTTONDOWN:
                    product = self.rack.click(pg.mouse.get_pos(), True)
                elif event.type == pg.MOUSEBUTTONUP:
                    if product is not None:

                        product.lay()
                        product = None
                if product is not None:
                    product.move(pg.mouse.get_pos())
                    self.counter.test_product(product)
                    product.draw()

            pg.display.update()
            self.clock.tick(self.FPS)
