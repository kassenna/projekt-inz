import copy

import pygame
from display_objects.coin import Coin
import random
from display_objects.object_display import Object_display
from other.point import Rectangle, Point


class Pocket(Object_display):
    def __init__(self,  w, h, coordinate):
        super().__init__( w, h)
        self.coordinate = Rectangle(coordinate)
        self.position = self.coordinate * Point((w, h))
        self.nominal = [50, 20, 10, 5, 2, 1]
        self.zl_count = []
        self.gr_count = []
        self.coins = []


    def count(self, sum):
        self.price = copy.deepcopy(sum)
        for i in self.nominal:
            print(str(sum))
            zl_temp = sum.zl // i
            gr_temp = sum.gr // i
            self.zl_count.append(zl_temp)
            self.gr_count.append(gr_temp)
            sum.zl -= zl_temp * i
            sum.gr -= gr_temp * i

    def create(self):
        dx = 0.05
        dy = 0.05 * self.screen_w / self.screen_h
        for idx, nom in enumerate(self.nominal):
            for i in range(self.zl_count[idx]):
                p = self.coordinate.size.x * random.random() + self.coordinate.point.x
                q = self.coordinate.size.y * random.random() + self.coordinate.point.x
                self.coins.append(Coin(self.screen_w, self.screen_h, (p, q, p+dx, q+dy), values=(self.nominal, 0),
                                       name=str(self.nominal[idx]) + 'zl.png'))
            for i in range(self.gr_count[idx]):
                p = self.coordinate.size.x * random.random() + self.coordinate.point.x
                q = self.coordinate.size.y * random.random() + self.coordinate.point.x
                self.coins.append(Coin(self.screen_w, self.screen_h, (p, q, p+dx, q+dy), values=(0, self.nominal),
                                       name=str(self.nominal[idx]) + 'gr.png'))

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
            print('click')
            for i in self.coins:
                coin = i.click(pos)
                if coin is not None:
                    return coin

    def move(self, pos):
        for i in self.coins:
           i.move(pos)

