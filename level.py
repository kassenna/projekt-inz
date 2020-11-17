from display_objects.rack import Rack
from play import Play
import pygame as pg
import _thread
import time
from display_objects.product_image import Product_image
class Level(Play):

    def __init__(self,  screen, clock, data= None, id = 0):
        super().__init__(data, screen, clock)
        self.screen_width, self.screen_height = self.screen.get_size()
        self.__set_level(id)
        
    def __set_level(self, lvl):
        self.recipe = self.data.receipes[lvl]
        self.rack = Rack(self.screen_width, self.screen_height, self.screen)
        self.rack.set_receipe(self.recipe)
        self.rack.set_shelves(None)

    def resize(self):
        print("resize")
        self.rack.resize(self.screen_width, self.screen_height)
        time.sleep(0.01)
        print(f"{self.screen_width, self.screen_height}")

    def run(self):
      test = Product_image((0.5, 0.1, 0.55, 0.15), self.screen, self.screen_width, self.screen_height)
      running = True
      self.screen.fill((50, 50, 50))

      while running:
        self.rack.draw()
        test.draw()
        for event in pg.event.get():

            if event.type == pg.VIDEORESIZE:
                try:
                    self.screen_width, self.screen_height = event.size
                    test.resize(self.screen_width, self.screen_height)
                    _thread.start_new_thread(self.resize())
                except:
                    pass

            elif event.type == pg.QUIT:
                quit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    return
            elif event.type == pg.MOUSEBUTTONDOWN:
                test.click(pg.mouse.get_pos())
            elif event.type == pg.MOUSEBUTTONUP:
                test.click(pg.mouse.get_pos(), False)
            test.move(pg.mouse.get_pos())
        pg.display.update()
        self.clock.tick(self.FPS)


