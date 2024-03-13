# Для ПО кондитерской фабрики нужно написать родительский класс Candy (Конфеты). Этот класс имеет атрибуты name, price, weight (наименование, цена, вес). Подклассы Chocolate, Gummy, HardCandy (шоколад, жевательный мармелад, леденец) наследуют все атрибуты суперкласса Candy. Кроме того, у них есть и свои атрибуты:

# Chocolate – cocoa_percentage (процент содержания какао) и chocolate_type (сорт шоколада).
# Gummy – flavor и shape (вкус и форма).
# HardCandy – flavor и filled (вкус и начинка).
# class Candy:
#     def __init__(self, name, price, weight):
#         self.name = name
#         self.price = price
#         self.weight = weight

# class Chocolate(Candy):
#     def __init__(self, name, price, weight, cocoa_percentage, chocolate_type):
#         super().__init__(name, price, weight)
#         self.cocoa_percentage = cocoa_percentage
#         self.chocolate_type = chocolate_type

# class Gummy(Candy):
#     def __init__(self, name, price, weight, flavor, shape):
#         super().__init__(name, price, weight)
#         self.flavor = flavor
#         self.shape = shape

# class HardCandy(Candy):
#     def __init__(self, name, price, weight, flavor, filled):
#         super().__init__(name, price, weight)
#         self.flavor = flavor
#         self.filled = filled

# # Пример использования:
# chocolate_bar = Chocolate("Dark Chocolate", 2.50, 100, 70, "Dark")
# print(chocolate_bar.name)  # Output: Dark Chocolate
# print(chocolate_bar.cocoa_percentage)  # Output: 70

# gummy_bear = Gummy("Gummy Bear", 1.00, 50, "Fruit", "Bear")
# print(gummy_bear.name)  # Output: Gummy Bear
# print(gummy_bear.shape)  # Output: Bear

# hard_candy = HardCandy("Filled Candy", 0.75, 25, "Mint", True)
# print(hard_candy.name)  # Output: Filled Candy
# print(hard_candy.filled)  # Output: True



# Задание 7
# Напишите класс Animal, обладающий свойствами name, species, legs, в которых хранятся данные о кличке, виде и количестве ног животного. Класс также должен иметь два метода – voice() и move(), которые сообщают о том, что животное подает голос и двигается.

# Создайте два подкласса – Dog и Bird. Подкласс Dog имеет атрибут breed (порода) и метод bark(), который сообщает о том, что собака лает. Подкласс Bird обладает свойством wingspan (размах крыльев) и методом fly(), который уведомляет о полете птицы.

# class Animal:
#     def __init__(self, name, species, legs):
#         self.name = name
#         self.species = species
#         self.legs = legs

#     def voice(self):
#         print('voice')

#     def move(self):
#         print('moving')

# class Dog(Animal):
#     def __init__(self, name, species, legs, breed):
#         super().__init__(name, species, legs)
#         self.breed = breed

#     def bark(self):
#         print('barking')

# class Bird(Animal):
#     def __init__(self, name, species, legs, wingspan):
#         super().__init__(name, species, legs)
#         self.wingspan = wingspan

#     def fly(self):
#         print('flying')

# # Создание объекта класса Dog
# dog = Dog(name="Buddy", species="Canine", legs=4, breed="Golden Retriever")

# # Создание объекта класса Bird
# bird = Bird(name="Sparrow", species="Aves", legs=2, wingspan=20)

# # Проверка атрибутов созданных объектов
# print("Dog:")
# print("Name:", dog.name)
# print("Species:", dog.species)
# print("Legs:", dog.legs)
# print("Breed:", dog.breed)
# print()

# print("Bird:")
# print("Name:", bird.name)
# print("Species:", bird.species)
# print("Legs:", bird.legs)
# print("Wingspan:", bird.wingspan)


# class Animal:
#     def __init__(self, name, species, legs):
#         self.name = name
#         self.species = species
#         self.legs = legs

#     def voice(self):
#         print(f"{self.species} {self.name} makes a sound.")

#     def move(self):
#         print(f"{self.species} {self.name} is moving.")


# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name, species="Dog", legs=4)
#         self.breed = breed

#     def bark(self):
#         print(f"{self.species} {self.name} (breed: {self.breed}) barks.")


# class Bird(Animal):
#     def __init__(self, name, wingspan):
#         super().__init__(name, species="Bird", legs=2)
#         self.wingspan = wingspan

#     def fly(self):
#         print(f"{self.species} {self.name} with wingspan {self.wingspan} is flying.")


# # Пример использования классов:

# # Создаем объекты
# dog = Dog(name="Buddy", breed="Labrador Retriever")
# bird = Bird(name="Sparrow", wingspan=30)

# # Вызываем методы
# dog.voice()  # Output: Dog Buddy makes a sound.
# dog.move()   # Output: Dog Buddy is moving.
# dog.bark()   # Output: Dog Buddy (breed: Labrador Retriever) barks.

# bird.voice() # Output: Bird Sparrow makes a sound.
# bird.move()  # Output: Bird Sparrow is moving.
# bird.fly()   # Output: Bird Sparrow with wingspan 30 is flying.


# Task: Bank Account Management System

# You are required to create a simple bank account management system using Python classes. The system should have the following functionalities:

#     Account Creation: Users should be able to create a new bank account with a unique account number, holder's name, and initial balance.

#     Deposit: Account holders should be able to deposit money into their accounts.

#     Withdrawal: Account holders should be able to withdraw money from their accounts. However, they should not be able to withdraw more than their current balance.

#     Balance Inquiry: Users should be able to check their current balance.

# Each account should have the following attributes:

#     Account Number (unique)
#     Holder's Name
#     Current Balance

# Additionally, the system should handle the following constraints:

#     The account number should be generated automatically and should be unique for each account.
#     Users should not be able to deposit or withdraw negative amounts.

# Implement the system using Python classes (BankAccount, SavingsAccount, etc.) and demonstrate its functionality with sample usage scenarios.

# This task not only requires you to design and implement classes for managing bank accounts but also involves handling constraints and implementing various functionalities using methods within those classes. It's a practical exercise that combines OOP concepts with real-world scenarios.

# Класс Vector3D 
# Экземляр класса задается тройкой координат в трехмерном пространстве (x,y,z). 
# Обязательно должны быть реализованы методы:  
# – сложение векторов оператором + (метод add), 
# – вычитание векторов оператором - (метод sub), 
# – скалярное произведение оператором * (метод mul), 
# – умножение на скаляр оператором * (метод mul), 
# – векторное произведение оператором @ (метод matmul). 
# Пример  
# v1 = Vector3D(4, 1, 2) 
# v1.display() 
# v2 = Vector3D() 
# v2.read() 
# v3 = Vector3D(1, 2, 3)


# class Vector3D:
#     def __init__(self, x=0, y=0, z=0):
#         self.x = x
#         self.y = y
#         self.z = z

#     def add(self, other):
#         return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

#     def sub(self, other):
#         return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

#     def mul(self, other):
#         if isinstance(other, Vector3D):
#             # Scalar product
#             return self.x * other.x + self.y * other.y + self.z * other.z
#         else:
#             # Multiplication by scalar
#             return Vector3D(self.x * other, self.y * other, self.z * other)

#     def matmul(self, other):
#         return Vector3D(self.y * other.z - self.z * other.y,
#                         self.z * other.x - self.x * other.z,
#                         self.x * other.y - self.y * other.x)

#     def display(self):
#         print(f"({self.x}, {self.y}, {self.z})")

#     def read(self):
#         self.x = int(input("Enter x coordinate: "))
#         self.y = int(input("Enter y coordinate: "))
#         self.z = int(input("Enter z coordinate: "))

# # Пример использования
# v1 = Vector3D(4, 1, 2)
# print("v1:")
# v1.display()

# v2 = Vector3D()
# print("v2:")
# v2.read()

# v3 = Vector3D(1, 2, 3)


# class Vector3D:

#     def __init__(self, x=0, y=0, z=0):
#         self.x = x
#         self.y = y
#         self.z = z

#     def add(self, other):
#         return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

#     def sub(self, other):
#         return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

#     def mul(self, other):
#         if isinstance(other, Vector3D):
#             return self.x * other.x + self.y * other.y + self.z * other.z
#         else:
#             return Vector3D(self.x * other, self.y * other, self.z * other)

#     def matmul(self, other):
#         return Vector3D(self.y * other.z - self.z * other.y,
#                         self.z * other.x - self.x * other.z,
#                         self.x * other.y - self.y * other.x)

#     def display(self):
#         print(f"({self.x}, {self.y}, {self.z})")

#     def read(self):
#         self.x = float(input("Введите координату x: "))
#         self.y = float(input("Введите координату y: "))
#         self.z = float(input("Введите координату z: "))

# v1 = Vector3D(4, 1, 2)
# print("v1:")
# v1.display()

# v2 = Vector3D()
# print("v2:")
# v2.read()

# v3 = Vector3D(1, 2, 3)

# Задача: Система Управления Банковскими Счетами

# Вам необходимо создать простую систему управления банковскими счетами с использованием классов Python. Система должна иметь следующие функциональные возможности:

# Создание счета: пользователи должны иметь возможность создать новый банковский счет с уникальным номером счета, именем владельца и начальным балансом.

# Депозит: владельцы счетов должны иметь возможность вносить деньги на свои счета.

# Вывод средств: владельцы счетов должны иметь возможность снимать деньги со своих счетов. Однако они не должны иметь возможности снять больше, чем их текущий баланс.

# Запрос баланса: пользователи должны иметь возможность проверить свой текущий баланс.

# Каждая учетная запись должна иметь следующие атрибуты:

# Номер счета (уникальный)
# Имя владельца
# Текущий Баланс

# Кроме того, система должна обрабатывать следующие ограничения:

# Номер счета должен быть сгенерирован автоматически и должен быть уникальным для каждого счета.
# Пользователи не должны иметь возможности вносить или снимать отрицательные суммы.

# Реализовать систему с помощью классов Python (BankAccount, SavingsAccount и т.д.) и продемонстрировать ее функциональность на примерах сценариев использования.

# Эта задача не только требует разработки и реализации классов для управления банковскими счетами, но и включает в себя обработку ограничений и реализацию различных функциональных возможностей с использованием методов внутри этих классов. Это практическое упражнение, которое сочетает в себе концепции ООП с реальными сценариями.