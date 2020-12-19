from price import Price
from random import sample


class Recipe_data:
    def __init__(self, data: dict, id: int):
        self.id = id
        self.name = data['name']
        self.difficulty = int(data['difficulty'])
        self.ingredient_number = data['ingredient']
        try:
            self.optional_ingredient_number = data['optional ingredient']
        except:
            self.optional_ingredient_number = None
        self.completed = data['completed']
        self.ingredient = list()
        self.ingredient_completed = None
        self.price = Price()
        self.products = None

    def add_product_to_recipe(self, el: tuple, products: list):

        if type(el[0]) is int:
            idx = el[0]
            self.ingredient.append(products[idx])
            products[idx].set_number_of_ingredient(el[1])
        else:
            try:
                idx = products.index(el[0])
                self.ingredient.append(products[idx])
                products[idx].set_number_of_ingredient(el[1])
            except:
                pass

    def insert_product(self, products: list) -> None:
        self.ingredient.clear()
        self.products = products
        for i in self.ingredient_number:
            self.add_product_to_recipe(i, products)
        if self.optional_ingredient_number is not None:
            x = sample(self.optional_ingredient_number, self.difficulty+1)
            for i in x:
                self.add_product_to_recipe(i, products)

    def display(self) -> str:
        print(f"{self.name, self.difficulty}")
        for i in self.ingredient:
            print(f"{i.display()}")

    def check(self) -> bool:
        for i in self.products:
            if i.is_checked is False:
                self.ingredient_completed = False
                return False
        self.ingredient_completed = True
        return True

    def set_price(self):
        for i in self.ingredient:
            self.price += i.price * i.number_recipe
