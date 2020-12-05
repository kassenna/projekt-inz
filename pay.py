import pygame
from display_objects.counter import Counter
from play import Play
from display_objects.pocket import Pocket


class Pay(Play):
    def __init__(self, screen_w, screen_h, count):
        self.size = (screen_w, screen_h)
        self.counter = Counter(screen_w, screen_h, (0.3, 0.1, 0.7, 0.5))
        self.pocket = Pocket(screen_w, screen_h, (0.4, 0.6, 0.7, 0.8))
        self.pocket.count(count)
        self.pocket.create()

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
            Play.clock.tick(Play.FPS)
