# EXTRA


# 1) '''Магическими называются даты, в которых произведение дня и месяца
# составляет последние две цифры года. Например, 10 июня 1960 года –
# магическая дата, поскольку 10 ´ 6 = 60. Напишите функцию, определя-
# ющую, является ли введенная дата магической. Используйте написан-
# ную функцию в главной программе для отображения всех магических
# дат в XX ве­ке.'''

# import datetime
# def magic_date():
#     year = int(input("Enter a year: "))
#     for month in range(1, 13):
#         for day in range(1, 32):
#             date = datetime.date(year, month, day)
#             if date.day * date.month == year % 100:
#                 print(f"Magic date: {date}")

# magic_date()

# 2) '''Напишите функцию для определения количества дней в конкретном ме-
# сяце. Ваша функция должна принимать два параметра: номер месяца
# в виде целого числа в диапазоне от 1 до 12 и год, состоящий из четырех
# цифр. Убедитесь, что функция корректно обрабатывает февраль високос-
# ного года. В основной программе запросите у пользователя номер месяца
# и год и отобразите на экране количество дней в указанном месяце.'''


# def days_in_month(month, year):
#     if month in (1, 3, 5, 7, 8, 10, 12):
#         return 31
#     elif month == 2:
#         if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
#             return 29
#         else:
#             return 28
#     else:
#         return 30

# month = int(input("Enter the month: "))
# year = int(input("Enter the year: "))
# print(days_in_month(month, year))
# # #

# 3) '''Напишите две функции с именами hex2int и int2hex для конвертации
# значений из шестнадцатеричной системы счисления 543в десятичную (по основанию 10) и обратно. Функ-
# ция hex2int должна принимать на вход строку с единственным символом
# в шестнадцатеричной системе и преобразовывать его в число от нуля
# до 15 в десятичной системе, тогда как функция int2hex будет выполнять
# обратное действие – принимать десятичное число из диапазона от 0 до
# 15 и возвращать шестнадцатеричный эквивалент. Обе функции должны
# принимать единственный параметр со входным значением и возвращать
# преобразованное число. Удостоверьтесь, что функция hex2int корректно
# обрабатывает буквы в верхнем и нижнем регистрах. Если введенное поль-
# зователем значение выходит за допустимые границы, вы должны вывести
# сообщение об ошибке.'''
# def hex2int(hex_str):
#     hex_str = hex_str.lower()  # Приведем символ к нижнему регистру для удобства обработки
#     hex_digits = "0123456789abcdef"
#     if hex_str not in hex_digits:
#         print("Ошибка: Введенное значение не является шестнадцатеричным символом.")
#         return None
#     return hex_digits.index(hex_str)

# def int2hex(decimal_num):
#     hex_digits = "0123456789abcdef"
#     if decimal_num < 0 or decimal_num > 15:
#         print("Ошибка: Введенное число должно быть в диапазоне от 0 до 15.")
#         return None
#     return hex_digits[decimal_num]

# # Примеры использования:
# hex_value = "a"
# decimal_value = hex2int(hex_value)
# if decimal_value is not None:
#     print(f"Десятичное значение символа {hex_value} равно {decimal_value}.")

# decimal_value = 10
# hex_value = int2hex(decimal_value)
# if hex_value is not None:
#     print(f"Шестнадцатеричный эквивалент числа {decimal_value} равен {hex_value}.")
    


# #

# 4) '''Представьте, что в вашем регионе устаревшим является формат номер-
# ных автомобильных знаков из трех букв, следом за которыми идут три
# цифры. Когда все номера такого шаблона закончились, было решено об-
# новить формат, поставив в начало четыре цифры, а за ними три буквы.
# Напишите функцию, которая будет генерировать случайный номерной
# знак. При этом номера в старом и новом форматах должны создаваться
# примерно с одинаковой вероятностью. В основной программе нужно сге-
# нерировать и вывести на экран случайный номерной знак.'''
# import random
# import string

# def generate_license_plate():
#     old_format = random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase) + \
#                  str(random.randint(100, 999))
#     new_format = str(random.randint(1000, 9999)) + random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase)
    
#     return random.choice([old_format, new_format])

# # Generate and print a random license plate
# print(generate_license_plate())


