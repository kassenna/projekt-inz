import random
from payment.coin_image import Coin_image
from abstract_class.element import Element


class Coin(Element):
    data = None

    def __init__(self, w, h, coordinate, values=None, number=0):
        super().__init__(values)
        if values is not None:
            self.coordinate = coordinate
            self.w = w
            self.h = h
            dx = 0.05
            dy = 0.05 * w / h
            if self.price.zl != 0:
                name = str(self.price.zl) + 'zl.png'
            elif self.price.gr != 0:
                name = str(self.price.gr) + 'gr.png'
            extra = random.randint(0, 5) - 3
            if extra < 0:
                extra = 0
            for i in range(number+extra):
                p = self.coordinate.size.x * random.random() + self.coordinate.point.x
                q = self.coordinate.size.y * random.random() + self.coordinate.point.y
                self.images.append(Coin_image(self.w, self.h, (p, q, p + dx, q + dy), values, name=name))

