import copy
import pygame

from other.price import Price
from payment.coin import Coin
from abstract_class.object_display import Object_display
from other.point import Rectangle, Point


class Pocket(Object_display):
    def __init__(self, w, h, coordinate):
        super().__init__(w, h)
        self.coordinate = Rectangle(coordinate)
        self.position = self.coordinate * Point((w, h))
        self.nominal = [50, 20, 10, 5, 2, 1]
        self.zl_count = []
        self.gr_count = []
        self.coins = []

    def count(self, sum):
        self.price = copy.deepcopy(sum)
        for i in self.nominal:
            zl_temp = sum.zl // i
            gr_temp = sum.gr // i
            self.zl_count.append(zl_temp)
            self.gr_count.append(gr_temp)
            sum.zl -= zl_temp * i
            sum.gr -= gr_temp * i

    def create(self):

        for idx, nom in enumerate(self.nominal):
            self.coins.append(Coin(self.screen_w, self.screen_h, self.coordinate, values=Price(nom),
                                   number=self.zl_count[idx]))
            self.coins.append(Coin(self.screen_w, self.screen_h, self.coordinate, values=Price(nom/100),
                                   number=self.gr_count[idx]))

    def draw(self):
        pygame.draw.rect(Object_display.screen, (50, 205, 50), self.position.rectangle())
        for i in self.coins:
            i.draw()

    def resize(self, w, h):
        for i in self.coins:
            i.resize(w, h)

    def click(self, event=None, pos=None):
        if event is not None:
            pass
        if pos is not None:
            for i in self.coins:
                coin = i.click(pos)
                if coin is not None:
                    return coin


