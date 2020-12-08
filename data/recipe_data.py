from other.price import Price
from random import sample, randint


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

    def insert_product(self, products) -> None:
        self.ingredient.clear()
        self.products = products
        for i in self.ingredient_number:
            self.ingredient.append(products[i[0]])
            products[i[0]].set_number_of_ingredient(i[1])
        if self.optional_ingredient_number is not None:
            x = sample(self.optional_ingredient_number,
                       randint(self.difficulty, len(self.optional_ingredient_number)))
            for i in x:
                products[i[0]].set_number_of_ingredient(i[1])
                self.ingredient.append(products[i[0]])

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
