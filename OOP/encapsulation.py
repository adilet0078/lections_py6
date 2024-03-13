#  Инкапсулация:
# 1. Языковая конструкция, которая помогает связвть данные с методами для их обработки и управление(связь между данными и методами которые упарвляют ими)(класс-капсула)

# 2. Механизм скрытия, при помощи которого можно орграничить доступ одного компонента программы к другому

# # Инкапсуляция как связь
# class Phone:
#     number = "+996555555555"
#     def print_number(self):
#         print(f'My number: {self.number}')
#         print(f'My number {Phone.number}')
    
# my_phone = Phone()
# my_phone.print_number()

# Инкапсуляция как механизм сокрытия
# 3 уровня сокрытие данных в питоне 
#       1. Публичный(public)-  number, print_number
#       2. Приватный(_private)- _number
#       3. Защищенный(__protected)- __number

# class Car:
#     _country = 'Germany'
#     __motor = 'V8'

#     def __init__(self) -> None:
#         self.marka = 'BMW'         # public
#         self._model = 'X5'         # protected
#         self.__color = 'Black'     # private

# object = Car()
# print(dir(object))
# print(object.marka)
# print(object._model, object._country)
# print(object._Car__color, object._Car__motor)

# class Phone:
#     username = "John"
#     _caller = 'Jamie'
#     __count_of_calls = 17
#     def call(self):
#         print(f'{self._caller} звонить нам !')
#         quesation = input(' Взять трубку да\нет:')
#         if quesation.lower().strip() == 'да':
#             print('Трубка взята')
#             self.__turn_on()
#         else:
#             print('Трубка не взята')

#     def __turn_on(self):
#         print('hello!')
#         print(f'count of calls with {self._caller}: {self.__count_of_calls}')

#     def __increment_calls(self):
#         self.__count_of_calls += 1

# john = Phone()
# print(john.username)
# john.call
# john.call
# john.call
# john.call

# class Person: 
#     def __init__(self, name, surname, age) -> None:
#         self.name = name
#         self.surname = surname
#         self.age = age

#     def display_info(self):
#         print(f'Name: {self.name} \nSurname: {self.surname} \nAge: {self.age}')


# obj = Person('John', 'Doe', 25)
# obj.display_info()
# obj.name = [1,2,3, 4]
# obj.age = '-25'
# obj.display_info()

# getter & setter
# они нужны чтобы избежать прямого обращения к атрибутам
# при этом можно добавить логику валидация(проверки) данных которые будут установлены в атрибуты

# class Person:
#     def __init__(self, name, surname, age) -> None:
#         self.__name = name
#         self.__surname = surname
#         self.__age = age

#     def display_info(self):
#         print(f'Name: {self.__name} \nSurname: {self.__surname} \nAge: {self.__age}')

#     # Getter
#     def get_name(self):
#         return self.__name

#     def get_age(self):
#         return self.__age

#     # Setter
#     def set_name(self, name):
#         if not isinstance(name, str):
#             print('Некорректное имя')
#         else:
#             self.__name = name

#     def set_age(self, age):
#         if not isinstance(age, int) or not 0 <= age <= 150:
#             print('Некорректный возраст')
#         else:
#             self.__age = age

# # Creating an object
# obj = Person('John', 'Doe', 25)
# obj.display_info()  # Displaying initial info
# obj.set_name('Jane')  # Setting new name
# obj.set_age(30)  # Setting new age
# obj.display_info()  # Displaying updated info
