from tinydb import TinyDB


db = TinyDB('data/db.json')
db.drop_tables()
t_product = db.table('Products')
t_product.insert({'name': 'chleb', 'price': 5, 'shelf': 0, 'number': 3})  # 0
t_product.insert({'name': 'bułka', 'price': 0.8, 'shelf': 0, 'number': 5})  # 1
t_product.insert({'name': 'mąka', 'price': 2, 'shelf': 1, 'number': 3})  # 2
t_product.insert({'name': 'jajko', 'price': 0.4, 'shelf': 2, 'number': 6})  # 3
t_product.insert({'name': 'olej', 'price': 3, 'shelf': 5, 'number': 2})  # 4
t_product.insert({'name': 'pomidor', 'price': 2, 'shelf': 6, 'number': 3})  # 5
t_product.insert({'name': 'ogórek', 'price': 1, 'shelf': 6, 'number': 3})  # 6
t_product.insert({'name': 'szczypiorek', 'price': 0.1, 'shelf': 4, 'number': 3})  # 7
t_product.insert({'name': 'sałata', 'price': 0.5, 'shelf': 6, 'number': 3})  # 8
t_product.insert({'name': 'ser', 'price': 4, 'shelf': 3, 'number': 3})  # 9
t_product.insert({'name': 'szynka', 'price': 3.5, 'shelf': 3, 'number': 3})  # 10
t_product.insert({'name': 'mleko', 'price': 3.5, 'shelf': 2, 'number': 3})  # 11
t_product.insert({'name': 'jogurt', 'price': 3.5, 'shelf': 2, 'number': 3})  # 12
t_product.insert({'name': 'kakao', 'price': 3.5, 'shelf': 1, 'number': 3})  # 13
t_product.insert({'name': 'jabłko', 'price': 1.5, 'shelf': 7, 'number': 5})  # 14
t_product.insert({'name': 'truskawka', 'price': 2.2, 'shelf': 7, 'number': 7})  # 15
t_product.insert({'name': 'majonez', 'price': 12, 'shelf': 4, 'number': 2})  # 16
t_product.insert({'name': 'płatki', 'price': 5.3, 'shelf': 3, 'number': 8})  # 17
t_product.insert({'name': 'majonez', 'price': 8, 'shelf': 5, 'number': 2})  # 18
t_product.insert({'name': 'keczup', 'price': 6, 'shelf': 5, 'number': 2})  # 19
t_product.insert({'name': 'banan', 'price': 3, 'shelf': 7, 'number': 4})  # 20
t_product.insert({'name': 'masło', 'price': 3.5, 'shelf': 4, 'number': 3})  # 20
t_product.insert({'name': 'rogal', 'price': 2.5, 'shelf': 0, 'number': 3})  # 21
t_product.insert({'name': 'sok', 'price': 2.5, 'shelf': 1, 'number': 3})  # 22

t_receipe = db.table("Receipe")
t_receipe.insert({"name": 'jajecznica', 'difficulty': 0, 'ingredient': [('chleb', 1), ('ser', 2)],
                  'optional ingredient': [('pomidor', 1), ('ogórek', 1)], 'completed': False})
t_receipe.insert({"name": 'kanapka I', 'difficulty': 0, 'ingredient': [('bułka', 2), ('jajko', 3)],
                  'optional ingredient': [('majonez', 1), ('szczypiorek'), 2], 'completed': False})
t_receipe.insert({"name": 'pasta jajeczna', 'difficulty': 1, 'ingredient': [('jajko', 4), ('majonez', 1)],
                  'optional ingredient': [('ogórek', 2), ('szczypiorek', 4)], 'completed': False})
t_receipe.insert({"name": 'kanapka III', 'difficulty': 2, 'ingredient': [('chleb', 1), ('szynka', 2)],
                  'optional ingredient': [('pomidor', 1), ('jajko', 1), ('majonez', 2), ('ogórek', 2), ], 'completed': False})
t_receipe.insert({"name": 'śniadanie', 'difficulty': 3, 'ingredient': [('chleb', 1), ('sok', 1), ],
                  'optional ingredient': [('jogurt', 1), ('masło', 1), ('szynka', 2), ('ser', 2), ('płatki', 1)], 'completed': False})

db.close()


