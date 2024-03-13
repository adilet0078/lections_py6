# class Student:
#     univer = 'MIT'

#     def __init__(self, name) -> None:
#         self.name = name
#         self.books = []
#         self.language = {}
#         self.knowledge = 0
#         self.is_ready_work = False

#     def add_points(self, points):
#         self.knowledge += points
#         if self.knowledge > 500 and not self.is_ready_work:
#             self.is_ready_work = True
#             print(f'{self.name} gets 500 points and is ready to work!')

#     def read_book(self, book_name):
#         self.add_points(50)
#         self.books.append(book_name)

#     def do_project(self):
#         self.add_points(100)

#     def learn_lang(self, language, percent):
#         if percent not in range(70, 101):
#             print('Invalid points for language!')
#         else:
#             self.language[language] = percent
#             self.add_points(percent)

# st1 = Student('John Snow')
# st2 = Student('Anvar Abdullayev')

# print(st1.name)
# print(st2.name)

# # print(f'Before study {st1.name}: {st1.books}, {st1.language}, {st1.knowledge}')
# # print(f'Ready to work: {st1.is_ready_work}')

# st1.read_book('Grocam algorithmy')
# st1.read_book('Python')
# st1.read_book('C++')
# st1.read_book('C#')

# st1.do_project()
# st1.do_project()

# st1.learn_lang('Python', 90)
# st1.learn_lang('C++', 80)
# st1.learn_lang('C#', 85)

# st1.do_project()
# print(f'After study {st1.name}: {st1.books}, {st1.language}, {st1.knowledge}')
# print(f'Ready to work: {st1.is_ready_work}')


# class Car :
#     def __init__(self, brand, model) -> None:
#         self.brand = brand
#         self.model = model
#         # self.is_started = False
#         # self.speed = 0

#     def show_info(self):
#         return f'Brand: {self.brand}\nModel: {self.model}' 
    
#     def __str__(self) -> str:
#         return f'Brand: {self.brand}\nModel: {self.model}'
    
# obj = Car('Toyota', 'Corolla')
# print(obj)
# obj2 =  Car('BMW', 'X5')
# print(obj2)

# ---------------------------------------------------------
# class Soda:
#     def __init__(self, ingredient = None) :
#         if isinstance(ingredient, str):
#             self.ingredient = ingredient
#         else:
#             self.ingredient = None

#     def __str__(self) -> str:
#         return'Normal one!' if not self.ingredient else f'gazirovka with {self.ingredient}'
    
# a = Soda('1231')
# b = Soda( True)
# print(a, b)

# dushes = Soda('grusha')
# limonad = Soda('malina')
# print(dushes, limonad) 

# # ---------------------------------------------------------
# import random

# class Sniper:
#     def __init__(self, name) -> None:
#         self.name = name
#         self.health = 100

#     def __str__(self) -> str:
#         return self.name

#     def shoot(self, other):
#         other.health -= 20
#         print(f'attacked {other}')
#         print(f'health of {other.name} is {other.health}')


# sniper1 = Sniper('John')
# sniper2 = Sniper('Anvar')

# while sniper1.health > 0 and sniper2.health > 0:
#     choice = random.randint(0, 1)
#     if choice == 0:
#         sniper1.shoot(sniper2)
#     else:
#         sniper2.shoot(sniper1)
#     print()

# print(f'Winner is {sniper1.name if sniper1.health > 0 else sniper2.name}')