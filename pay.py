import copy

from tinydb import TinyDB, Query
import pygame
from tinydb.operations import set
from counter import Counter
from play import Play
from points import Rectangle
from pocket import Pocket
from pygameAssets import TextBox


class Pay(Play):
    path = None
    db = None
    def __init__(self, screen_w, screen_h, count, recipe):
        self.screen_w = screen_w
        self.screen_h = screen_h
        self.recipe = recipe
        self.label = TextBox(screen_w // 2, 50, "Do zapłaty: " + str(count), color=(150, 200, 200))
        self.counter = Counter(screen_w, screen_h, (0.3, 0.1, 0.7, 0.5))
        self.pocket = Pocket(screen_w, screen_h, (0.4, 0.6, 0.7, 0.8))
        self.pocket.count(copy.deepcopy(count))
        self.pocket.create()
        from button import Button_pay
        self.button = Button_pay(Rectangle((0.85, 0.85, 1, 1)), screen_w, screen_h, count)

    def resize(self):
        self.pocket.resize(self.size[0], self.size[1])
        self.counter.resize(self.size[0], self.size[1])
        self.button.resize(self.size[0], self.size[1])

    def complete_level(self, path='data/db.json'):
        if Pay.path is None:
            Pay.path = path
        if Pay.db is None:
            Pay.db = TinyDB(path)

        recipe = Pay.db.table('Receipe')
        self.recipe.completed = True
        r = Query()
        recipe.update(set("completed", True), r.name == self.recipe.name)

    def run(self):
        running = True
        win = False
        self.screen.fill((50, 50, 50))
        coin = None
        while running:
            self.screen.fill((139, 69, 19))
            self.counter.draw()
            self.pocket.draw()
            self.label.draw()

            for event in pygame.event.get():
                if event.type == pygame.VIDEORESIZE:
                    self.size = event.size
                    self.resize()
                elif event.type == pygame.QUIT:
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    coin = self.pocket.click(pos=pygame.mouse.get_pos())
                    if coin is not None:
                        self.counter.test_product(coin, lay=False)
                elif event.type == pygame.MOUSEBUTTONUP:
                    if coin is not None:
                        self.counter.test_product(coin, lay=True)
                        coin = None
                if coin is not None:
                    coin.current_image.move(pygame.mouse.get_pos())
                    coin.draw()
                if self.button.click(event=event):
                    if win is False:
                        self.complete_level()
                        self.label = TextBox(self.screen_w // 2, 50, 'Gratuluję! Poziom ukończony',
                                             color=(150, 200, 200))
                        self.button.setText('Powrót')
                        win = True
                    else:
                        return
            self.button.draw(self.counter.price)
            pygame.display.update()
            Play.clock.tick(Play.FPS)
