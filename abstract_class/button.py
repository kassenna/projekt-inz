import abc
import copy
from pygameAssets import pygameAssets, pygame
from abstract_class.object_display import Object_display
from other.point import Point
from payment.pay import Pay


class Button(Object_display):
    def __init__(self, w, h, coordinate):
        super().__init__(w, h)
        self.coordinate = copy.deepcopy(coordinate)
        pygameAssets.Button.setScreen(Object_display.screen)

    @abc.abstractmethod
    def draw(self):
        pass

    @abc.abstractmethod
    def resize(self, w: int, h: int):
        pass

    @abc.abstractmethod
    def click(self, event: pygame.event):
        pass


class Button_ok(Button):

    def __init__(self, coordinate, w, h, receipe):
        super().__init__(w, h, coordinate)
        self.coordinate.move(Point((self.coordinate.size.x / 2, self.coordinate.size.y - 0.1)))
        self.resize(w, h)
        self.receipe = receipe

    def draw(self):
        if self.receipe.ingredient_completed:
            self.widget.setColor((0, 200, 0))
        else:
            self.widget.setColor((200, 0, 0))
        self.widget.draw()

    def resize(self, w: int, h: int):
        self.rec = copy.copy(self.coordinate) * Point((w, h))
        self.widget = pygameAssets.Button(self.rec.point.x, self.rec.point.y, self.rec.size.x // 2, 40,
                                          color=(0, 200, 0), text='zapłać', textColor=(0, 0, 0),
                                          activeColor=(0, 0, 100), fontSize=40)

    def click(self, event: pygame.event):
        # if self.receipe.ingredient_completed:
        if self.widget.isPressed(event):
            Pay(self.screen_w, self.screen_h, self.receipe.price).run()


class Button_pay(Button):

    def __init__(self, coordinate, w, h, counter, count):
        super().__init__(w, h, coordinate)
        self.count = count
        self.resize(w, h)

    def draw(self, price):
        print(str(self.count) + ' ' + str(price))
        if self.count == price:
            print(True)
            self.widget.setColor((0, 200, 0))
        else:
            print(False)
            self.widget.setColor((200, 0, 0))
        self.widget.draw()

    def resize(self, w: int, h: int):
        self.rec = copy.copy(self.coordinate) * Point((w, h))
        self.widget = pygameAssets.Button(self.rec.point.x, self.rec.point.y, self.rec.size.x // 2, 40,
                                          color=(0, 200, 0), text='zapłać', textColor=(0, 0, 0),
                                          activeColor=(0, 0, 100), fontSize=40)

    def click(self, event: pygame.event):
        # if self.receipe.ingredient_completed:
        if self.widget.isPressed(event):
            if self.count == self.counter.price:
                print('zaplacono')
