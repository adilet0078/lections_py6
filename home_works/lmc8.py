# Задание 1.
# Есть список list_1 = [5.97, 6, "tom", 3.14, "bob", "alice", 5, -35, "nursultan", 42, "ulukbek", "edil", 91, "nurlan", 1.5, 27.9]
#      Написать функцию которая будет принимать этот список в качестве аргумента. Далее функция должна ВЕРНУТЬ список состоящий из имен(строковых значений) и чтобы эти имена были с заглавной буквы и в алфавитном порядке
#     Написать функцию которая будет принимать этот список в качестве аргумента. Далее функция должна ВЫВЕСТИ НА КОНСОЛЬ список из целочисленных значений в отсортированном виде но в обратном порядке, т.е от большого к маленькому
#     Написать функцию которая будет принимать этот список в качестве аргумента. Далее функция должна ВЕРНУТЬ сложение всех чисел с плавающей точкой


# def extract_and_format_names(input_list):
#     names = [item for item in input_list if isinstance(item, str)]
#     formatted_names = [name.title() for name in names]
#     formatted_names.sort()
#     return formatted_names

# list_1 = [5.97, 6, "tom", 3.14, "bob", "alice", 5, -35, "nursultan", 42, "ulukbek", "edil", 91, "nurlan", 1.5, 27.9]
# result = extract_and_format_names(list_1)
# print(result)



# def output_sorted_reverse_integers(input_list):
#     integers = [item for item in input_list if isinstance(item, int)]
#     integers.sort(reverse=True)
#     print(integers)

# list_1 = [5.97, 6, "tom", 3.14, "bob", "alice", 5, -35, "nursultan", 42, "ulukbek", "edil", 91, "nurlan", 1.5, 27.9]
# output_sorted_reverse_integers(list_1)



# def sum_floats(input_list):
#     float_numbers = [item for item in input_list if isinstance(item, float)]
#     return sum(float_numbers)

# list_1 = [5.97, 6, "tom", 3.14, "bob", "alice", 5, -35, "nursultan", 42, "ulukbek", "edil", 91, "nurlan", 1.5, 27.9]
# result = sum_floats(list_1)
# print(result)

# Задание 2.
# Сэндвичи: напишите функцию, которая получает первым аргументом размер сэндвича в виде строкового значения и список компонентов сэндвича.

# При вызове функции, функция должна выводить описание заказанного сэндвича например «Большой сэндвич со следующими ингредиентами: огурец, колбаса … » . Вызовите функцию три раза с разными количествами аргументов и разными размерами (Большой, средний, маленький)


# def make_sandwich(size, components):
#     size_description = ""
#     if size.lower() == "большой":
#         size_description = "Большой сэндвич"
#     elif size.lower() == "средний":
#         size_description = "Средний сэндвич"
#     elif size.lower() == "маленький":
#         size_description = "Маленький сэндвич"
#     else:
#         size_description = "Сэндвич"

#     components_description = ", ".join(components)
#     print(f"{size_description} со следующими ингредиентами: {components_description}")

# make_sandwich("большой", ["огурец", "колбаса", "сыр", "томат"])
# make_sandwich("средний", ["ветчина", "сыр", "листья салата", "горчица"])
# make_sandwich("маленький", ["тунец", "майонез", "огурец", "помидор"])



# Задание 3.
# Напишите функцию для сохранения информации об автомобиле в словаре . Функция всегда должна возвращать производителя и название модели, но при этом она может получать произвольное количество именованных аргументов . Вызовите функцию с передачей обязательной информации и еще двух пар «имя—значение» (например, цвет и комплектация) . Ваша функция должна работать для вызовов следующего вида: car = make_car(‘subaru’, ‘outback’, colour=’blue’, engine='V8') и возвращать строку" Subaru Outback colour is blue, engine is V8

# def descripition_the_car():
#     dict_ = { 
#         'brand': 'subaru',
#         'model': 'outback',
#         'colour': 'blue',
#         'engine': 'V8'
#     }
 
#     for key, value in dict_.items():
#         print(f"{key} is {value}")
#     return dict_

# result = descripition_the_car()
# print(result)


 

# Задача 4

# Напишите функцию count_letters, которая принимает на вход текст и подсчитывает, какое в нём количество цифр и букв. Функция должна вывести на экран информацию о найденных буквах и цифрах в определённом формате.

# Реализовать в цикле while, для выхода пользователь должен ввести "выход"

# Пример:

# Введите текст: 100 лет в обед

# Какую цифру ищем? 0

# Какую букву ищем? л

# Количество цифр 0: 2

# Количество букв л: 1


# def count_letters(text):
#     while True:
#         letter = input("Какую букву ищем? ") 
#         if letter == "выход":
#             break
#         count = 0
#         for i in text:
#             if i == letter:
#                 count += 1
#         print(f"Количество букв {letter}: {count}") 


# text = "100 лет в обед"
# count_letters(text)

# Задача 5.

# Напишите функцию, которая в виде аргумента принимает словарь (данные с именами и должностями , где ключ это имя работника,  а значение его должность. Функция должна вернуть предложения, типа:  
# Работник Асан, занимает должность Директор

# def dict_info(dict_):
#     for key, value in dict_.items():
#         print(f"Работник {key}, занимает должность {value}")

# dict_ = {
#     "Асан": "Директор",
#     "Асанов": "Менеджер",
#     "Асанова": "Бухгалтер"
#  }

# dict_info(dict_)
 

# Задача 6 (дополнительно)

# Напишите программу, которая будет суммировать все числа, введенные пользователем, игнорируя при этом нечисловой ввод. Выводите на экран текущую сумму чисел после каждого очередного ввода. Ввод пользователем значения, не являющегося числовым, должен приводить к появлению соответствующего предупреждения, после чего пользователю должно быть предложено ввести следующее число. Выход из программы будет осуществляться путем пропуска ввода. Удостоверьтесь, что ваша программа корректно обрабатывает целочисленные значения и числа с плавающей запятой. 

# Пример:

# Введите число: 1

# Сумма: 1

# Введите число: 2

# Сумма: 3

# Введите число: 5

# Сумма: 8

# Введите число: кукарача

# Ошибка, введите только числа

# Введите число: 12

# Сумма: 20 (т.е. сумма не обнуляется, а продолжает "считать" (8 + 12 = 20)

# def sum_numbers():
#     sum = 0
#     while True:
#         number = input("Введите число: ")
#         if number == "выход":
#             break
#         elif number.isdigit():
#             sum += int(number)
#             print(f"Сумма: {sum}")
#         else:
#             print("Ошибка, введите только числа")

# sum_numbers()

# 1) '''Напишите функцию, принимающую на вход длины двух катетов прямо-
# угольного треугольника и возвращающую длину гипотенузы, рассчитан-
# ную по теореме Пифагора. В главной программе должен осуществляться
# запрос длин сторон у пользователя, вызов функции и вывод на экран
# полученного результата.'''

# a = int(input('введите длину стороны a: '))
# b = int(input('введите длину стороны b: '))
  

# def pifagor_teorem(a, b):
 
#     c = (a**2 + b**2)**0.5
#     return c



# print(pifagor_teorem(a, b))




# 2) '''Представьте, что сумма за пользование услугами такси складывается из
# базового тарифа в размере $4,00 плюс $0,25 за каждые 140 м поездки.
# Напишите функцию, принимающую в качестве единственного параметра
# расстояние поездки в километрах и возвращающую итоговую сумму опла-
# ты такси. В основной программе должен демонстрироваться результат
# вызова функции.'''

# def path_cost(km):

#  cost = 4.00 + 0.25 * (km // 140)
#  return cost


# print(path_cost(140000))




# #

# 3) '''Интернет-магазин предоставляет услугу экспресс-доставки для части
# своих товаров по цене $10,95 за первый товар в заказе и $2,95 – за все
# последующие. Напишите функцию, принимающую в качестве единствен-
# ного параметра количество товаров в заказе и возвращающую общую
# сумму доставки. В основной программе должны производиться запрос
# количест­ва позиций в заказе у пользователя и отображаться на экране
# сумма доставки.'''


# def delivery_cost(count):

#     if count == 1:
#         cost = 10.95
#     else:
#         cost = 10.95 + 2.95 * (count - 1)
#     return cost

# print(delivery_cost(int(input("Количество позиций в заказе: "))))

# #

# 4) '''Напишите функцию, которая будет принимать на вход три числа в качест­
# ве параметров и возвращать их медиану. В основной программе должен
# производиться запрос к пользователю на предмет ввода трех чисел, а так-
# же вызов функции и отображение результата.'''

# def mediana(a, b, c):

#     numbers = [a, b, c]
#     numbers.sort()
#     return numbers[1]

# print(mediana(int(input("Первое число: ")), int(input("Второе число: ")), int(input("Третье число: "))))



# #

# 5) '''Используя решения из упражнений 100 и 102, напишите программу, ге-
# нерирующую случайный надежный пароль и выводящую его на экран.
# Посчитайте, с какого раза удастся создать пароль, отвечающий нашим
# требованиям надежности, и выведите на экран количество попыток. Им-
# портируйте функции из предыдущих упражнений и вызывайте их при
# необходимости для решения этой задачи.'''

# import random
# import string
# import math

# def random_password(length):
#     # Define the characters that can be used in the password
#     characters = string.ascii_letters + string.digits + string.punctuation
#     password = ''.join(random.choice(characters) for _ in range(length))   
#     return password


# print(random_password(8))


# import random
# import string

# def generate_password(length=12):
#     characters = string.ascii_letters + string.digits + string.punctuation
#     password = ''.join(random.choice(characters) for _ in range(length))
#     return password

# def check_password_strength(password):
#     # Функция из упражнения 100 для проверки надежности пароля
#     # Здесь можно вставить код из упражнения 100

#     return True  # Возвращаем True, если пароль удовлетворяет требованиям надежности

# def main():
#     attempts = 0
#     while True:
#         attempts += 1
#         password = generate_password()
#         if check_password_strength(password):
#             print(f"Надежный пароль: {password}")
#             break

#     print(f"Количество попыток: {attempts}")

# if __name__ == "__main__":
#     main()




