# Декаротар - это функция которая позволяет без изменения кода расширить функционал той функции к которой был применен декоратор

# import requests
# from time import time

# # api_url = 'https://api.ninjas.com/v1/cars?model={}'

# def timeCheckDecorator(func):
#     def wrapper():
#         start = time() #10:26:12
#         func()
#         finish = time() #10:26:32
#         print(f'Время выполнения: {round (finish - start, 2)} сек')
#     return wrapper

    
# @timeCheckDecorator
# def printcars():
#     car = input('введите марку авто: ')
#     api_url = f'https://api.api-ninjas.com/v1/cars?model={car}'
#     response = requests.get(api_url, headers={'X-Api-Key': 'fMvF8LTzSEKonJ8R7LWhEw==GYSkLGG2n8xytyiF'})
#     if response.status_code == 200:
#         print(response.text)
#     else:
#         print(f'Error: {response.status_code}\n {response.text}')



# import requests
# @timeCheckDecorator
# def print_users():
#     api_url = 'https://randomuser.me/api/'
#     data = requests.get(api_url)
#     if data.status_code == 200:
#         print(data.text)
#     else:
#         print(f'Error: {data.status_code}\n {data.text}')

# printcars()
# print()
# print()
# print_users()

# print_users()


# path = 8
# steps= 'uddduduu'
# # res = 1 #'dolina'

# sea_level = 0 
# dolina = 0
# for step in steps:
#     if step == 'u':
#         sea_level += 1
#         if sea_level == 0:
#             dolina += 1 
#     else:
#         sea_level -= 1


# print(f'{dolina} dolina')


# def decoprator(func):
#     def wrapper():
#         print('decorator worked!')
#         print(f'{func.__name__} ,была вызвана!')
#         print()
#         func()
#     return wrapper


# @decoprator
# def getName():
#     print(f'Owner name is John Snow')

# getName()


# @decoprator
# def hello():
#     print('hello world!')

# hello()


# def trace(func):
#     def wrapper( *args , **kwargs):
#         print(f'trace: вызвала  {func.__name__}(\nona  приняля args: {args}, kwargs: {kwargs}')
#         res = func( *args , **kwargs)
#         print(f'trace: вызвала  {func.__name__}() \noна  вернула {res}')
#         return res
#     return wrapper

# @trace
# def printAdress(name, adress ):
#     return f'name: {name} -> lives in adress: {adress}'

# @trace
# def get_hello(name, last_name, country):
#     return f'hello {name} {last_name} from {country}'

# # print(printAdress('dinwinchestr', 'kanzas'))
# # print(get_hello('John', 'Snow', 'Great Britain'))


# printAdress('John', 'London')
# print()
# print(get_hello('John', last_name ='Snow',country = 'Great Britain'))


# def boldText(func):
#     def wrapper(*args, **kwargs):
#         res = f'<bold> + {func(*args, **kwargs)} + </bold>'
#         return res
#     return wrapper

# def itext(func):
#     def wrapper(*args, **kwargs):
#         res = f'<i> + {func(*args, **kwargs)} + </i>'
#         return res
#     return wrapper


# @itext
# @boldText

# def get_name ():
#     name = input('введите имя: ')
#     return name


# print(get_name())

