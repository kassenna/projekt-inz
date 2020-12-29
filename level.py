from pygameAssets import TextBox
from counter import Counter
from rack import Rack
from play import Play
import pygame as pg


class Level(Play):

    def __init__(self, id:int):
        self.screen_w, self.screen_h = Play.screen.get_size()
        self.recipe_id = id
        self.__set_level()
        self.counter = Counter(self.screen_w, self.screen_h, (0.00, 0.7, 1, 1))
        self.rack = Rack(self.screen_w, self.screen_h, self.recipe_id)
        self.label = TextBox(self.screen_w // 2, 20, "wybierz produkty według listy i przeciągnij je na ladę",
                             color=(200, 200, 200))

    def __set_level(self):
        self.recipe = Play.data.recipes[self.recipe_id]
        self.recipe.set_price()

    def __resize(self):
        self.rack.resize(self.screen_w, self.screen_h)
        self.counter.resize(self.screen_w, self.screen_h)

    def run(self):
        self.recipe.check()
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
                        self.__resize()
                    except:
                        pass
                elif event.type == pg.QUIT:
                    quit()
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        return
                elif event.type == pg.MOUSEBUTTONDOWN:
                    product = self.rack.click(pos=pg.mouse.get_pos())
                    if product is not None and product is not False:
                        self.counter.test_product(product, lay=False)
                elif event.type == pg.MOUSEBUTTONUP:
                    if product is not None and product is not False:
                        self.counter.test_product(product, lay=True)
                        product = None
                        self.recipe.check()
                if self.rack.click(event=event) is False:
                    return
            if product is not None and product is not False:
               product.current_image.move(pg.mouse.get_pos())
               product.current_image.draw()

            self.label.draw()
            pg.display.update()
            self.clock.tick(self.FPS)
