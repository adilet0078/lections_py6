# magic methods(магические методы)
# dunder methods(double underscore)-> __init__
# служебные методы 

# магия(фишка) заключается в том что эти методы запускаются без прямого обращение к ним ,опредленные методы могут отвечать за определенные операторы

# Магческие методы сравнение

# __eg__(self, other) -> 5==8
                        # 5.__eq__(8)
# __ne__->!=

#__lt__-><

# __gt__ -> >

# __le__ -><=

# print('15'<'ABC')
# class Word(str):
#     def __new__(cls, obj):
#         obj =obj.replace(' ', '')
#         return super().__new__(cls, obj)
    
#     def __init__(self, obj):
#         super().__init__()
#         self.obj = obj 

#     def __gt__(self, other):
#         print('gt worked')
#         print(self, '---', other)
#         if len(self) >len(other):
#             return self
#         elif len(self) <len(other):
#             return other
#         else:
#             return "eq"
        
#     def __lt__(self, other) -> bool:
#         return len(self) < len(other)
    
#     def __eq__(self, other) -> bool:
#         return len(self) == len(other)
    

# obj = Word('     hello john')
# obj2 = Word('cod i   fy')

# print(obj > obj2)
# print(obj < obj2)
# print(obj == obj2)
# ---------------------------------------------------------------
# +-/*//%**

# + -> __add__
# - ->__sub__
# // -> __floordiv__
# / -> __div__(py2) - > __truediv__(py3)
# % -> __mod__
# ** -> __pow__

# class Cifra:
#     def __new__(cls, *args, **kwargs):
#         number = abs(args[0])
#         isinstance = super().__new__(cls)
#         isinstance.number = number
#         return isinstance
    
#     def __add__(self, other):
#         print('add worked')
#         res = self.number + other.number
#         print(f'Result:{self.number} + {other.number} = {res}')
#         return res

# value1 = Cifra(-117)
# value2 = Cifra(53)
# res = value1 + value2
# print(res)
#----------------------------------------------------------------------------------

# from random import choice

# class Dog:
#     def sound(self):
#         print('bark!')

# class Cat :
#     def sound(self):
#         print('meow meow!')

# class Horse:
#     def sound(self):
#         print('igogog')

# class Pet:
#     def __new__(cls):
#         pet = choice([Dog, Cat, Horse])
#         self = super().__new__(pet)
#         print(f'I am {type(self).__name__}')
#         return self
    
#     def __init__(self) -> None:
#         print('pet never was called')

# pet = Pet()
# pet.sound()

# SINGLETON
# class Singleton:
#     _instance = None

#     def __new__(cls):
#         if not cls._instance:
#             cls._instance = super().__new__(cls)
#         return cls._instance
    
#     def __str__(self) -> str:
#         return str(id(self))
    
# a = Singleton()
# b = Singleton()
# print(a, b)
# print(a is b )
# obj = Singleton()
# obj1 = Singleton()
# print(obj, obj1)
# from itertools import repeat
# from random import choice, randint

# class Kopilka:
#     def __init__(self) -> None:
#         self.total = 0
#         self.coins = []

#     def add_coin(self, coin):
#         self.total += coin
#         self.coins.append(coin)

#     def __len__(self):
#         return len(self.coins)

#     def __getitem__(self, index):
#         return self.coins[index]

# obj = Kopilka()  # Instantiate the class
# print(obj.coins)  # Output: []
# print(obj.total)  # Output: 0

# print(len(obj))  # Output: 0
# for _ in repeat(None, randint(89, 156)):  # repeat(None, n) repeats None n times
#     obj.add_coin(choice([1, 3, 5, 10]))

# obj.add_coin(10) 
# obj.add_coin(5)
# obj.add_coin(3)
# obj.add_coin(1)

# print(obj.total)  # Output: Total amount of coins added
# print(obj.coins)  # Output: List of coins added

