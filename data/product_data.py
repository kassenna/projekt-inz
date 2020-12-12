# os -> independent    os patch
import copy
from other.price import Price


class Product_data:
    def __init__(self, d: dict):
        self.name = d['name']
        self.price = Price(d['price'])
        self.shelf = d['shelf']
        self.number = d['number']
        self.number_lay = 0
        self.number_recipe = 0
        self.is_clicked = False
        self.is_checked = False

    def __index__(self):
        return self.name

    def copy(self):
        return copy.deepcopy(self)

    def display(self) -> str:
        print(f"{self.name, self.price, self.shelf}")

    def set_number_of_ingredient(self, i):
        if i <= self.number:
            self.number_recipe = i
        else:
            self.number_recipe = self.number

    def checked(self, number):
        self.is_checked = (number == self.number_recipe)

    def __eq__(self, other):
        if self.name == other:
            return True
        return False