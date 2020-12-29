import abc
from pygameAssets import pygameAssets, pygame
from object_display import Object_display
from recipe_data import Recipe_data
from points import Point, Rectangle
from price import Price
from pay import Pay


class Button(Object_display):
    def __init__(self, w: int, h: int, coordinate: Rectangle):
        super().__init__(w, h)
        self.coordinate: Rectangle = coordinate.copy()
        pygameAssets.Button.setScreen(Object_display.screen)

    @abc.abstractmethod
    def draw(self, other=None):
        pass

    def setText(self, text: str):
        self.widget.setText(text)

    def resize(self, w: int, h: int):
        self.rec = self.coordinate.copy() * Point((w, h))
        self.widget = pygameAssets.Button(self.rec.point.x, self.rec.point.y, self.rec.size.x // 2, 40,
                                          color=(0, 200, 0), text='zapłać', textColor=(0, 0, 0),
                                          activeColor=(0, 0, 100), fontSize=40)

    @abc.abstractmethod
    def click(self, event: pygame.event):
        pass


class Button_ok(Button):

    def __init__(self, coordinate: Rectangle, w: int, h: int, receipe: Recipe_data):
        super().__init__(w, h, coordinate)
        self.coordinate.move(Point((self.coordinate.size.x / 2, self.coordinate.size.y - 0.1)))
        self.resize(w, h)
        self.receipe = receipe

    def draw(self, other=None):
        if self.receipe.ingredient_completed:
            self.widget.setColor((0, 200, 0))
        else:
            self.widget.setColor((200, 0, 0))
        self.widget.draw()

    def click(self, event: pygame.event):
        if self.receipe.ingredient_completed:
            if self.widget.isPressed(event):
                Pay(self.screen_w, self.screen_h, self.receipe.price, self.receipe).run()
                return False


class Button_pay(Button):

    def __init__(self, coordinate: Rectangle, w: int, h: int, count: int):
        super().__init__(w, h, coordinate)
        self.lock = True
        self.count = count
        self.resize(w, h)

    def draw(self, price: Price = Price()):
        if self.count == price:
            self.lock = False
            self.widget.setColor((0, 200, 0))
        else:
            self.widget.setColor((200, 0, 0))
        self.widget.draw()

    def click(self, event: pygame.event):
        if self.widget.isPressed(event):
            if self.lock is False:
                return True
        return False
