import abc
class Object_display(abc.ABC):
    def __init__(self, screen, w, h):
        self.screen = screen
        self.screen_w = w
        self.screen_h = h
    @abc.abstractmethod
    def draw(self):
        pass

    @abc.abstractmethod
    def resize(self, w, h):
        pass

    def move(self, pos):
        pass
