#os -> independent    os patch
import copy

from other.point import Point
from other.price import Price


class Product_data:
    def __init__(self, d : dict):
        self.name = d['name']
        self.price = Price(float(d['price']))
        print(str(self.price))
        self.shelf = int(d['shelf'])
        self.number = int(d['number'])
        self.number_lay = 0
        self.number_recipe = 0
        self.is_clicked = False
        self.is_checked = False


    def copy(self):
        return copy.deepcopy(self)

    def display(self) -> str:
        print(f"{self.name, self.price, self.shelf}")

    def set_number_of_ingredient(self, i):
        if i <= self.number:
            self.number_recipe = i
        else:
            self.number_recipe = self.number

    def checked(self, l):
        self.is_checked = (l == self.number_recipe)



