import copy


class Point:
    def __init__(self, point: tuple):
        self.x = point[0]
        self.y = point[1]

    def __eq__(self, point):
        return (self.x == point.x) and (self.y == point.y)

    def __gt__(self, point):
        return (self.x > point.x) and (self.y > point.y)

    def __lt__(self, point):
        return (self.x < point.x) and (self.y < point.y)

    def __mul__(self, point):
        return Point((self.x * point.x, self.y * point.y))

    def __imul__(self, point):
        self.x *= point.x
        self.y *= point.y
        return self

    def __add__(self, point):
        x = self.x + point.x
        y = self.y + point.y
        return Point((x, y))

    def __iadd__(self, point):
        self.x += point.x
        self.y += point.y
        return self

    def __sub__(self, point):
        x = self.x - point.x
        y = self.y - point.y
        return Point((x, y))

    def __isub__(self, point):
        self.x -= point.x
        self.y -= point.y
        return self

    def to_int(self):
        return (int(self.x), int(self.y))


class Rectangle:
    def __init__(self, coordinate: tuple):
        self.point = Point((coordinate[0], coordinate[1]))
        self.end_coordinate = Point((coordinate[2], coordinate[3]))
        self.size = self.end_coordinate - self.point

    def __mul__(self, point: Point):
        p = copy.deepcopy(self)
        p.point *= point
        p.end_coordinate *= point
        p.size = p.end_coordinate - p.point
        return p

    def __imul__(self, point: Point):
        self.point *= point
        self.end_coordinate *= point
        self.size = self.end_coordinate - self.point
        return self

    def scale(self, point: Point):
        self.point += point
        self.end_coordinate -= point
        self.size = self.end_coordinate - self.point

    def move(self, point: Point):
        self.point += Point((point.x, point.y))
        self.end_coordinate += Point((point.x, point.y))

    def get_coordinate(self):
        return self.point.x, self.point.y, self.end_coordinate.x, self.end_coordinate.y

    def to_rectangle(self):
        return list((self.point.x, self.point.y, self.size.x, self.size.y))

    def is_in_area(self, point: Point):
        return self.point < point < self.end_coordinate

    def __getitem__(self, idx: int):
        return self.to_rectangle()[idx]

    def setsize(self, x: int or float, y: int or float):
        self.size = Point((x, y))
        self.end_coordinate = self.point + self.size
