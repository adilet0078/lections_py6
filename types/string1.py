# "String -  строки"
# "Hello world! My name is John Snow!"

# str1 = '''
# I'm John Snow 
# Im King of North!
# '''
# print(str1)

#  строки -  набор последовательных символов, которрые мы используем для хранение и представление текстововй информации

# индексация  в строке 
# name = "John" 
# # J = 0 = -4
# # o = 1 = -3 
# # h = 2 = -2
# # n = 3 = -1 
# print(name)
# print(name[1]) 
# print(name[-1])

# срезы по индексам 
# [start: end: <step>]

# str1 = "birthday"
# # print(str1)
# # print(str1[0 : 5])
# # #print(str1[5 : 8])
# print(str1[:5])
# print(str1[5:])

# text = "Hello world! My name is John Snow! I/'m King of North!"
# print(text)
# print(text[:13])
# print(text[:13:3])
# print(text[::2])
# print(text[::-2])

# конкатенация строк(соединение )
# a = "Hello"
# b = "World"
# c = ' '
# res = a + c + b
# print(res)

# экранирование - способ записи символов в строку,которые невозможно ввести с клавиатуры , либо же записать спец символов которые имеют функционал в питоне

# \n -> перенос строки
# \t -> горизонтальная табуляция
# \v -> вертикальная табуляция
# \' -> ' апостроф
# \" -> " кавычка
# \\ -> \ обратный слеш
# \f -> \f - перевод страницы
# \r -> \r - возврат каретки

# str1 = '\tHello world!\n\v\tHello John!\n\'\\'
# print(str1) 

# Форматирование строк 
# 1. с помощью % 
# 2. с помощью .format()
# 3. итерполяция(преобразование строк) f- строки

# first_name = input('Enter your first name: ') 
# last_name = input('Enter your last name: ')
# STR1 = 'Hello mr/mrs %s %s' %(first_name, last_name )
# print(STR1)

#  .format
# first_name = input('Enter your first name: ') 
# last_name = input('Enter your last name: ')
# club = 'Kipish'
# print('Welcome in da club, {}, mr/mrs {} {}!'.format(club, first_name, last_name))

# f-строки
# name = input('Enter your name: ')
# first_name = input('Enter your first name: ')
# print(f'Hello mr/mrs {name} {first_name}! Welcome to the party!')

# Умножение строк 
# str1 = 'codify '
# print(str1 * 5)

