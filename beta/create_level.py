import pygame_menu
from tinydb import TinyDB, Query

from screen import Screen


class CreateLevel:

    def __init__(self, path):
        self.db = TinyDB(path)
        self.products = list()
        self.optional_products = list()
        self.dif = 0
        self.v1 = 0
        self.v2 = 0
        self.n = 'test'
        pass

    def name(self, value):
        self.n = value

    def difficult(self, value, v):
        self.dif = v

    def value1(self, value):
        self.v1 = value

    def value2(self, value):
        self.v2 = value

    def product1(self, value, number):
        self.p1 = value
        self.n1 = number

    def product2(self, value, number):
        self.p2 = value
        self.n2 = number

    def add(self):
        table = self.db.table('Products')
        q = Query()
        product = table.search(q.name == self.p1[0])
        print(type(product))
        if self.n1 > self.v1:
            self.products.append((self.p1[0], self.n1))
        else:
            self.products.append((self.p1[0], self.v1))

    def add_optional(self):
        table = self.db.table('Products')
        q = Query()
        product = table.search(q.name == self.p2[0])
        if self.n2 > self.v2:
            self.optional_products.append((self.p2[0], self.n2))
        else:
            self.optional_products.append((self.p2[0], self.v2))

    def add_recipe(self):
        if len(self.optional_products) > self.dif:
            table = self.db.table('Recipes')

            table.insert({"name": self.n, 'difficulty': self.dif, 'ingredient': self.products,
                          'optional ingredient': self.optional_products, 'completed': False})

    def run(self, window, data):
        menu = pygame_menu.Menu(Screen.get_size()[1], Screen.get_size()[0], 'menu', theme=pygame_menu.themes.THEME_BLUE)
        menu.add_text_input("Nazwa:", onchange=self.name)
        menu.add_selector('Trudność', [('łatwy', 0), ('średni', 1), ('trudny', 2)], onchange=self.difficult)
        menu.add_vertical_margin(40)
        self.p1 = data.products_list[0]
        menu.add_selector("wybierz produkt", data.products_list, onchange=self.product1)
        menu.add_text_input("wpisz liczbę", onchange=self.value1, input_type='__pygame_menu_input_int__')
        menu.add_button('dodaj', self.add)
        menu.add_vertical_margin(40)
        self.p2 = data.products_list[0]
        menu.add_selector("wybierz produkt opcjonalny", data.products_list, onchange=self.product2)
        menu.add_text_input("wpisz liczbę", onchange=self.value2, input_type='__pygame_menu_input_int__')
        menu.add_button('Dodaj', self.add_optional)
        menu.add_vertical_margin(40)
        menu.add_button('dodaj przepis', self.add_recipe)
        menu.mainloop(window)
