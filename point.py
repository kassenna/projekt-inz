import numpy
class Point:
    def __init__(self, point):
        self.x = point[0]
        self.y = point[1]

    def __eq__(self, point):
        if self.x == point.x:
            if self.y == self.y:
                return True
        return False

    def __gt__(self, point):
        if self.x > point.x:
            if self.y > point.y:
                return True
        return False
    def __mul__(self, point):
        self.x = self.x * point.x
        self.y = self.y * point.y
    def move(self, x, y):
        self.x = self.x + x
        self.y = self.y + y
    def __add__(self, point):
        x = self.x + point.x
        y = self.y + point.y
        return Point(x, y)

    def __sub__(self, point):
        x = self.x - point.x
        y = self.y - point.y
        return Point((x, y))
    def to_tuple(self):
        return (int(self.x), int(self.y))

class Rectangle:
    def __init__(self,x, y, xend, yend):
        self.point = Point((x, y))
        self.end_coordinate = Point((xend, yend))
        self.size = Point((xend-x, yend-y))
    def __mul__(self, point ):
        self.point * point
        self.end_coordinate * point
        self.size = self.end_coordinate - self.point
    def resize(self, dx, dy):
        self.point.move(dx, dy)
        self.end_coordinate.move(-dx, -dy)
        self.size = self.end_coordinate - self.point
    def move(self, point):
        self.point.move(point.x, point.y)
        self.end_coordinate.move(point.x, point.y)

    def rectangle(self):
        return int(self.point.x), int(self.point.y), int(self.size.x), int(self.size.y)

    def __eq__(self, point):
        if point > self.point and self.end_coordinate > point:

            return True
        return False
class Parallelogram:
    def __init__(self, x, y, xmax, ymax, angle):
        temp = (xmax - y) / numpy.math.tan(numpy.math.radians(angle))
        self.points = Rectangle(x, y, xmax, ymax)
        self.angle = angle
        self.parrallelogram= numpy.array([Point((x, y)), Point((xmax, y)), Point((xmax + temp, ymax)), Point((x + temp, ymax))])
    def move(self, dx, dy):
        for i in self.parrallelogram:
            i.move(dx, dy)
    def polygon(self):
        ret = []
        for i in self.parrallelogram:
            ret.append(i.to_tuple())
        return ret
