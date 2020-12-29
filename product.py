import copy

from product_data import Product_data
from points import Rectangle, Point
from uml.product_image import Product_image
from element import Element


class Product(Element):
    data = None

    def __init__(self, coordinate: tuple, w: int, h: int, product: Product_data):
        super().__init__(product.price)
        self.product = product
        self.number = product.number_recipe
        c = Rectangle(coordinate)
        for i in range(self.product.number):
            self.images.append(Product_image(copy.deepcopy(c.get_coordinate()), w, h,
                                             product=product, name=product.name))
            c.move(Point((-0.004, -0.008)))

        # self.images.reverse()

    def check(self):
        l = 0
        for i in self.images:
            if i.on_counter is True:
                l += 1
        self.product.checked(l)

    def lay(self):
        self.product.is_clicked = False
        if self.current_image.on_counter is False:
            self.current_image.lay()

        self.current_image = None
        self.check()
