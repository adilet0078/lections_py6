# 1) Task Палиндром:

# Напишите программу, которая проверяет, является ли введенная пользователем строка палиндромом (читается одинаково с начала и с конца, игнорируя пробелы, регистр букв).


# def is_palindrome(input_str):
#     cleaned_str = ''.join(input_str.split()).lower()
#     return cleaned_str == cleaned_str[::-1]

# user_input = input("Enter a string: ")

# if is_palindrome(user_input):
#     print("It's a palindrome!")
# else:
#     print("It's not a palindrome.")

# Task 2 
# Подсчет слов:

# Программа должна принимать текст и слово. Напишите программу, которая подсчитывает количество слов в этом предложении.
# Так же вам нужно подсчитать количество введенного слова в этом тексте

# text = input("Enter text: ")
# word = input("Enter word: ")

# print(text.count(word))

# Task 3 
# Генерация пароля:
# Напишите программу, которая генерирует случайный пароль заданной длины. Пароль должен содержать как буквы, так и цифры.

# input= int(input("Enter the length of the password: "))
# import random
# import string
# print ("".join(random.sample(string.ascii_letters + string.digits, input)))

# Task 4 
# Поиск повторяющихся символов:
# Напишите программу, которая проверяет, есть ли в веденной строке повторяющиеся символы.

# string = input('enter a sring :')

# if len(string) == len(set(string)):
#     print('no repeated characters')
# else:
#     print('repeated characters')

# Task 5
#  Подсчет гласных и согласных:
# Введите строку, а затем напишите программу, которая подсчитывает количество гласных и согласных букв в ней.


# def count_vowels_and_consonants(input_str):
#     vowels = "aeiouAEIOU"
#     consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

#     # Инициализируем счетчики
#     vowel_count = 0
#     consonant_count = 0

#     for char in input_str:
#         if char in vowels:
#             vowel_count += 1
#         elif char in consonants:
#             consonant_count += 1

#     return vowel_count, consonant_count

# # Получаем ввод от пользователя
# user_input = input("Введите строку: ")

# # Подсчитываем гласные и согласные
# vowels, consonants = count_vowels_and_consonants(user_input)

# # Выводим результат
# print(f"Количество гласных букв: {vowels}")
# print(f"Количество согласных букв: {consonants}")
