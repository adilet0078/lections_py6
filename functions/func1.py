# нaйти квадрат,куб , результат деление 100 любых 3 чисел 

# num = 5 
# {'num':5, '2':25, '3': 125, '100':  0.05}
# num1 = 5
# num2 = 75
# num3 = 1154

# res = {'num' : num1, '2': num1 ** 2, '3': num1 ** 3, '100': num1 /100 }
# res2 = {'num' : num2, '2': num2 ** 2, '3': num2 ** 3, '100': num2 /100 }
# res3 = {'num' : num3, '2': num3 ** 2, '3': num3 ** 3, '100': num3 /100 }

# print(res, res2, res3, sep='\n\n')


# DRY - don't repeat yourself

# def do_operations(num: int) -> None:
#     res = {'num' : num, '2': num ** 2, '3': num ** 3, '100': num /100 }
#     print(res)

# do_operations(5)
# do_operations(75)
# do_operations(1154)

# --------------------------------------------------------------------

# функция - это именованная часть программы, которая содержит в себе определенный блок кода, и может вызываеться из других частях программы столько раз сколько угодно

# def name_of_function(<a,b> параметры фнукции):
    # <body>  #код,какая то логика которая будет давать конечный результат
    # return <value> # опертаор который помогает сохранить результат возвращаемый функцией

# name_of_function(4 ,6 # аргументы)
# параметры функйции - переменные в которых мы временно сохраняем данные которые передаем при вызове в функцию, они доступны только внутри функции
# аргументы функции - данные которые мы передаем при вызове функции, они попадают в параметры функции по очередно

# def isEven(num):
#     return True if num % 2 == 0 else False

# res = isEven(16)
# res1 = isEven(17)
# print(res, res1)

# def isEven(num: int) -> bool:
#    """ return True or False after cheking number is even """
#    return True if num % 2 == 0 else False


# def sum_of_args(a: int, b: int , c: int=0) -> int:
#     """return sum of given arguments"""
#     try:
#         return a + b + c
#     except TypeError:
#         raise Exception(' invalid values for  arguments')
    

# print(sum_of_args(1, 2, ))
# print(sum_of_args(6, 9, 12))
# print(sum_of_args(6, 9, None))

# ---------------------------------------------------------------------------
# print(len('string'))


# from typing import Iterable

# def our_len(obj: Iterable) -> str :
#     """return len of iterable object"""
#     i = 0
#     print(obj)
#     for _ in obj: 
#         i += 1
#     print(f'result:{i} ')

# our_len([1,2,3,4,5,6,7,8,9,10])
# our_len('string Hello World My name is John Snow')

#----------------------------------------------------------------------------

'hello world! My name is John Snow, nice to meet you.'


# 'hello world snow king'
# 'king snow world hello'

# s = 'hello world snow king'
# reversed_string = ' '.join(reversed(s.split()))
# print(reversed_string)

# def reverse_text(text: str) -> str:
#     """reversing text"""
#     spisok = text.split()
#     return ' '.join(reversed(spisok [::-1]))
# print(reverse_text('hello world snow kings'))

# str1 = 'hello world snow king '
# print(reverse_text(str1))
# print(reverse_text('hello world snow king '))
