#os -> independent    os patch
import copy

from other.point import Point


class Product_data:
    def __init__(self, d : dict):
        self.name = d['name']
        price = float(d['price'])
        self.price = Point((int(price), (int(price*100))%100))
        self.shelf = int(d['shelf'])
        self.number = int(d['number'])
        self.number_recipe = 0
        self.is_clicked = False
        self.is_checked = False

    def copy(self):
        return copy.deepcopy(self)

    def display(self) -> str:
        print(f"{self.name, self.price, self.shelf}")



