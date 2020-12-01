import copy
from display_objects.product_image import Product_image


class Product:
    def __init__(self, coordinate, w, h, product):
        self.is_lay = False
        self.product = product
        self.images = []
        self.number = 0
        self.current_image = None
        self.number_products = 0
        for i in range(self.product.number):
            self.images.append(Product_image(copy.deepcopy(coordinate), w, h,
                                             product=product, name=product.name))

    def click(self, pos):
        for i in self.images:
            self.current_image = i.click(pos)
            if self.current_image is not None:
                self.product.is_clicked = True
                return self.current_image

    def resize(self, w, h):
        for i in self.images:
            i.resize(w, h)

    def draw(self):
        for i in self.images:
            i.draw()

    def lay(self):
        if self.current_image.is_lay:
            #sprawdx czy wszystkie
            self.current_image.is_on_counter = True
        else:
            #sprawdz czy wszystkie
            self.current_image.return_to_shelf()
            self.product.is_clicked = False
            self.current_image.is_on_counter = False
