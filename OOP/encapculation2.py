# Аннотация свойств (@property(getter setter))


# class Person:
#     __name = 'John'
#     __age = 22 
#     @property
#     def name(self):
#         """The name property"""
#         print(self.__name)

#     @name.setter
#     def name (self, value):
#         if not isinstance(value, str):
#             print('invalid value for name')
#         else:
#             print(f'new name: {value}')
#             self.__name = value
#     @property
#     def age(self):
#         print(self.__age)

#     @age.setter
#     def age(self, value):
#         if not isinstance(value, int) or value not in range(0, 150):
#             print('invalid value for age')
#         else:
#             print(f'new age: {value}')
#             self.__age = value

# obj = Person()
# obj.name
# obj.name = 'Jane'
# obj.name
# obj.age 
# obj.age = 25
# obj.age
# obj.age = 200
# obj.age = 'dlkf'
# obj.age = -12
# obj.age
# -------------------------------------------------------------

# read , write, delete

# class Circle:
#     def __init__(self, radius) -> None:
#         self.__radius = radius

#     def _get_radius(self):
#         print("getter, _get_radius")
#         return self.__radius
    
#     def _set_radius(self, value):
#         print("setter, _set_radius")
#         if not isinstance(value, (int, float)):
#             print('radius must me an u=int or float object')
#         else:
#             self.__radius = value
    
#     def delete_radius(self):
#         print("deleter, delete_radius")
#         answer = input('Are you sure?(yes/no)')
#         if answer.lower().strip() == 'yes':
#             del self.__radius
#             print('radius deleted')
#         else:
#             print('radius not deleted')

#     radius = property(fget=_get_radius, fset=_set_radius)

# obj = Circle(5)
# print(obj.radius)
# obj.radius = 10
# print(obj.radius)
# obj.delete_radius()
# print(obj.radius)
# -------------------------------------------------------------

# class CoordinateWriteError(Exception):
#     pass
# class Point:
#     def __init__(self, x, y) -> None:
#         self.x = x
#         self.y = y

#     @property
#     def x(self):
#         print(self.__x)

#     @property
#     def y(self):
#         print(self.__y)

#     @x.setter
#     def x(self, value):
#         raise CoordinateWriteError ('x-coordinate is read only')

#     @y.setter
#     def y(self, value):
#         raise CoordinateWriteError ('y-coordinate is read only')
    
# obj = Point(1, 2)
# obj.x
# obj.y
# obj.x = 10
# obj.y = 20

# write only

# import hashlib
# import os

# class User:
#     def __init__(self, username, password):
#         self.username = username
#         self.__password = self._hash_password(password)

#     def _hash_password(self, password):
#         salt = os.urandom(32)
#         return hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000), salt

#     @property
#     def password(self):
#         raise AttributeError('password is write only')

#     @password.setter
#     def password(self, value):
#         if not isinstance(value, str) or len(value) < 8:
#             print('Invalid value for password')
#         else:
#             self.__password = self._hash_password(value)

# john = User('johnsnow', 'secret')
# # print(john.password)

# john.password = 'secret123'
# print(john._User__password)
