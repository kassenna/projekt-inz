import copy
from display_objects.product_image import Product_image


class Product:
    data = None

    def __init__(self, coordinate, w, h, product):
        self.is_lay = False
        self.product = product
        self.images = []
        self.number = product.number_recipe
        self.current_image = None
        self.price = product.price
        for i in range(self.product.number):
            self.images.append(Product_image(copy.deepcopy(coordinate), w, h,
                                             product=product, name=product.name))

    def click(self, pos):
        for i in self.images:
            self.current_image = i.click(pos)
            if self.current_image is not None:
                return self

    def resize(self, w, h):
        for i in self.images:
            i.resize(w, h)

    def draw(self):
        for i in self.images:
            i.draw()

    def check(self):
        l = 0
        for i in self.images:
            if i.is_lay is True:
                l += 1
        self.product.checked(l)
        print(self.product.name +'  '+ str(self.product.is_checked))


    def lay(self):
        self.product.is_clicked = False
        if self.current_image.is_lay:
            self.current_image.is_on_counter = True
        else:
            self.current_image.return_to_shelf()
            self.current_image.is_on_counter = False
            self.current_image.lay()
        self.current_image = None
        self.check()

