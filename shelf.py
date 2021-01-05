from object_display import Object_display
from product_data import Product_data
from shelf_image import Shelf_image
from points import Rectangle, Point
from product import Product


class Shelf(Object_display):
    def __init__(self, id: int, coordinate: tuple, screen_w: int, screen_h: int):
        super().__init__(screen_w, screen_h)
        self.id = id
        self.rectangle = Rectangle(coordinate)
        self.image = Shelf_image(coordinate, screen_w, screen_h)
        self.product = []
        self.nmbr_product = 0
        self.product_start = self.rectangle.copy()
        self.product_start.setsize(self.product_start.size.x / 5, self.product_start.size.x / 5 * screen_w / screen_h)
        self.product_start.move(Point((self.product_start.size.x * 0.8, -self.product_start.size.y * 0.56)))

    def draw(self):
        self.image.draw()
        for i in self.product:
            i.draw()

    def add_product(self, product: Product_data):
        if self.nmbr_product > 3:
            return
        p = Product(self.product_start.get_coordinate(), self.screen_w, self.screen_h, product)
        p.check()
        self.product.append(p)
        self.product_start.move(Point((self.product_start.size.x * 1.3, 0)))
        self.nmbr_product += 1

    def resize(self, w:int, h:int):
        self.image.resize(w, h)
        for i in self.product:
            i.resize(w, h)

    def click(self, pos:tuple):
        for i in self.product:
            product = i.click(pos)
            if product is not None:
                self.is_clicked = True
                return product
        self.is_clicked = False
