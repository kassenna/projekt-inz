#os -> independent    os patch
import copy


class Product:
    def __init__(self, d):
        self.name = d['name']
        self.price = d['price']
        self.shelf = d['shelf']
        #self.path = 'data/graphic/' + self.name
        self.is_clicked = False
        self.is_checked = False
    def copy(self, point):
        product = copy.deepcopy(self)
        return product
    def display(self):
        print(f"{self.name, self.price, self.shelf}")



