

class Recipe_data:
    def __init__(self, data, id):
        #print(id)
        self.id = id
        self.name = data['name']
        self.difficulty = int(data['difficulty'])
        self.ingredient_number = data['ingredient']
        self.completed = data['completed']
        # self.path = path
        self.ingredient = list()

    def insert_product(self, products):
        for i in self.ingredient_number:
            self.ingredient.append(products[int(i)])

    def display(self):
        print(f"{self.name, self.difficulty}")
        for i in self.ingredient:
            print(f"{i.display()}")
