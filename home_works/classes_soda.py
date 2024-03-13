# Анвар, [2024/2/19 13:16]
# # Создайте класс Soda принимающий 1 аргумент при инициализации (отвечающий за добавку к выбираемому лимонаду).
# # В этом классе реализуйте метод show_my_drink(), выводящий на печать «Газировка и {ДОБАВКА}» в случае наличия добавки, а иначе отобразится следующая фраза: «Обычная газировка».

# class Soda:
#     def __init__(self, addon=None):
#         self.addon = addon

#     def show_my_drink(self):
#         if self.addon:
#             print(f"Газировка и {self.addon}")
#         else:
#             print("Обычная газировка")

# # Create an instance of the Soda class
# my_soda = Soda("вишневый сироп")  # Instantiate with an addon

# # Call the show_my_drink method to display the drink information
# my_soda.show_my_drink()


# # Создайте класс Student. При создании его экземпляра, мы должны записать имя и фамилию студента в соответствующие переменные объекта. В классе должны быть:
# #  1 переменная объекта books = [ ]
# #  2 переменная объекта “knowledge” со значением по умолчанию 0
# #  3 метод read_book, который принимает название книги, добавляет книгу в books, добавляет 100 баллов в knowledge
# #  4 метод do_homework, который при вызове добавляет 10 баллов в knowledge
# #  5 Создайте экземпляры, вызовите методы.

# class Student:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.books = []
#         self.knowledge = 0

#     def read_book(self, book_title):
#         self.books.append(book_title)
#         self.knowledge += 100

#     def do_homework(self):
#         self.knowledge += 10

# # Create instances of the Student class and call the methods
# student1 = Student("John", "Doe")
# student1.read_book("Mathematics")
# student1.do_homework()

# student2 = Student("Alice", "Smith")
# student2.read_book("History")
# student2.do_homework()

# # Display the state of the instances
# print(f"{student1.first_name} {student1.last_name} has gained {student1.knowledge} knowledge points and read the books: {student1.books}")
# print(f"{student2.first_name} {student2.last_name} has gained {student2.knowledge} knowledge points and read the books: {student2.books}")

# Анвар, [2024/2/19 13:18]
# 6. Создайте класс имеющий атрибут "дата рождения" и автоматически просчитываемый возраст по входящей дате рождения. Используйте модуль time/datetime

# import datetime

# class Person:
#     def __init__(self, birthdate):
#         self.birthdate = birthdate

#     @property
#     def age(self):
#         today = datetime.date.today()
#         birthdate = datetime.datetime.strptime(self.birthdate, "%Y-%m-%d").date()
#         age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
#         return age

# # Create an instance of the Person class and get the age
# person = Person("1990-05-15")  # Assuming the birthdate is "1990-05-15"
# print(f"The person's age is: {person.age}")