# text = ('the more you learn, the more you earn ')
# # len() - возвращает длину строки, считая каждый ее символ 
# len_text = len(text)
# print(len_text, text)
# print(text[:: -1])

# count_e = 0
# i = 0 
# while i < len_text: 
#     symbol = text[i]
#     if symbol == 'e' or symbol == 'E':
#         count_e += 1
#     i += 1 # инкримент i = i + 1   
#     print(symbol)    
#     print(f'Symbols e :found:{count_e} times!' )

# custome len code

# ---------------------------------


# методы строк - dir()

# print(dir(str))
# print(dir(12))

# count(value, [start]) - считает количество вхождений value в  нашу строку 
# text = ('hello o o o o hello ')
# print(text.count('h',5))
# print(text.count('o'))
# print(text.count('l'))

# # replase(old, new, [count]) - меняет в строке old на new, заменит count раз если передается число
# text = "ha ha ha ha "
# res = text.replace('a', 'e' ,2)
# print(text)
# print(f'original: {text} ')
# print(f'result after replace: {res} ' )

# strip() - убирает пробельные символы в начале и в конце строки
# rstrip , lstrip 
# a = '  hello  '
# print(a, len(a), sep= '->')
# res = a.lstrip()
# print(res, len(res), sep= '->')
# print (a.lstrip(), '1')

# print(dir(str))
# isdigit - проверяет является ли строка числом 
# isnumeric- проверяет является ли строка числом
# isdecimal - проверяет является ли строка десятичным числом
 
# num  = input('enter the number ')
# print(f'entered number is?:{num.isdigit()}')

# isalpha = состоит ли наша строка только из букв 
# txt = "hello world"
# print(txt.isalpha())
# res = txt.replace (' ', '')
# print(res, res.isalpha())

# num = int(input('enter your number: '))
# if num.isdigit(): 
#     num = int(num)
#     print(f'{num} * 5 = {num *5} ')      
# else:
#      print('enter the number')

#  split() - разбивает нашу строку по разделителю
# spilit(seperator)- дробит(разделяет) строку на несколько частей по разделителю,все части сохраняются в типе list

# text = 'let me speak in english !'
# res = text.split('e')
# print(res)
# print(text) 
# print(text.split)

# a = '#hello#life#work#bishkek'
# print(a)
# print(a[1 :].split('#'))

# 'connector'.join(list) - объединяет элементы списка по connector строки которые были в list
# ls = ['Anvar', 'John', 'Alex', 'Osmon']
# print(ls)
# res = '-'.join(ls)
# print(res)

# swapcase() - меняет регистр букв в строке на противоположный
# upper() - переводит строку в верхний регистр 
# lower() - переводит строку в нижний регистр

# original_string = "Hello, World!"

# swapped_string = original_string.swapcase()

# print(swapped_string)
# print(original_string.lower())
# print(original_string.upper())      

# index(value - выводит индек значение value внутри строки) 
# find(value - делает тоже самое что и index , но возвращает -1 если не найдено)

# text = "Hello, World!"

# # print(text.index("Hello"))
# # print(text.index("World!"))
# # print(text.index("o" , -2))
# print(text.find('a'))