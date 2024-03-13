

# def sum_args(a, b, c=5, d=3): # параметры функции
#     return a + b + c + d
# result = sum_args(1, 2, 3, 4) # аргументы
# print(result)
# print(sum_args(0, 0))

# -----------------------------------------------------------------------------
# позиционные и именованные аргументы

# def printParams(a, b, c):
#     print(a, 'is stored in param a')
#     print(b, 'is stored in param b')
#     print(c, 'is stored in param c')
    
# # printParams(5 , 10, 15)
# # printParams()
# printParams( c=15, b=10, a=5)

# def sum_of_args(a, b, c, d):
#     return a + b + c + d

# print(sum_of_args(5, 10, 15, 20 ))                  # аргументы(позиционные)
# print(sum_of_args(a=5, b=10, c=15, d=20 ))          # именованные аргументы(keywords arguments)
# print(sum_of_args(5, 10, d=20, c=15 ))              #смешанные аргументы



# оператор * - распаковка (передача нескольких аргументов в функцию)
# a = (1, 2, 3)
# b= (4, 5, 6)
# c = [*a, *b]
# print(c)

#-----------------------------------------------------------------------------
# *args, **kwargs - позиционные и именованные аргументы

# def func(*args, **kwargs):
#     print(args)
#     print(kwargs)

# func(1, 2, 3, a=5, b=10)

# def printScores(student, *scores):
#     print(f'Студент {student}, ')
#     # print(scores)
#     print(f'AMG: {sum(scores)/len(scores)}')
#     for x in scores:
#         print(f'Оценка: {x}')

# printScores('Иван', 5, 4, 3, 5)

# def printParamPetNames(owners, **pets):     #{'key': 'value'}
#     print(f'owner name: {owners} ')
#     # print(pets)

# # printParamPetNames('John Snow', dog='Rex', cat='Garfield')
#     for pet, name in pets.items():
#         if type(name) == list: 
#             print(f'{pet}', *name)
#         else:
#             print(f'{pet}:{name}')
# printParamPetNames('John Snow', dog='Rex', cat='Garfield', fish=['Nemo','Dori','Tima'],turtle= 'Leonardo' )



# def get_some_data( a, b, *args, **kwargs):
#     print('параметры a и b:', a , b)
#     print('позиционные аргументы:', args)
#     print('ключевые аргументы:', kwargs)

# get_some_data(1, 2, 3, 4, 5, 6, name='John', age=30)

# import string as s 
# from random import choice, shuffle
# def generate_random_string(len_):
#     # print(s.ascii_letters, s.digits, s.punctuation )
#     symbols = s.ascii_letters + s.digits
#     res = [choice(symbols) for _ in range(1, len_)] + [choice(s.punctuation)]
#     shuffle(res)
#     return ''.join(res)

# print(generate_random_string(15))
# print(generate_random_string(20))
# print(generate_random_string(9))
# print(generate_random_string(11))

