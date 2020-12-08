from tinydb import TinyDB
db = TinyDB('data/db.json')
db.drop_tables()
t_product = db.table('Products')
t_product.insert({'name': 'chleb', 'price': 5, 'shelf': 0, 'number': 5})    #0
t_product.insert({'name': 'bułka', 'price': 0.8, 'shelf': 0, 'number': 10}) #1
t_product.insert({'name': 'mąka', 'price': 2, 'shelf': 1, 'number': 3})     #2
t_product.insert({'name': 'jajko', 'price': 0.4, 'shelf': 2, 'number': 10}) #3
t_product.insert({'name': 'olej', 'price': 3, 'shelf': 5, 'number': 2})     #4
t_product.insert({'name': 'pomidor', 'price': 2, 'shelf': 6, 'number': 3})  #5
t_product.insert({'name': 'ogórek', 'price': 1, 'shelf': 6, 'number': 3})   #6
t_product.insert({'name': 'szczypiorek', 'price': 0.1, 'shelf': 6, 'number': 3}) #7
t_product.insert({'name': 'sałata', 'price': 0.5, 'shelf': 6, 'number': 3})   #8
t_product.insert({'name': 'ser', 'price': 4, 'shelf': 2, 'number': 3})      #9
t_product.insert({'name': 'szynka', 'price': 3.5, 'shelf': 3, 'number': 3})   #10

t_receipe = db.table("Receipe")
t_receipe.insert({"name": 'jajecznica', 'difficulty': 0, 'ingredient': [(0, 1), (3, 2)],
                  'optional ingredient': [(8, 1), (6, 1)], 'completed': False})
t_receipe.insert({"name": 'kanapka', 'difficulty': 0, 'ingredient': [(0, 1), (10, 1)],
                  'optional ingredient': [(6, 1)], 'completed': False})
t_receipe.insert({"name": 'kanapka', 'difficulty': 1, 'ingredient': [(1, 2), (9, 2)],
                  'optional ingredient': [(8, 2), (6, 1)], 'completed': True})
t_receipe.insert({"name": 'kanapka', 'difficulty': 2, 'ingredient': [(0, 1), (3, 2)], 'completed': False})
db.close()