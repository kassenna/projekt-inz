import copy
from shop.product_image import Product_image
from abstract_class.element import Element


class Product(Element):
    data = None

    def __init__(self, coordinate, w, h, product):
        super().__init__(product.price)
        self.product = product
        self.number = product.number_recipe
        for i in range(self.product.number):
            self.images.append(Product_image(copy.deepcopy(coordinate), w, h,
                                             product=product, name=product.name))

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
