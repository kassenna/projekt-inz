from product import Product
from receipe_data import Receipe_data
from tinydb import TinyDB, Query

class Data:
    def __init__(self, path='data/db.json'):
        self.products = []
        self.receipes = []
        self.shelves = []
        self.db = TinyDB(path)
        self.__insert_products()
        self.__insert_receipes()

    def __insert_products(self):
        t_product = self.db.table("Products")
        for p in t_product:
            self.products.append(Product(p))

    def __insert_receipes(self):
        t_receipe = self.db.table("Receipe")
        id = 0
        for r in t_receipe:
            self.receipes.append(Receipe_data(r, id))
            id = id+1

    def temp(self):
        print(self.db.all())

    def display_products(self):
        for i in self.products:
            i.display()

    def display_receipes(self):
        for i in self.receipes:
            i.display()

    def insert_product_to_receipe(self, id):
        self.receipes[id].insert_product(self.products)
