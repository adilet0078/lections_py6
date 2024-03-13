
# zip(Iterable) - она соединяет элементы из итерируемых объектов между собой в тип данных tuple и возвращает итератор


# ls1 = [1, 2, 3]
# ls2 = [100, 200, 300]
# ls3 = ['one', 'two', 'three']

# res = list(zip(ls1, ls2, ls3))
# print(res)
# # for x in res:
# #     print(x)

# -------------------------------------------

# all(), any()
# all(iterable) - возвращает True если все элементы итерируемого объекта истинные иначе False
# any(iterable) - возвращает True если хотя бы один элемент итерируемого объекта истинный иначе False

# ls = [[1, 2] , -5 , 'stroka', 1]
# print(all(ls))

# ip1 = '10.255.12.155'
# ip2 = '10.255.1y.123'

# result = all(x.isdigit() for x in ip1.split('.'))
# print(result)


# result2 = all(x.isdigit() for x in ip2.split('.'))
# print(result2)

# any # возвращает True если хотя бы один элемент итерируемого объекта истинный иначе False

# ls = [[1, 2] , -5 , 'stroka', 1 ,'']
# print(any(ls))


# ignor = ['rm-rf', 'sudo', 'reset', 'poweroff', 'exit']

# cmd = input('Enter command: ')
# if any (x in cmd for x in ignor):
#     raise Exception('you do not have permission')
# print('ok')   


# Анонимные функции - lambda(лямбда(обычные функции только без названия))
# lambda функции могут принимать сколько угодно аргументов, но всегда возвращают один и только один результат

# def sum_of_args(a, b):
#     return a + b
# print(sum_of_args(5, 6))

# func = lambda a, b: a + b
# print(func (15, 5 ))

# def myFunc (n):
#     # def result(num):
#     #     return num * n
#     # return result
#     return lambda num: num * n
# myDoubler = myFunc(2)
# myTripler = myFunc(3)

# print(myDoubler(550))
# print(myDoubler(50))
# print(myDoubler(73))
# print(myTripler(11))
# print(myTripler(5))
# print(myTripler(8))


# dict = {'john' : 1_000_000, 'jamie': 100, 'din': 10_000, 'anvar':500, 'sam' : 100_000 }

# res = sorted(dict.items(),key=lambda x: x[1], reverse=True)
# print(res)


# enumerate - она пронумировывает каждый элемент внутри  Iterable, ее собственным индексом   
# ls = ['hello', 'world', 'python', 'is', 'great']

# res = list(enumerate(ls))
# print(res)

# for index, value in enumerate(ls):
#     print(index, value)
# for i , x in enumerate(ls):
#     print(f' index {i},element {x}')
#---------------------------------------------------------------------------
# map(function , iterable) - применяет функцию к каждому элементу итерируемого объекта

# ls = ['one', 'two', 'three', 'four', 'five']
# res = list(map(str.title, ls))
# print(res)
# res = []
# for x in ls :
#     res.append(x.title())
# print(res)

# names = ['John', 'Sultan','Anvar', 'Din', 'Sam']
# res = list(map(lambda name: f'Hello, {name}!', names))
# print(res)

# dict_ = {1:2, 3:4, 5:6 }
# # ------->{1:'2', 3:'4', 5:'6'}
# print(dict_)

# res = dict(map(lambda x: (x[0], str(x[1])), dict_.items()))
# print(res)

# filter (function, iterable) -->применяет ко всем элементам  итерируемую функцию которую мы передали и возвращает итератор с теми элементами
# для которых условие истинно(True).(фильтрует итерируемый объект, оставляя только те элементы, которые удовлетворяют заданному условию)


# ls = ['one', 'two', '', 'list', '100', '12', 'din']
# res = []
# for x in ls:
#     if x.isdigit():
#         res.append(x)
# print(res)


# res = list(filter(str.isdigit, ls))
# print(res)

# ls = ['john', 'codify', 'aibek', 'ono','bootcamp', 'Kyrgyzstan', 'mountains' ] 

# res = list(filter(lambda x: len(x) > 5, ls))
# print(res)


# ls = [
#     {'name': 'python','point':10},
#     {'name': 'java','point':3},
#     {'name': 'c++','point':6},
#     {'name': 'js','point':8},
#     {'name': 'c#','point':9}
#  ] # > 8
# res = list(filter(lambda dict_: dict_['point'] > 8 ,ls ))
# print(res)


# users = [
#     {'username': 'Din', 'comments': ['I love u !',' so gorgeus!']},
#     {'username': 'Raichel', 'comments': []},
#     {'username': 'Steven', 'comments': ['bishkek', 'python']},
#     {'username': 'Sam', 'comments' : []},
#     {'username':'Kira', 'comments': ['the best post!']}
# ]
# acive_users = list(filter(lambda 
#                           obj :  obj ['comments'], users))

# inacive_users = list(filter(lambda 
#                           obj : not obj ['comments'], users))
# print(acive_users)
# print()
# print(inacive_users) 

# ---------------------------------------------------------------------------------------------

# names = ['John', 'Sultan','Anvar', 'Din', 'Sam']
# res = list(
#     map(lambda x: f'Hello, {x}!',filter(lambda x: len(x) > 5, names))
# )
# print(res)

# ------------------------------------------------------------------------------------
# функция Reduce () принимает функцию и последовательность и возвращает одно значение, рассчитанное следующим образом:
# 1. Первоначально функция вызывается с первыми двумя элементами из последовательности, и результат возвращается.
# 2. Затем функция вызывается снова с результатом, полученным на шаге 1, и следующим значением в последовательности. Этот процесс повторяется до тех пор, пока в последовательности не закончатся элементы.


# from functools import reduce
# ls = [1, 2, 3, 4, 5]
# sum = reduce(lambda x, y: x + y, ls)
# res = reduce(lambda x, y: x * y, ls)
# print( sum,res)

# --------------------------------------------------------------
# from itertools import repeat
# from random import choices, shuffle
# from string import ascii_letters, digits
# from statistics import mean

# symbols = '_()$!%+-@#'
# q_pass = int(input('Enter quantity of passwords: '))
# res = {
#      f (choices(ascii_letters, k=10),
#       choices(digits, k=4),
#       choices(symbols, k=2)) 
#       for f in repeat(
#          lambda a, b, s: ''.join(set(a+b+s)), q_pass)

# }
# print(res)
# print(f'quantity of passwords: {len(res)}')
# dlina =[len(x) for x in res]
# print(f'mean: {mean(dlina)}')
