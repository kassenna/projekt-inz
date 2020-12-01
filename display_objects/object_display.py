import abc


class Object_display(abc.ABC):
    screen = None
    data = None

    def __init__(self, w: int, h: int):
        self.screen_w = w
        self.screen_h = h

    @abc.abstractmethod
    def draw(self):
        pass

    @abc.abstractmethod
    def resize(self, w: int, h: int):
        pass

    def move(self, pos: tuple):
        pass
