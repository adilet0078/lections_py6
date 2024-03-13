# Write a program that calculates the sum and product of the digits of a positive three-digit number.
# calculate the sum and product of the digits of a positive three-digit number 
# num= int(input ("enter the three digit number"))
# 123

# digit_sum = sum(int(digit) for digit in num)
# print(list(int(digit) for digit in num))
# digit_product = 1 
# for digit in num:
#     digit_product *=int(digit)
# print('sum of the digits:', digit_sum )  
# print('product of the digits:', digit_product)                     

# ed = num % 10
# des = num // 10 % 10
# sot = num // 100

# print(ed + des + sot)
# print(ed * des * sot)



# 1) Напишите функцию -- чат-бот, который 
# Всегда отвечает “Конечно!” на любой вопрос
# Всегда отвечает “Успокойся”, если ты кричишь на него ВОТ ТАК!
# Всегда отвечает “Как классно, когда ты молчишь. Продолжай в том же духе!” Если вызвал функцию, но ничего не передал.
# В любых других случаях, отвечает “ну и что


# def chat_bot(input_text):
#     if input_text.endswith('!'):                          #если оканчание текста на '!'
#         return "Успокойся"
#     elif not input_text.strip():
#         return "Как классно, когда ты молчишь. Продолжай в том же духе!"
#     else:
#         return "Конечно!"

# # Примеры использования:
# print(chat_bot("Какой сегодня день?"))
# print(chat_bot("Сколько будет дважды два?"))
# print(chat_bot("Я голоден!"))
# print(chat_bot("ВОТ ТАК!"))
# print(chat_bot(""))


# 2) Напишите функцию, которая принимает слово и возвращает True, если слово изограмма (т.е. все буквы в слове уникальны). Иначе возвращает False

# def is_isogram(word):
#     return len(set(word.lower())) == len(word)  #сранивает возравращенное слово,если оно уникально и в нижнем регистре и равно на длину текста 
# print(is_isogram("Algorism"))
# print(is_isogram("PasSword"))


#сранивает возравращенное слово,если оно уникально и в нижнем регистре и равно на длину текста то терминал выводить True а иначе False



# 3) Подсчет букв:
# Напишите функцию, которая принимает строку и возвращает словарь, в котором ключами являются буквы, а значениями — количество их вхождений в строку. Регистр букв не должен учитываться.
# """
# def count_letters(text):
#     return {letter: text.lower().count(letter) for letter in set(text.lower())} 
# count_letters("Hello World")
# print(count_letters("Hello World"))



# """
# 4) Поиск подстроки:
# Напишите функцию, которая принимает две строки и возвращает True, если вторая строка является подстрокой первой.
# ""

# def search_substring(main_string, substring):  
#     return substring in main_string

# print(search_substring("Hello World", "World"))
# print(search_substring("Hello World", "John"))



# 5) Напишите функцию, которая проверяет, сколько раз каждое слово в переданной фразе было использовано. Например: “Money, money, money, it’s always sunny, in the richmen’s world”. money: 3, it’s: 1, always: 1, sunny: 1, in: 1, the: 1, richmen’s: 1, world: 1.

# def count_words(text):
#     return {word: text.lower().split().count(word) for word in set(text.lower().split())}

# count_words("Money, money, money, it’s always sunny, in the richmen’s world")
# print(count_words("Money, money, money, it’s always sunny, in the richmen’s world"))



# """
# 6) Напишите функцию, которая принимает строку и выводит количество гласных, согласных букв и остальных символов. Используйте только кириллические символы
# """

# def count_vowels_consanants(string):
#     vowels = "aeiou"
#     consonants = 'bcdfghjklmnpqrstvwxyz'
#     count_vowels = sum(1 for char in string if char.lower() in vowels)
#     count_consonants = sum(1 for char in string if char.lower() in consonants)
#     count_other = len(string) - count_vowels - count_consonants
#     return count_vowels, count_consonants, count_other

# print(f"count_vowels_consanants: {count_vowels_consanants('Hello World ../')}")

# def count_vowels_consanants(string):
#     dict = { 
#         'vowels' : sum(1 for char in string if char.lower() in 'aeiou'),
#         'consonants' : sum(1 for char in string if char.lower() in 'bcdfghjklmnpqrstvwxyz'),
#         'other' : len(string) - sum(1 for char in string if char.lower() in 'aeiou') - sum(1 for char in string if char.lower() in 'bcdfghjklmnpqrstvwxyz')
#     }

#     return dict

# print(f"count_vowels_consanants: {count_vowels_consanants('Hello World ../')}")

# 7) Вам дан список из нескольких имён в нижнем регистре. Напишите функцию которая записывает начинает первую букву имени в верхнем регистре и сохраните в новом списке.
# """

# def list_name(name_list):
#     return [name.title() for name in name_list]

# print(list_name(['john', 'jane', 'jack']))


# 8) Вам дан список из целых чисел. Напишите функцию, в которой Вам необходимо найти факториал каждого из чисел и записать в новый список.


# import math 
# def factorial(num_list):
#     return [math.factorial(num) for num in num_list]

# print(factorial([1, 2, 3, 4, 5]))

# 9) Вам дан список из чисел. Напишите функцию, которая вернёт новый список из квадратов этих чисел.

# import math 
# def sqrt(num_list):
#     return [math.sqrt(num) for num in num_list]
# print(f'sqrt: {sqrt([4, 9, 16, 25])}')

# 10) Напишите функцию average, которая принимает список чисел и возвращает их среднее значение, НЕ используя встроенные функции sum и len
# def average(num_list):
#     return sum(num_list) / len(num_list)

# print(average([1, 2, 3, 4, 5]))
  
# def average(num_list):
#     count = 0
#     total = 0
#     for num in num_list:
#         count += 1
#         total += num
#     return total / count

# print(average([1, 2, 3, 4, 5]))
        
 