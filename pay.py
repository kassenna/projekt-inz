import pygame
from display_objects.coin import Coin
from display_objects.counter import Counter
from other.point import Rectangle
from play import Play
from pocket import Pocket


class Pay(Play):
    def __init__(self, data, screen, clock, screen_w, screen_h):
        super().__init__(data, screen, clock)
        self.size = (screen_w, screen_h)
        #self.coin = Coin(self.screen, screen_w, screen_h, (0.1, 0.1, 0.2, 0.2), name='0zl.png')
        self.counter = Counter(self.screen, screen_w, screen_h, 0.1, 0.1, 0.8, 0.5)
        self.pocket = Pocket()
        self.pocket.count(12.90)
        self.pocket.create(self.screen, screen_w, screen_h, (0.1, 0.2, 0.3, 0.3))

    def resize(self):
        pass

    def run(self):
        running = True
        self.screen.fill((50, 50, 50))
        coin = None
        while running:
            self.screen.fill((255, 255, 230))
            self.counter.draw()
            self.pocket.draw()
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
                    coin = self.pocket.click(posK=pygame.mouse.get_pos())
                elif event.type == pygame.MOUSEBUTTONUP:
                    if coin is not None:
                        coin.lay()
                        coin = None
                if coin is not None:
                    coin.move(pygame.mouse.get_pos())
                    self.counter.test_product(coin)
                    coin.draw()

                pygame.display.update()

                self.pocket.move(pos=pygame.mouse.get_pos())
            self.clock.tick(self.FPS)
