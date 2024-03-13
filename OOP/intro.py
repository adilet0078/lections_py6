# ООП - объектно-ориентированное программирование  

# Класс - это описание того, как должен выглядеть объект,то есть  в классе мы описываем какими свойствами(данными) и  поведением(методами)(функциями) должен обладать объект .

# Объект - это сущность, которая находится внутри класса, у объекта есть собсвтенные свойств(данные) и поведение(функции).

# Метод - это функция, которая принадлежит классу (функция внутри класса).

# Атрибут - это данные, принадлежащие обьекту. (обычные переменные внутри класса).
 
# ---------------------------------------------



# class Human:
#     age = 0

#     def __init__(self, first_name, last_name, job, citizenship):
#         self.name = first_name + " " + last_name
#         self.job = job
#         self.citizenship = citizenship

#     def show_info(self):
#         return f'Name: {self.name}\nJob: {self.job}\nCitizenship: {self.citizenship} \nAge: {self.age}'
    

# John = Human('John', 'Doe', 'Engineer', 'USA')

# Anvar = Human('Anvar', 'Abdullayev', 'Developer', 'Kyrgyzstan')


# print(John)
# print(dir(John))
# print(type(John))
# print(John.show_info())

# print(Anvar.show_info())

# John.age = 25
# John.job = 'Programmer'

# print(John.show_info())
 

# ------------------------------------------------
# class Dog:
#     # атрибуты класса 
#     age = 0
#     ushi  = True

#     # методы класса
#     def __init__(self, name: str , color: str) -> None:
#         """ Инициализатор, именно здесь создаются атрибуты обьекта"""
#         #self - ссылка на текущий обьект 
#         self.name = name 
#         self.color = color

#     def bark(self):
#         print(f' {self.name} barks!')

#     def show_info(self):
#         print(f'Name: {self.name} \nColor: {self.color} \nAge: {self.age} \nUshi: {self.ushi}')

# rex = Dog('Rex', 'black')
# pluto = Dog(name='Pluto',color='white')
# aktosh = Dog('Aktosh', 'grey')

# rex.show_info()
# pluto.show_info()
# aktosh.show_info()

# rex.age = 2
# pluto.age = 7 
# aktosh.age = 1 
# aktosh.ushi = False

# rex.show_info()
# pluto.show_info()
# aktosh.show_info()

# rex.bark()
# pluto.bark()
# aktosh.bark()

# class Human:
#     def __init__(self, name):
#         self.name = name
#         self.hunger_level = 0

#     def info(self):
#         print(f"Name: {self.name}, Hunger level: {self.hunger_level}")

#     def eat(self, food):
#         if self.hunger_level > 0:
#             print(f"{self.name} is eating {food}")
#             self.hunger_level -= 1
#         else:
#             print(f"{self.name} is not hungry")

#     def walk(self):
#         print(f"{self.name} is walking")

#     def work(self):
#         print(f"{self.name} is working")

# obj = Human('John')
# obj.info()
# obj.eat('croissant')
# obj.eat('salad')
# obj.info()
# obj.walk()
# obj.work()
# obj.info()
# obj.eat('burger')
# obj.eat('fried potato')
# obj.info()
