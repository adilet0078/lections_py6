# # task 1 
# У вас есть словарь игроков, которые участвовали в трёх видах спорта. В словаре хранятся пары «Ф. И. — очки»:
# players = {

#     ("Will", "Smith"): (10, 5, 13),

#     ("Bob", "Robbin"): (7, 5, 14),

#     ("Rob", "Bobbin"): (12, 8, 2)

# }
# Один программист попросил нас для своей базы отправить ему немного другой вариант хранения этой информации.
# Напишите программу, которая объединяет ключ словаря со значением в один кортеж, и выведите результат на экран. Постарайтесь использовать как можно более эффективное решение.
# Результат работы программы:
# [('Will', 'Smith', 10, 5, 13), ('Bob', 'Robbin', 7, 5, 14), ('Rob', 'Bobbin', 12, 8, 2)]

# players = {

#     ("Will", "Smith"): (10, 5, 13),

#     ("Bob", "Robbin"): (7, 5, 14),

#     ("Rob", "Bobbin"): (12, 8, 2)

# }
# result = []
# for k, v in players.items():
#     res = tuple(list(k) + list(v))
#     result.append(res)

# print(result)


# task 2
# Есть список из 10 случайных чисел. Напишите программу, которая делит эти числа на пары кортежей внутри списка, и выведите результат на экран.
# Дополнительно: решите задачу несколькими способами.
# Пример:
# Оригинальный список: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Новый список: [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9)]

# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# result = []
# for i in range(0, len(numbers), 2):
#     result.append(numbers[i:i+2])
# print(result)

# Python program to create a list of tuples
# from given list having number and
# its cube in each tuple
 
# # creating a list
# list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# # using list comprehension to iterate each
# # values in list and create a tuple as specified
# res = [(val, val**3) for val in list1]
#  # print the result
# print(res)

# task 3  Посчитайте, сколько раз символ "O"и "А" встречается в строке.   
# "ДЛЯ ТОГО, ЧТОБЫ ЗНАТЬ, ЧТО НРАВСТВЕННО, НАДО ЗНАТЬ, ЧТО БЕЗНРАВСТВЕННО; ДЛЯ ТОГО, ЧТОБЫ ЗНАТЬ, ЧТО ДЕЛАТЬ, НАДО ЗНАТЬ, ЧЕГО НЕ ДОЛЖНО ДЕЛАТЬ"

# text = "ДЛЯ ТОГО, ЧТОБЫ ЗНАТЬ, ЧТО НРАВСТВЕННО, НАДО ЗНАТЬ, ЧТО БЕЗНРАВСТВЕННО; ДЛЯ ТОГО, ЧТОБЫ ЗНАТЬ, ЧТО ДЕЛАТЬ, НАДО ЗНАТЬ, ЧЕГО НЕ ДОЛЖНО ДЕЛАТЬ"
# print(text.count('О'))  
# print(text.count('A'))

# TASK 4 
# Переделайте прошлый калькулятор
# Сделайте так, чтобы калькулятор спрашивал постоянно данные для совершения операций в калькулятор
# Если пользователь вводит букву q то калькулятор должен завершаться (для хардкора, если пользователь введет пустую строку, вывести строку "Нет ничего приятнее, чем знание о твоих знаниях!

# print("0 в качестве знака операции"
#       "\nзавершит работу программы\n")
 
# while True:
#     s = input("Знак (+, -, *, /): ")
#     if s == '0':
#         break
#     if s in ('+', '-', '*', '/'):
#         a = float(input("a = "))
#         b = float(input("b = "))
#         if s == '+':
#             print("%.2f" % (a + b))
#         elif s == '-':
#             print("%.2f" % (a - b))
#         elif s == '*':
#             print("%.2f" % (a * b))
#         elif s == '/':
#             if b != 0:
#                 print("%.2f" % (a / b))
#             else:
#                 print("Деление на ноль!")
#     else:
#         print("Неверный знак операции!")

# while True:
#     # Ask for user input
#     data = input("Enter an operation ('q' to quit): ")

#     # Check if user wants to quit
#     if data == 'q':
#         break

#     # Check if input is empty
#     if not data:
#         print("Нет ничего приятнее, чем знание о твоих знаниях!")
#         break

#     # Evaluate the operation
#     try:
#         result = eval(data)
#         print("Result:", result)
#     except Exception as e:
# #         print("Error:", str(e))

# task 5 
# Дополнительно: попробуйте реализовать программу через цикл While, "стоп-слово" для выхода из цикла "Выход"

# Мы решили написать приложение для удобного прослушивания музыки, но наши песни хранятся в виде словаря. Каждая песня состоит из названия и продолжительности с точностью до долей минут.
# violator_songs = {

#     'World in My Eyes': 4.86,

#     'Sweetest Perfection': 4.43,

#     'Personal Jesus': 4.56,

#     'Halo': 4.9,

#     'Waiting for the Night': 6.07,

#     'Enjoy the Silence': 4.20,

#     'Policy of Truth': 4.76,

#     'Blue Dress': 4.29,

#     'Clean': 5.83

# }

# Напишите программу, которая запрашивает у пользователя количество песен из списка и затем названия этих песен, а на экран выводит общее время их звучания.
# Пример:
# Сколько песен выбрать? 3
# Название 1 песни: Halo
# Название 2 песни: Enjoy the Silence
# Название 3 песни: Clean
# Общее время звучания песен: 14.93 минут

# violator_songs = {
#     'World in My Eyes': 4.86,
#     'Sweetest Perfection': 4.43,
#     'Personal Jesus': 4.56,
#     'Halo': 4.9,
#     'Waiting for the Night': 6.07,
#     'Enjoy the Silence': 4.20,
#     'Policy of Truth': 4.76,
#     'Blue Dress': 4.29,
#     'Clean': 5.83
# } 
# total_time = 0 
# print('welcome to music player')
# num_of_songs = int(input('сколько песен вы хотите выбрать?'))
# while num_of_songs > 0 :
#     song_title = input(f"название песни {num_of_songs} (введите 'stop' чтоб выйти): ")
#     if song_title.lower() == 'stop':
#             break
#     if song_title in violator_songs:
#         total_time += violator_songs[song_title]
#         num_of_songs -= 1
#     else:
#         print("неверное название песни. пожалуйста введите правильное название песни.")
        
# print(f'общее время звучания песен: {total_time} минут')

# task 6 
# Задача 6. (дополнительно)

# Асан помимо программирования также увлекается и географией, поэтому он решил связать эти две области и написать для своего проекта небольшую программу-навигатор.

# Пользователь вводит количество стран N, а затем N раз вводит страну и города, которые в этой стране находятся, в одну строку. Затем пользователь вводит три названия городов. Реализуйте такую программу и для каждого из трёх городов укажите, в какой стране он находится. Если такого города нет, то выведите соответствующее сообщение.
# Пример: 
# Кол-во стран: 2

# 1 страна: Кыргызстан Бишкек Кант Каракол

# 2 страна: Германия Берлин Лейпциг Мюнхен

#  1 город: Москва
# Город Москва расположен в стране Россия.

#  2 город: Мюнхен
# Город Мюнхен расположен в стране Германия.

# 3 город: Рим
# По городу Рим данных нет.
 

# # Get the number of countries
# num_countries = int(input("Number of countries: "))

# # Create a dictionary to store the country-city mapping
# country_city_mapping = {}

# # Iterate over each country and its cities
# for i in range(num_countries):
#     country_cities = input(f"{i+1} country: ").split()
#     country = country_cities[0]
#     cities = country_cities[1:]
#     for city in cities:
#         country_city_mapping[city] = country

# # Get the three cities from the user
# for i in range(3):
#     city = input(f"{i+1} city: ")
#     if city in country_city_mapping:
#         print(f"The city of {city} is located in the country of {country_city_mapping[city]}.")
#     else:
#         print(f"There is no data for the city of {city}.")