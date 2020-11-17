class Coin:
    def __init__(self):
        self.PLN20 = None
        self.PLN10 = None
        self.PLN5 = None
        self.PLN2 = None
        self.PLN1 = None
        self.PLN05 = None
        self.PLN02 = None
        self.PLN01 = None
        self.PLN005 = None
        self.PLN002 = None
        self.PLN001 = None
        self.nominal = [50, 20, 10, 5, 2, 1]
        self.zl_count = []
        self.gr_count = []

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

