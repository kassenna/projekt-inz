from display_objects.coin import Coin
import random


class Pocket:
    def __init__(self):

        self.nominal = [50, 20, 10, 5, 2, 1]
        self.zl_count = []
        self.gr_count = []
        self.coins = []

    def count(self, sum):
        zl = int(sum)
        gr = int((sum - zl) * 100)
        self.zl_count.clear()
        self.gr_count.clear()
        for i in self.nominal:
            zl_temp = zl % i
            gr_temp = gr % i
            self.zl_count.append(zl_temp)
            self.gr_count.append(gr_temp)
            zl = zl - zl_temp * i
            gr = gr - gr_temp * i

    def create(self, screen, w, h, coordinate):
        for idx, nom in enumerate(self.nominal):
            for i in range(self.zl_count[idx]):
                self.coins.append(Coin(screen, w, h, coordinate, values=(self.nominal, 0),
                                       name=str(self.nominal[idx]) + 'zl.png'))
            for i in range(self.gr_count[idx]):
                self.coins.append(Coin(screen, w, h, coordinate, values=(0, self.nominal),
                                       name=str(self.nominal[idx]) + 'gr.png'))

    def draw(self):
        for i in self.coins:
            i.draw()

    def resize(self, w, h):
        for i in self.coins:
            i.resize(w, h)

    def click(self, event=None, pos=None):
        if event is not None:
            pass
        if event is not None:
            print('click')
            for i in self.coins:
                coin = i.click(pos)
                if coin.is_clicked:
                    return coin

    def move(self, pos):
        for i in self.coins:
           i.move(pos)

