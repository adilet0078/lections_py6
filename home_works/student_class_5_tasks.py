# Sanzhar, [2024/2/19 13:53]
# Задание 2: Класс "Студент"

# Задача: Определите класс Студент с атрибутами имя и оценки (список оценок). Добавьте методы для добавления оценки к списку оценок и метод для расчета среднего балла.

# Пример использования:

# студент = Студент("Иван")
# студент.добавить_оценку(5)
# студент.добавить_оценку(4)
# print(студент.расчет_среднего()) -> 4.5


# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.grades = []

#     def add_grade(self, grade):
#         self.grades.append(grade)

#     def calculate_average(self):
#         if len(self.grades) > 0:
#             average_grade = sum(self.grades) / len(self.grades)
#             return average_grade
#         else:
#             return 0

# # Create an instance of the Student class and use the methods
# student = Student("Иван")
# student.add_grade(5)
# student.add_grade(4)
# print(student.calculate_average())  # Output: 4.5



# Sanzhar, [2024/2/19 13:55]
# Задание 1: Класс "Комната" и "Дом"
# Цель: Практика в создании взаимодействующих объектов и управлении ими.

# Задача: Создайте класс Комната с атрибутами название, ширина и длина. Добавьте метод, который вычисляет площадь комнаты. Затем создайте класс Дом, который содержит список комнат. В классе Дом должны быть методы для добавления комнаты и вычисления общей площади дома.


# class Room:
#     def __init__(self, name, width, length):
#         self.name = name
#         self.width = width
#         self.length = length

#     def calculate_area(self):
#         return self.width * self.length

# class House:
#     def __init__(self):
#         self.rooms = []

#     def add_room(self, room):
#         self.rooms.append(room)

#     def calculate_total_area(self):
#         total_area = 0
#         for room in self.rooms:
#             total_area += room.calculate_area()
#         return total_area

# # Create instances of the Room and House classes and use the methods
# room1 = Room("Living Room", 5, 6)
# room2 = Room("Bedroom", 4, 4)

# house = House()
# house.add_room(room1)
# house.add_room(room2)

# print(house.calculate_total_area())  # Output: 46


# Sanzhar, [2024/2/19 13:55]
# Задание 3: Класс "Библиотека" и "Книга"
# Цель: Работа с коллекциями объектов и их методами.

# Задача: Расширьте класс Книга из предыдущего задания, добавив атрибут количество. Создайте класс Библиотека, который будет содержать список книг. В классе Библиотека реализуйте методы для добавления книги (с учетом уже существующих тайтлов), удаления книги по названию, и поиска книг по автору.

# class Book:
#     def __init__(self, title, author, quantity):
#         self.title = title
#         self.author = author
#         self.quantity = quantity

# class Library:
#     def __init__(self):
#         self.books = []

#     def add_book(self, book):
#         for existing_book in self.books:
#             if existing_book.title == book.title:
#                 existing_book.quantity += book.quantity
#                 break
#         else:
#             self.books.append(book)

#     def remove_book(self, title):
#         for book in self.books:
#             if book.title == title:
#                 self.books.remove(book)
#                 break

#     def find_books_by_author(self, author):
#         books_by_author = [book for book in self.books if book.author == author]
#         return books_by_author

# # Create an instance of the Library class and use the methods
# library = Library()
# book1 = Book("Python 101", "John Smith", 5)
# book2 = Book("Web Development", "Emma Johnson", 3)
# book3 = Book("Python 101", "John Smith", 2)

# library.add_book(book1)
# library.add_book(book2)
# library.add_book(book3)
# print([book.title for book in library.books])  # Output: ['Python 101', 'Web Development']

# library.remove_book("Web Development")
# print([book.title for book in library.books])  # Output: ['Python 101']

# print([book.title for book in library.find_books_by_author("John Smith")])  # Output: ['Python 101']



# Sanzhar, [2024/2/19 13:56]
# Задание 4: Класс "Магазин" и "Продукт"
# Цель: Изучение принципов инкапсуляции и взаимодействия объектов.

# Задача: Создайте класс Продукт с атрибутами название, цена и категория. Затем создайте класс Магазин, который будет содержать список продуктов. В Магазине реализуйте методы для добавления продукта, удаления продукта по названию, и метод, который выводит список продуктов определенной категории.


# class Product:
#     def __init__(self, name, price, category):
#         self.name = name
#         self.price = price
#         self.category = category

# class Store:
#     def __init__(self):
#         self.products = []

#     def add_product(self, product):
#         self.products.append(product)

#     def remove_product(self, name):
#         for product in self.products:
#             if product.name == name:
#                 self.products.remove(product)
#                 break

#     def get_products_by_category(self, category):
#         products_by_category = [product for product in self.products if product.category == category]
#         return products_by_category

# # Create an instance of the Store class and use the methods
# store = Store()
# product1 = Product("Laptop", 1000, "Electronics")
# product2 = Product("Headphones", 100, "Electronics")
# product3 = Product("Shirt", 30, "Clothing")

# store.add_product(product1)
# store.add_product(product2)
# store.add_product(product3)

# print([product.name for product in store.products])  # Output: ['Laptop', 'Headphones', 'Shirt']

# store.remove_product("Headphones")
# print([product.name for product in store.products])  # Output: ['Laptop', 'Shirt']

# print([product.name for product in store.get_products_by_category("Electronics")])  # Output: ['Laptop']


# Sanzhar, [2024/2/19 13:56]
# Задание 5: Класс "Пользователь" и "УчетнаяЗапись"
# Цель: Глубокое понимание взаимодействия классов и управления состоянием.

# Задача: Создайте класс Пользователь с атрибутами имя, фамилия и email. Создайте класс УчетнаяЗапись, который будет содержать пользователя, логин, пароль и баланс. В классе УчетнаяЗапись реализуйте методы для изменения пароля, пополнения баланса и совершения платежа, проверяя достаточность средств на балансе.


# class User:
#     def __init__(self, first_name, last_name, email):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = email

# class Account:
#     def __init__(self, user, username, password, balance):
#         self.user = user
#         self.username = username
#         self.password = password
#         self.balance = balance

#     def change_password(self, new_password):
#         self.password = new_password

#     def deposit(self, amount):
#         self.balance += amount

#     def withdraw(self, amount):
#         if self.balance >= amount:
#             self.balance -= amount
#             return True
#         else:
#             return False

# # Create an instance of the User and Account classes and use the methods
# user = User("John", "Doe", "johndoe@example.com")
# account = Account(user, "johndoe", "password123", 1000)

# account.change_password("newpassword123")
# print(account.password)  # Output: 'newpassword123'

# account.deposit(500)
# print(account.balance)  # Output: 1500

# payment_success = account.withdraw(700)
# print(payment_success, account.balance)  # Output: True, 800