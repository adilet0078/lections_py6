# class Employee:
#     bonus = 1.5

#     def __init__(self, first_name, last_name, salary):
#         self.name = f'{first_name} {last_name}'
#         self.salary = salary

#     def get_info(self):
#         return f'FIO: {self.name}\nSalary: {self.salary}'

#     def increase_salary(self):
#         self.salary *= self.bonus

#     def __str__(self):
#         return self.get_info()


# class Manager(Employee):
#     def __init__(self, first_name, last_name, salary, devs=None):
#         super().__init__(first_name, last_name, salary)
#         self.devs = devs if devs is not None else []

#     def add_dev(self, developer):
#         self.devs.append(developer)

#     def show_devs(self):
#         return [x.get_info() for x in self.devs]


# class Developer(Employee):
#     def __init__(self, first_name, last_name, salary, language):
#         super().__init__(first_name, last_name, salary)
#         self.language = language

#     def get_info(self):
#         info = super().get_info()
#         info += f'\n Programming language: {self.language}'
#         return info


# dev1 = Developer('John', 'Doe', 1000, 'Python')
# dev2 = Developer('Jane', 'Doe', 2000, 'Java')
# dev3 = Developer('Anvar', 'Abdullayev', 3000, 'C++')
# dev4 = Developer('Anar', 'Abdullayev', 4000, 'C#')

# man1 = Manager('James', 'Doe', 5000, [dev1, dev2])
# man2 = Manager('William', 'Doe', 6000)

# man1.add_dev(dev3)
# man1.add_dev(dev4)
# man2.add_dev(dev3)
# man2.add_dev(dev4)

# dev3.increase_salary()
# dev4.increase_salary()
# man2.increase_salary()

# print(f'Manager {man1} has {man1.show_devs()} developers')
# print(f'Manager {man2} has {man2.show_devs()} developers')

# ------------------------------------------------
# множественное наследование - это когда класс наследуется от двух или более классов


# class Avto:
#     def play_music_at_station(self):
#         print('Music is playing...')

#     def ride (self):
#         print('Riding...')
# class Plane: 
#     def play_music_at_station(self):
#         print('Listening ED Sheeran!')

#     def fly(self):
#         print(' We are flying...')

# class FutureAvto(Plane, Avto):
#     pass

# obj = FutureAvto()
# obj.ride()
# obj.fly()
# obj.play_music_at_station()
# obj.play_music_at_station()

# ------------------------------------------------
# Проблема ромба - когда поиск шел в родительский класс и прежде чем искать у соседнего общего потомка (решена с помощью MRO)

# MRO - Method Resolution Order - механизм для корректного поиска родительских методов . Был создан для решение проблемы ромба, которая появилась в object в Python. Поиск идет таким образом что если у родительских классов есть общий предок, то идет поиск в ширину (MRO).
  
# class Zero:
#     def say(self):
#         print('class Zero')

# class Fisrt(Zero):
#     def say(self):
#         print('class Fisrt')
# class Second(Zero):
#     def say(self):
#         print('class Second')

# class MyClass(Fisrt, Second):
#     def say(self):
#         super().say()
#         print('MyClass')

# obj = MyClass()
# obj.say()
# print(MyClass.mro()) #MyClass.mro