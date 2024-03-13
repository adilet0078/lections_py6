"""
1) Объявите 3 переменных, запишите в них строку, список и словарь. Затем запишите их в список, и пройдитесь по нему циклом чтобы распечатать длину сразу каждого из объектов.
"""

# a = "string"
# b = [1, 2, 3]
# c = {"key": "value"}
# str = [a, b, c]
# for i in str:
#     print(len(i))

"""
2) Создайте классы Dog и Cat с одинаковым методом voice. Для собак он должен печатать "Гав", для кошек "Мяу".
Объявите для каждого из классов по экземпляру. Затем объявить функцию to_pet(), которая будет принимать животное и вызывать у него метод voice()
# """
# class Dog:
#     def voice(self):
#         print("Гав")

# class Cat:
#     def voice(self):
#         print("Мяу")

# def to_pet(animal):
#     animal.voice()


# dog = Dog()
# cat = Cat()

# to_pet(dog)
# to_pet(cat)


"""
3. Создайте 2 класса: MyInt и MyString, наследуйте MyInt от int, MyString от str. У обоих
классов переопределите метод, который отвечает за работу с оператором “+”.
Напишите функцию add_objects(), которая принимает объект одного из 2 типов.
При сложении объектов класса MyInt должно выдаваться сообщение “Это сложение”, а
потом идти логика сложения 2 чисел, и выдача результата.
При конкатенации объектов класса MyString() Должно выдаваться сообщение: “Это
конкатенация”, а затем логика конкатенации из базового класса и выдача результата.
"""
# class MyInt(int):
#     def __add__(self, other):
#         print("Это сложение")
#         return super().__add__(other)

# class MyString(str):
#     def __add__(self, other):
#         print("Это конкатенация")
#         return super().__add__(other)

# def add_objects(obj1, obj2):
#     if isinstance(obj1, MyInt) and isinstance(obj2, MyInt):
#         return obj1 + obj2
#     elif isinstance(obj1, MyString) and isinstance(obj2, MyString):
#         return obj1 + obj2
#     else:
#         raise TypeError
    

# obj1 = MyInt(5)
# obj2 = MyInt(10)
# result = add_objects(obj1, obj2)
# print(result)
# result1 = add_objects(MyString("Hello, "), MyString("world!"))
# print(result1)


"""
4) Создайте 3 класса: Person, Employee и Student, при этом Employee и Student должны наследоваться от Person. Определите во всех трёх классах метод get_info():
-для класса Person он должен принимать и возвращать следующее: “Привет, меня зовут Иван Петров”.
-для класса Employee он должен принимать и возвращать: “Привет, меня зовут Иван Петров, я работаю в компании “Рога и копыта” на должности “директор”.
-для класса Student должно приниматься и возвращаться: “Привет, меня зовут Иван Петров, я учусь в КГТУ на 3 курсе”.
Определите функцию get_human_info(), которая будет принимать объект одного из трёх классов, вызывать метод get_info и печатать результат.
"""

# class Person:
#     def get_info(self):
#         return "Привет, меня зовут Иван Петров"

# class Employee(Person):
#     def __init__(self, company, position):
#         self.company = company
#         self.position = position

#     def get_info(self):
#         return f"Привет, меня зовут Иван Петров, я работаю в компании {self.company} на должности {self.position}"
    
# class Student(Person):
#     def __init__(self, school, course):
#         self.school = school
#         self.course = course

#     def get_info(self):
#         return f"Привет, меня зовут Иван Петров, я учусь в {self.school} на {self.course} курсе"
    

# object = Employee("Рога и копыта", "директор")

# print(object.get_info())

"""
5) Объявите абстрактный класс геометрических фигур Shape и определите в нём абстрактный метод get_area() для расчёта площади фигуры, которые необходимо переопределить в дочерних классах.

Затем наследуйте от Shape три класса: Triangle, Square и Circle.
-треугольник создаётся с заданными основанием и высотой
-квадрат создаётся с заданной длиной стороны
-круг создаётся с заданным радиусом
Переопределите в каждом из классов метод get_area() таким образом, чтобы он рассчитывал площадь для конкретной фигуры.

Затем создайте от каждого из трёх классов по экземпляру, и вызовите у каждого метод get_area()

Подсказка: для создания абстрактных классов воспользуйтесь модулем abc
# """
# from abc import ABC, abstractmethod
# import math

# class Shape(ABC):
#     @abstractmethod
#     def get_area(self):
#         pass

# class Triangle(Shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height

#     def get_area(self):
#         return 0.5 * self.base * self.height

# class Square(Shape):
#     def __init__(self, side_length):
#         self.side_length = side_length

#     def get_area(self):
#         return self.side_length * self.side_length

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def get_area(self):
#         return math.pi * self.radius * self.radius

# # Создание экземпляров и вызов метода get_area()
# triangle = Triangle(3, 4)
# print(triangle.get_area())

# square = Square(5)
# print(square.get_area())

# circle = Circle(6)
# print(circle.get_area())