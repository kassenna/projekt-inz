import pygame
from price import Price
from coin import Coin
from object_display import Object_display
from points import Rectangle, Point


class Pocket(Object_display):
    def __init__(self, w, h, coordinate):
        super().__init__(w, h)
        self.price = None
        self.coordinate = Rectangle(coordinate)
        self.position = self.coordinate * Point((w, h))
        self.nominal = [50, 20, 10, 5, 2, 1]
        self.zl_count = []
        self.gr_count = []
        self.coins = []

    def count(self, sum: Price):
        self.price = sum.copy()
        for i in self.nominal:
            zl_temp = sum.zl // i
            gr_temp = sum.gr // i
            self.zl_count.append(zl_temp)
            self.gr_count.append(gr_temp)
            sum.zl -= zl_temp * i
            sum.gr -= gr_temp * i

    def create(self):
        coordinate = self.coordinate.copy()
        coordinate.setsize(self.coordinate.size.x - 0.1, self.coordinate.size.y - 0.1)
        for idx, nom in enumerate(self.nominal):
            self.coins.append(Coin(self.screen_w, self.screen_h, coordinate, values=Price(nom),
                                   number=self.zl_count[idx]))
            self.coins.append(Coin(self.screen_w, self.screen_h, coordinate, values=Price(nom / 100),
                                   number=self.gr_count[idx]))

    def draw(self):
        pygame.draw.rect(Object_display.screen, (50, 205, 50), self.position.to_rectangle())
        for i in self.coins:
            i.draw()

    def resize(self, w, h):
        self.position = self.coordinate * Point((w, h))
        for i in self.coins:
            i.resize(w, h)

    def click(self, event=None, pos=None):
        if event is not None:
            pass
        if pos is not None:
            self.coins.reverse()
            for i in self.coins:
                coin = i.click(pos)
                if coin is not None:
                    self.coins.reverse()
                    return coin
            self.coins.reverse()
