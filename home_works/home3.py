# task 1 
# ) Проверить введенное пользователем число и если оно больше 5 то вывести “True”, иначе “False”.

# num = int(input('enter your number'))
# if num > 5:
#     print(True)
# else:
#     print(False)

# task 2 
#  Проверить введенные пользователем данные и если длина строки больше или равна 5 символам вывести “True” иначе “False”.

# string = (input('enter your string'))

# if len(string) >= 5:
#     print(True)
# else:
#     print(False)
 
# task 3 
# Проверить введенное пользователем значение если оно больше или равно 90, вывести “Отлично ваша оценка 5”, если значение больше или равно 80, вывести “Здорово ваша оценка 4”, если значение больше или равно 70, вывести , если значение больше или равно 60, вывести “Вам стоит подучить материал", в других случаях “вы не сдали экзамен”.


# string = (input('enter your string'))
# if len(string) >= 90:
#     print('Отлично ваша оценка 5')
# elif len(string) >= 80:
#         print('Здорово ваша оценка 4')
# elif len(string) >= 70:
#     print('Хорошо ваша оценка 3')
# elif len(string) >= 60:
#     print("Вам стоит подучить материал")
# else:
#     print('вы не сдали экзамен')
                        
#  task 4 Проверить введенное пользователем число если оно отрицательное то вывести “negative”, если положительное то “positive”, если оно равно 0 то вывести “Zero”

# user_num = float (input('enter your number'))
# if user_num < 0: 
#     print('negative')
# elif user_num > 0:
#     print('positive')
# elif user_num == 0:
#     print('zero')  
                  
# task 5  Даны два целых числа. Выведите значение наименьшего из них.
# a = int(input ('enter your number'))
# b = int(input ('enter your number'))
# min_num = min(a, b)
# print(min_num)

# task 6 
# # Даны три целых числа. Выведите значение наименьшего из них.
# num1 = int(input('enter your number'))
# num2 = int(input('enter your number'))
# num3 = int(input('enter your number'))
# min_num = min(num1, num2, num3 )
# print(min_num)

# task 7 
#  Даны три целых числа. Определите, сколько среди них совпадающих. Программа должна вывести одно из чисел: 3 (если все совпадают), 2 (если два совпадает) или 0 (если все числа различны).

# x=input('enter an integer:') 
# y=input('enter an integer:') 
# z=input('enter an integer:') 
# if x==y==z :
#     print(3)
# elif x==y or y==z or z==x:
#     print(2)
# else:
#     print(0)

# task 8 
# Вводятся два целых числа. Проверить делится ли первое на второе. Вывести на экран сообщение об этом, частное (в любом случае), а также остаток от деления (если он есть). input: 678 23 
# output: 678 не делится на 23 
# Частное: 29 
# Остаток: 11

# from tabnanny import check


# def find(n , m):
#     x = n//m
#     y = n%m
#     return x , y 
# print(find(int(input('enter your niumber')), int(input('enter your niumber'))))
 # task 9 
#   Дано номер года. Требуется определить, является ли год с данным номером високосным. Если год является високосным, то выведите YES, иначе выведите NO. Напомним, что в соответствии с григорианским календарем, год является високосным, если его номер кратен 4, но не кратен 100, а также если он кратен 400.

# year = int(input('enter the year'))
# if year %4 == 0 and year % 100 != 0 or  year % 400 == 0 :
#     print('leap year')
# else:
#     print('not leap year')

# task 10 
#   Перевести число, введенное пользователем, в байты или килобайты в зависимости от его выбора.

# number = float(input("Enter a number: "))
# result = number * 1024 
# print(result)


# Task 11 Создайте список при помощи встроенной функции.
# ls = ('Hello world!')


# # task 12 
#  Дан список list_ = [66.25, 333, 27.5, 86, 3.1432, 1546.89, 333, ]. Посчитайте сколько раз встречается (333), (3.1432) и ('n').
# ls = [66.25, 333, 27.5, 86, 3.1432, 1546.89, 333, ]
# # ls.count =(333 and 3.1432 or ()'n')
# c_333 = ls.count(333)
# c3_14 = ls.count(3.1432)
# n = ls.count('n')
# print(c_333, c3_14, n )


# task 13

#  Дан список list_ = [66.25, 333, 27.5, 86, 3.1432, 1546.89, 333, ]. Узнайте под каким индексом лежит (86) и удалите (1546.89).
# list_ = [66.25, 333, 27.5, 86, 3.1432, 1546.89, 333]

# index_86 = list_.index(86)
# list_.remove(1546.89)
# print(f"The index of (86) is: {index_86}")
# print(f"The list after deleting (1546.89): {list_}")
 
# task 14 
# Дан список list_ = [66.25, 333, 27.5, 86, 3.1432, 1546.89, 333, ]. Сперва отсортируйте его по возрастанию, а затем переверните его.

# list_ = [66.25, 333, 27.5, 86, 3.1432, 1546.89, 333]
# list_.sort()
# list_.reverse()
# print("Sorted and reversed list:", list_)

# task 15 Создайте два списка, и расширьте список тремя разными путями.
# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']
# combined_list1 = list1 + list2

# list1.extend(list2)

# combined_list3 = list(list1) + list(list2)
# list1.append(list2)
# print("List 1:", list1)
# print("List 2:", list2)
# print("Combined List 1 (concatenation):", combined_list1)
# print("List 1 after extending with List 2:", list1)
# print("List 1 after appending List 2:", list1)
# print("List 2:", list2)

# task 16 Создайте кортеж только с одним элементом и выведите его тип данных.
# my_tuple = (42,)
# print(type(my_tuple))

# task 17 Создайте кортеж при помощи встроенной функции.
# my_tuple = tuple([1, 2, 3, 4, 5])
# print(my_tuple)

#  task 18 ан кортеж tuple_ = ('a', 1, 'Hello', True, ['1', 'b']). Возвратите новый кортеж удалив слово 'Hello'.
# tuple_ = ('a', 1, 'Hello', True, ['1', 'b'])

# # Create a new tuple without the element 'Hello'
# new_tuple = tuple(item for item in tuple_ if item != 'Hello')

# print(new_tuple)
# tuple_ = ('b', 1, 'Hello', True, ['False', 'b'], None, ('tuple'))

# # Create a new tuple with elements at even indexes
# new_tuple = tuple_[::2]

# print(new_tuple)