import copy
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

    def __lt__(self, point):
        if self.x < point.x:
            if self.y < point.y:
                return True
        return False

    def __imul__(self, point):
        self.x = self.x * point.x
        self.y = self.y * point.y

    def __mul__(self, point):
        return Point((self.x * point.x, self.y * point.y))

    def move(self, x, y):
        self.x = self.x + x
        self.y = self.y + y

    def __add__(self, point):
        x = self.x + point.x
        y = self.y + point.y
        return Point((x, y))

    def __iadd__(self, point):
        self.x += point.x
        self.y += point.y

    def __sub__(self, point):
        x = self.x - point.x
        y = self.y - point.y
        return Point((x, y))

    def to_tuple(self):
        return (int(self.x), int(self.y))


class Rectangle:
    def __init__(self, coordinate):
        self.point = Point((coordinate[0],coordinate[1]))
        self.end_coordinate = Point((coordinate[2], coordinate[3]))
        self.size = self.end_coordinate - self.point

    def __mul__(self, point: Point):
        p = copy.deepcopy(self)
        p.point = p.point * point
        p.end_coordinate = p.end_coordinate * point
        p.size = p.end_coordinate - p.point
        return p

    def __imul__(self, point: Point):
        self.point *= point
        self.end_coordinate *= point
        self.size = self.end_coordinate - self.point

    def resize(self, x, y):
        self.size = self.size * Point((x, y))
        self.end_coordinate = self.point + self.size

    def scale(self, dx, dy):
        self.point.move(dx, dy)
        self.end_coordinate.move(-dx, -dy)
        self.size = self.end_coordinate - self.point

    def move(self, point):
        self.point.move(point.x, point.y)
        self.end_coordinate.move(point.x, point.y)

    def get_coordinate(self):
        return self.point.x, self.point.y, self.end_coordinate.x, self.end_coordinate.y

    def rectangle(self):
        return list((self.point.x, self.point.y, self.size.x, self.size.y))

    def is_in_area(self, point):
        if self.point < point < self.end_coordinate:
            return True
        return False

    def __getitem__(self, item):
        return self.get_coordinate()[item]

    def setsize(self, x, y):
        self.size = Point((x, y))
        self.end_coordinate = self.point + self.size


class Parallelogram:
    def __init__(self, x, y, xmax, ymax, angle):
        self.angle = angle
        self.tan = numpy.math.tan(numpy.math.radians(self.angle))
        self.temp = (ymax - y) / self.tan
        self.points = Rectangle(x, y, xmax, ymax)
        self.parrallelogram = numpy.array(
            [Point((x, y)), Point((xmax, y)), Point((xmax + self.temp, ymax)), Point((x + self.temp, ymax))])

    def __index__(self, i):
        return self.parrallelogram[i]

    def move(self, dx, dy):
        for i in self.parrallelogram:
            i.move(dx, dy)

    def polygon(self):
        ret = []
        for i in self.parrallelogram:
            ret.append(i.to_tuple())
        return ret

    def multiply(self, w, h):
        self.points = self.points * Point((w, h))
        position = copy.deepcopy(self.parrallelogram)
        for i in self.parrallelogram:
            i *= Point((w, h))
        self.temp = (position[3].y - position[0].y) / self.tan
