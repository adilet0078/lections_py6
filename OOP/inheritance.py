# принципы ООП:

# 1. Наследование 
# 2. Инкапсуляция
# 3. Полиморфизм

# 4. Абстракция 
# 5. Композиция
# 6. Агрегация
# -----------------------------------------------------


# Наследование позваляет принимать родительские методы и атрибуты в дочерние классы 

# Родительские класс 
# Дочерние класс
# -----------------------------------------------------


# class Animal:
#     def print_info(self):
#         print('I am an Animal') 

# class Lion(Animal):
#     pass

# class Dog(Animal):
#     pass


# lion = Lion()
# lion.print_info()

# dog = Dog()
# dog.print_info()
# print(dir(Lion))


# -----------------------------------------------------

# class Animal:
#     def say(self):
#         print(f'This animal\'s name is {self.name} : {self.voice}')

#     def eat(self):
#         print(f'{self.name} eats {self.food}')


# class Lion(Animal):
#     name = 'lion'
#     voice = 'roar'
#     food = 'meat'
#     griva = True

#     def info(self):
#         print(f'Name: {self.name}\nVoice: {self.voice}\nFood: {self.food}\nGriva: {self.griva}')

# class Dog(Animal):
#     name = 'dog'
#     voice = 'woof'
#     food = 'meat'
#     griva = False

#     def info(self):
#         print(f'Name: {self.name}\nVoice: {self.voice}\nFood: {self.food}\nGriva: {self.griva}')

# class Koala(Animal):
#     name = 'koala'
#     voice = 'hiss'
#     food = 'grass'
#     griva = False

#     def info(self):
#         print(f'Name: {self.name}\nVoice: {self.voice}\nFood: {self.food}\nGriva: {self.griva}')

# rex = Dog()
# simba = Lion()
# julian = Koala()

# rex.say()
# rex.eat()
# rex.info()

# simba.say()
# simba.eat()
# simba.info()

# julian.say()
# julian.eat()
# julian.info()


# -----------------------------------------------------
 
# class Person:
#     def info(self):
#         print('I\'m a person from Bishkek')

# class Student(Person):
#     def info(self):
#         super().info()
#         print('I\'m study at Manas University')

# obj = Student()
# obj.info()

# -----------------------------------------------------
# class Laptop:
#     def __init__(self, brand, model, price) -> None:
#         self.brand = brand
#         self.model = model
#         self.price = price

#     def get_info(self):
#         return f'Brand: {self.brand}, Model: {self.model}, Price: {self.price}'


# class Acer(Laptop):
#     def __init__(self, model, price, cpu, ram, year):
#         super().__init__('Acer', model, price)
#         self.year = year
#         self.cpu = cpu
#         self.ram = ram

#     def get_info(self):
#         return f'{super().get_info()}, Year: {self.year}, CPU: {self.cpu}, RAM: {self.ram}'


# class Apple(Laptop):
#     def __init__(self, model, price, cpu, ram, year, display):
#         super().__init__('Macbook', model, price)
#         self.display = display
#         self.year = year
#         self.cpu = cpu
#         self.ram = ram

#     def get_info(self):
#         return f'{super().get_info()}, Year: {self.year}, CPU: {self.cpu}, RAM: {self.ram}, Display: {self.display}'

# mac = Apple('M1', 1000, 'M1', 8, 2021, '13"')
# print(mac.get_info())

# acer = Acer('Aspire', 1000, 'i5', 8, 2021)
# print(acer.get_info())
