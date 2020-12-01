from product import Product


class Recipe_data:
    def __init__(self, data : dict, id: int):
        #print(id)
        self.id = id
        self.name = data['name']
        self.difficulty = int(data['difficulty'])
        self.ingredient_number = data['ingredient']
        #print(type(self.ingredient_number[0]))
        self.completed = data['completed']
        # self.path = path
        self.ingredient = list()

    def insert_product(self, products ) -> None:
        for i in self.ingredient_number:
            products[i[0]].number_recipe = i[1]
            self.ingredient.append(products[i[0]])

    def display(self) -> str:
        print(f"{self.name, self.difficulty}")
        for i in self.ingredient:
            print(f"{i.display()}")
