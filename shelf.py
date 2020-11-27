import copy

from display_objects.object_display import Object_display
from display_objects.product_image import Product_image
from display_objects.shelf_image import Shelf_image
from other.point import Rectangle, Point


class Shelf(Object_display):
    def __init__(self, id, x, y, xmax, ymax, screen, screen_width, screen_height):
        super().__init__(screen, screen_width, screen_height)
        self.is_clicked = False
        self.id = id
        self.rectangle = Rectangle(x, y, xmax, ymax)
        self.image = Shelf_image(x, y, xmax, ymax, screen_width, screen_height, screen)
        self.product = []
        self.nmbr_product = 0
        self.product_start = copy.deepcopy(self.rectangle)
        self.product_start.setsize(self.product_start.size.x/5, self.product_start.size.x/5 * screen_width/screen_height)
        self.product_start.move(Point((self.product_start.size.x*0.3, -self.product_start.size.y * 0.5)))
    def draw(self):
        self.image.draw()
        for i in self.product:
            i.draw()

    def add_product(self, product):
        if self.nmbr_product > 9:
            return
        self.product.append(
            Product_image(copy.deepcopy(self.product_start.get_coordinate()), self.screen, self.screen_w, self.screen_h, product, name=product.name))
        self.product_start.move(Point((self.product_start.size.x*0.8, 0)))
        self.nmbr_product += 1

    def resize(self, w, h):
        self.image.resize(w, h)
        for i in self.product:
            i.resize(w, h)

    def click(self, pos):
        for i in self.product:
            product = i.click(pos)
            if product is not None:
                self.is_clicked = True
                return product
        self.is_clicked = False
