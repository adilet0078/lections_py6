# функция полиморфизм -> len(): len
# print(len('Makers'))
# print(len([1,2,3,4,5]))
# print(len({1:2,3:4,5:6}))

# + (add) - метод
# print(5 + 5)
# print('hello' + 'world')
# print([1,2,3]+[4,5,6])

#  Полиморфизм - способность функции(метода) использоватся для разных типов(классов)
# Широко распрастраненное определение:"один интерфейс - много реализаций"
# list.pop
# set.pop
# dict.pop
 

# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def info(self):
#         print(f"It's a cat. Cat's name is {self.name}, age: {self.age}")

#     def make_sound(self):
#         print("meow, meow!")

# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def info(self):
#         print(f"It's a dog. Dog's name is {self.name}, age: {self.age}")

#     def make_sound(self):
#         print("bark, bark")

# cat = Cat('Garfield', 5)
# dog = Dog('Pluto', 6)

# for obj in (cat, dog):
#     obj.info()
#     obj.make_sound()




# from abc import ABC, abstractmethod
# import math

# class Shape(ABC):
#     def __init__(self, name) -> None:
#         self.name = name

#     @abstractmethod
#     def area(self):
#         pass

#     @abstractmethod
#     def perimeter(self):
#         pass

# class Square(Shape):
#     def __init__(self, length) -> None:
#         super().__init__('Square')
#         self.length = length

#     def area(self):
#         return self.length**2

#     def perimeter(self):
#         return 4 * self.length

#     def fact(self):
#         return "A square has all sides equal and angles equal to 90 degrees"

# class Circle(Shape):
#     def __init__(self, radius) -> None:
#         super().__init__('Circle')
#         self.radius = radius

#     def area(self):
#         return math.pi * self.radius**2

#     def perimeter(self):
#         return 2 * math.pi * self.radius

#     def fact(self):
#         return "A circle has a circumference"

# a = Square(5)
# b = Circle(5)

# print(a.fact())
# print(a.area())
# print(a.perimeter())
# print(b.fact())
# print(b.area())
# print(b.perimeter())