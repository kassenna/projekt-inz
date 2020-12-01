from data.product_data import Product_data
from data.recipe_data import Recipe_data
from tinydb import TinyDB


class Data:
    def __init__(self, path='data/db.json'):
        self.products = []
        self.recipes = list()
        self.shelves = []
        self.db = TinyDB(path)
        self.__insert_products()
        self.__insert_recipes()
        self.current_recipe = 0

    def __insert_products(self) -> None:
        t_product = self.db.table("Products")
        for p in t_product:
            self.products.append(Product_data(p))

    def __insert_recipes(self):
        t_receipe = self.db.table("Receipe")
        for id, r in enumerate(t_receipe):
            self.recipes.append(Recipe_data(r, id))

    def temp(self) -> str:
        print(self.db.all())

    def display_products(self) -> str:
        for i in self.products:
            i.display()

    def display_recipes(self):
        for i in self.recipes:
            i.display()

    def insert_product_to_receipe(self, id :int) -> None:
        self.recipes[id].insert_product(self.products)
