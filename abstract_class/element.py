import abc


class Element(abc.ABC):
    data = None

    def __init__(self, price):
        self.is_lay = False
        self.images = []
        self.current_image = None
        self.price = price

    def click(self, pos):
        for i in self.images:
            self.current_image = i.click(pos)
            if self.current_image is not None:
                return self

    def resize(self, w, h):
        for i in self.images:
            i.resize(w, h)

    def draw(self):
        for i in self.images:
            i.draw()

    def check(self) -> bool:
        pass

    def lay(self):
        pass
