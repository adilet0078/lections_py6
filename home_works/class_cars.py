
# Created: 2024-01-08 10:00
# Deadline: 2024-02-20 18:00
# Max score: 100

# Автомобиль: создайте класс с именем Car. Метод __init__ () класса Car должен содержать три атрибута: brand, year и color. Создайте метод get_auto(), который выводит информацию об автомобиле, и метод get_year, который выводит возраст авто .

# Добавьте атрибут horsepower, который равен 85.

# Напишите метод add_horsepower, который всем машинам будет добавлять по 20 л/с, а машинам Mers, Bmw, Poshe по 40 л/с

# Создайте на основе своего класса экземпляр с именем bmw . Выведите три атрибута по отдельности, затем вызовите все методы.

# Два авто: начните с класса из вышеописанного упражнения. Создайте 2 разных экземпляра, вызовите для каждого экземпляра метод get_auto

# Студенты: создайте класс с именем Student. Создайте атрибуты name, age, course. Напишите метод get_student(), который выводит сводку с информацией о студенте . Создайте еще один метод get_birth_year() для вывода информации о годе рождения студента.

# Создайте несколько экземпляров, представляющих разных студентов. Вызовите оба метода для каждого студента.

# class Car:
#     def __init__(self, brand, year, color):
#         self.brand = brand
#         self.year = year
#         self.color = color
#         self.horsepower = 85

#     def get_auto(self):
#         print(f"Brand: {self.brand}, Year: {self.year}, Color: {self.color}, Horsepower: {self.horsepower}")

#     def get_year(self):
#         current_year = 2023  # Assuming the current year is 2023
#         age = current_year - self.year
#         print(f"The car is {age} years old")

#     def add_horsepower(self):
#         if self.brand.lower() in ["mers", "bmw", "poshe"]:
#             self.horsepower += 40
#         else:
#             self.horsepower += 20

# # Create an instance of the Car class named bmw
# bmw = Car("BMW", 2018, "Black")

# # Display individual attributes
# print(f"Brand: {bmw.brand}")
# print(f"Year: {bmw.year}")
# print(f"Color: {bmw.color}")

# # Call all methods
# bmw.get_auto()
# bmw.get_year()
# bmw.add_horsepower()
# bmw.get_auto()