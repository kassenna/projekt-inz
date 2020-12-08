import copy

import pygame

from counter import Counter
from abstract_class.play import Play
from other.point import Rectangle
from payment.pocket import Pocket
from pygameAssets import TextBox

class Pay(Play):
    def __init__(self, screen_w, screen_h, count):
        self.screen_w = screen_w
        self.screen_h = screen_h
        self.label = TextBox(screen_w//2, 50, "Potrzeba zapłacić: " + str(count))
        self.counter = Counter(screen_w, screen_h, (0.3, 0.1, 0.7, 0.5))
        self.pocket = Pocket(screen_w, screen_h, (0.4, 0.6, 0.7, 0.8))
        self.pocket.count(copy.deepcopy(count))
        self.pocket.create()
        from abstract_class.button import Button_pay
        self.button = Button_pay(Rectangle((0.9, 0.9, 1, 1)), screen_w, screen_h, self.counter, count)

    def resize(self):
         pass

    def run(self):

        running = True
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
                        coin.lay()
                        coin = None
                if coin is not None:
                    coin.current_image.move(pygame.mouse.get_pos())
                    coin.draw()
                self.button.click(event=event)
            self.button.draw(self.counter.price)
            pygame.display.update()
            Play.clock.tick(Play.FPS)
