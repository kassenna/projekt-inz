import copy


class Price:

    def __init__(self, price: float = 0):
        self.zl = int(price)
        self.gr = int(price * 100) % 100

    def __add__(self, other):
        temp = copy.deepcopy(self)
        temp.gr += other.gr
        a = 0
        if temp.gr >= 100:
            a = temp.gr // 100
            temp.gr = temp.gr % 100
        temp.zl += a + other.zl
        return temp

    def __iadd__(self, other):
        self.gr += other.gr
        a = 0
        if self.gr >= 100:
            a = self.gr // 100
            self.gr = self.gr % 100
        self.zl += other.zl + a
        return self

    def __mul__(self, number: int):
        temp = copy.deepcopy(self)
        temp.gr *= number
        a = 0
        if temp.gr >= 100:
            a = temp.gr // 100
            temp.gr = temp.gr % 100
        temp.zl *= number
        temp.zl += a
        return temp

    def __imul__(self, other):
        self.gr *= other
        a = 0
        if self.gr >= 100:
            a = self.gr // 100
            self.gr = self.gr % 100
        self.zl *= other
        self.zl += a
        return self

    def __str__(self):
        return f"{self.zl} zł  {self.gr} gr "

    def __eq__(self, other):
        return self.zl == other.zl and self.gr == other.gr

    def clear(self):
        self.zl = 0
        self.gr = 0

    def copy(self):
        return copy.copy(self)
