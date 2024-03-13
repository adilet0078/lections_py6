

# """
# 1) В текстовом файле посчитать количество строк, а также для каждой
# отдельной строки определить количество в ней символов и слов. (5 баллов)
# """
# # Писать код здесь

# with open ('home.txt', 'r') as file:
#     stroki = len(file.readlines())
#     file.seek(0)
#     for i in file.readlines():
#         print(f'Количество символов в строке: {len(i)}', f'Количество слов в строке: {len(i.split())}')

# """
# 2) Создайте файл nums.txt, содержащий несколько чисел, записанных через
# пробел. Напишите программу, которая подсчитывает и выводит на экран
# общую сумму чисел, хранящихся в этом файле. (5 баллов)
# """
# # Писать код здесь
# with open('nums.txt', 'r') as file:
#     numbers = file.read().split()
#     numbers = [int(num) for num in numbers]
#     sum = 0
#     for num in numbers:
#         sum += num
#     print(sum)

# """
# 3) Считать из файла input.txt 10 чисел (числа записаны через пробел). Затем
# записать их произведение в файл output.txt (5 баллов)
# """
# # Писать код здесь

# with open('input.txt', 'r') as file:
#     numbers = file.read().split()
#     numbers = [int(num) for num in numbers]
#     product = 1
#     for num in numbers:
#         product *= num

# with open('output.txt', 'w') as file:
#     file.write(str(product))

# """
# 4) В файле записаны в целые числа. Найти максимальное и минимальное
# число и записать в другой файл. (5 баллов)
# """
# # Писать код здесь

# with open('input.txt', 'r') as file:
#     numbers = file.read().split()
#     numbers = [int(num) for num in numbers]
#     max_num = max(numbers)
#     min_num = min(numbers)
#     with open('output.txt', 'w') as file:
#         file.write(f'{max_num} {min_num}')

# """
# 5) В файле записаны в столбик целые числа. Отсортировать их по
# возрастанию суммы цифр и записать в другой файл. (5 баллов)
# """
# # Писать код здесь

# with open('input.txt', 'r') as file:
#     numbers = file.read().split()
#     numbers = [int(num) for num in numbers]
#     sorted_numbers = sorted(numbers, key=lambda x: sum(map(int, str(x))))
#     with open('output.txt', 'w') as file:
#         file.write(' '.join(map(str, sorted_numbers)))


# # 6) Напишите функцию read_last(lines, file), которая будет открывать определенный файл file и выводить на печать построчно последнюю строку в количестве lines (на всякий случай проверим, что задано положительное целое число). Протестируем функцию на файле «article.txt» со следующим содержимым:Вечерело Жужжали мухи  (15 баллов)
#                                                 Светил фонарик             
#                                                 Кипела вода в чайнике
#                                                 Венера зажглась на небе 
#                                                 Деревья шумели 
#                                                 Тучи разошлись 
#                                                 Листва зеленела

# def read_last(n, file):
#     with open(file, 'r') as f:
#        result = f.readlines()[-n:]
#     return result

# print(read_last(2, 'article.txt'))



# # 7) Выберите любую папку на своем компьютере, имеющую вложенные директории. Выведите на печать в терминал ее содержимое, как и всех подкаталогов при помощи функции print_docs(directory).
# # Проход по все каталогам и файлам в определенной директории можно осуществить при помощи функции walk() модуля os.(15 баллов)

# import os
# def print_docs(directory):
#     for root, dirs, files in os.walk(directory):
#         for file in files:
#             print(os.path.join(root, file))

# print_docs('.')


# # 8) Документ «article.txt» содержит следующий текст:     Вечерело Жужжали мухи 
#                             Светил фонарик 
#                             Кипела вода в чайнике 
#                             Венера зажглась на небе 
#                             Деревья шумели 
#                             Тучи разошлись 
#                             Листва зеленела 
# Требуется реализовать функцию
# longest_words(file), которая выводит слово, имеющее максимальную длину (или список слов, если таковых несколько). (15 баллов)


# def longest_words(file):
#     with open(file, 'r') as f:
#         words = f.read().split()
#     max_word = max(words, key=len)
#     return max_word

# print(longest_words('article.txt'))



# # 9) Требуется создать csv-файл «rows_300.csv» со следующими столбцами: – № - номер по порядку (от 1 до 300); – Секунда – текущая секунда на вашем ПК; – Микросекунда – текущая миллисекунда на часах. На каждой итерации цикла искусственно приостанавливайте скрипт на 0,01 секунды. (15 баллов)


# import csv
# import time
# with open('rows_300.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     for i in range(1, 301):
#         time.sleep(0.01)
#         writer.writerow([i, time.time(), time.time() * 1000])



# # 10) Имеется текстовый файл prices.txt с информацией о заказе из интернет магазина. В нем каждая строка с помощью символа табуляции \t разделена на три колонки:
# # наименование товара;
# # количество товара (целое число);
# # цена (в рублях) товара за 1 шт. (целое число).
# # Напишите программу, подсчитывающую общую стоимость заказа. (15 баллов)

# total = 0
# with open('prices.txt', 'r') as file:
#     for line in file:
#         parts = line.strip().split('\t')
#         if len(parts) == 3:
#             name, quantity, price = parts
#             try:
#                 total += int(quantity) * int(price)
#             except ValueError:
#                 print(f"Invalid quantity or price in line: {line.strip()}")
#         else:
#             print(f"Illegal line: {line.strip()}")

# print(total)


#                                 ДОПОЛЬНИТЕЛЬНО

# # 11) Словарь из csv. Имеется файл data.csv, содержащий информацию в csv-формате. Напишите функцию read_csv() для чтения данных из этого файла. Она должна возвращать список словарей, интерпретируя первую строку как имена ключей, а каждую последующую строку как значения этих ключей. Функция read_csv() не должна принимать аргументов. (10 баллов)


# import csv
# def read_csv(file):
#     with open(file, 'r') as f:
#         reader = csv.DictReader(f)
#         return list(reader)

# data = read_csv('data.csv')
# print(data)


# # 12) Запрещенные слова
# # Напишите программу, которая получает на вход строку с названием текстового файла, и выводит на экран содержимое этого файла, заменяя все запрещенные слова звездочками * (количество звездочек равно количеству букв в слове). Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле forbidden_words.txt. Все слова в этом файле записаны в нижнем регистре. Программа должна заменить запрещенные слова, где бы они ни встречались, даже в середине другого слова. Замена производится независимо от регистра: если файл forbidden_words.txt содержит запрещенное слово exam, то слова exam, Exam, ExaM, EXAM и exAm должны быть заменены на ****.        (10 баллов)
# # Формат ввода
# # Строка текста с именем существующего текстового файла, в котором необходимо заменить запрещенные слова звездочками.
# # Формат вывода
# # Текст, отредактированный в соответствии с условием задачи.
# # Пример ввода вывода
# # Предположим, что forbidden_words.txt содержит следующие запрещенные слова:
# # hello email python the exam wor is
# # А текст файла, подлежащего цензуре, выглядит так:
# Hello, world! Python IS the programming language of thE future. My EMAIL is.... PYTHON is awesome!!!!
# # Тогда программа должна вывести отредактированный текст в таком виде:
# # # *, *ld! **  * programming language of * future. My * .... **  awesome!!!!

# import re

# def censor_text(input_file):
#     with open('prices.txt', 'r') as forbidden_file:
#         forbidden_words = forbidden_file.read().split()

#     with open(input_file, 'r') as file:
#         text = file.read()

#     for word in forbidden_words:
#         pattern = re.compile(r'\b' + re.escape(word) + r'\b', re.IGNORECASE)
#         text = pattern.sub('*' * len(word), text)

#     print(text)

# # Example usage
# censor_text('prices.txt')




# # 13) В текстовый файл построчно записаны фамилия и имя учащихся класса и его оценка за контрольную. Вывести на экран всех учащихся, чья оценка меньше 3 баллов (5 баллов)

# # Открываем файл для чтения
# with open('output.txt', 'r') as file:
#     # Читаем строки из файла
#     lines = file.readlines()

# # Проходим по каждой строке и анализируем оценку
# for line in lines:
#     # Разделяем строку на фамилию, имя и оценку
#     surname, name, score = line.strip().split()
#     # Преобразуем оценку в целое число
#     score = int(score)
#     # Проверяем, если оценка меньше 3, выводим на экран фамилию и имя учащегося
#     if score < 3:
#         print(surname, name)



# # 14) Выведите в обратном порядке содержимое всего файла полностью. Для этого считайте файл целиком при помощи метода read().  (5 баллов)
# Примеры
# входные данные:
# Beautiful is better than ugly. 
# Explicit is better than implicit. 
# Simple is better than complex.
# Complex is better than complicated.

# выходные данные:
# .detacilpmoc naht retteb si xelpmoC 
# .xelpmoc naht retteb si elpmiS 
# .ticilpmi naht retteb si ticilpxE 
# .ylgu naht retteb si lufituaeB
# Открываем файл для чтения


with open('prices.txt', 'r') as file:
    content = file.read()
print(content[::-1])

