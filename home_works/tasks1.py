# """Функции задания"""

# # 1
# # Создать функцию, которая будет принимать 3 числа в качестве аргументов, функция должна возвращать сумму первых двух чисел разделеную на третье число
# # нужно реализовать проверку на то, что третье число не является нулем, если это ноль, то просто возвратить результат сложения первого и второго числа
# # def func(a, b, c):
# #   if c == 0:
# #     return a + b
# #   else:
# #     return (a + b) / c
  
# # print(f'{func(1, 2, 0)}')


# # 2
# # Создать фуункцию, которая принимает в качестве аргумента список со строками и в каком регистре нужно вернуть данные, строки могут быть записаны в любом регистре, задача: на основе выбора регистра, возвращать либо список со строками в верхнем регистре, либо в нижнем регистре
# # Например: func(["hEllo", "wORld"], "lower") -> ["hello", "world"]

# # def func(a, b):
# #     if b == 'upper':
# #         return [i.upper() for i in a]
# #     else:
# #         return [i.lower() for i in a]

# # print(func(["hEllo", "wORld"], "lower"))


# # 3
# # Создать функцию, которая будет принимать в качестве аргумента строку, а затем говорить сколько в ней и каких символов, результать вернуть в виде объекта
# # Например: 'Hello' -> {'H': 1, 'e': 1, 'l': 2, 'o': 1}

# # def func(a):
# #     result = {}
# #     for i in a:
# #         if i in result:
# #             result[i] += 1
# #         else:
# #             result[i] = 1
# #     return result

# # print(func('Hello'))

# 4
# # Создать калькулятор используя функции, должны быть доступны операции(+, -, /, *), также должна быть функция-менеджер, которая будет принимать 2 числа и операцию, а затем вызывать нужную функцию и возвращать результат

# # def calculate(a, b, op):
# #     if op == '+':
# #         return a + b
# #     if op == '-':
# #         return a - b
# #     if op == '*':
# #         return a * b
# #     if op == '/':
# #         return a / b
    
# # def manager(a, b, op):
# #     return calculate(a, b, op)

# # print(manager(1, 2, '+'))

# # 5
# # Создайте функцию, которая будет рассылать сообщения пользователям, сообщая о акции в магазине компьютерной техники, отправлять сообщения нужно только тем людям, которые тем или иным образом относятся к IT-сфере
# # users = [
# #   { 'name': 'Jack', 'age': 35, 'work': 'IT-backend developer' },
# #   { 'name': 'Helen', 'age': 35, 'work': 'Nurse' },
# #   { 'name': 'Bob', 'age': 35, 'work': 'Driver' },
# #   { 'name': 'Jessica', 'age': 35, 'work': 'IT-frontend developer' },
# #   { 'name': 'Hel\'ga', 'age': 35, 'work': 'IT-HR' }
# # ]

# # def messages(users):
# #     for user in users:
# #         if 'IT' in user['work']:
# #             print(user['name'], ' - ', user['work'])

# # messages(users)




# # 6
# # Создать функцию, которая будет принимать в качестве аргумента 2 строки, 1-я строка должна быть следующего вида -> '1200m', вторая строка состоит из величины, в которую необходимо преобразовать данные -> 'km', 'cm', 'mm', задача: реализовать логику, которая будет принимать например строку вида '2000m', и строку в которую нужно преобразовать величину например 'km', вывод должен быть '2km'


# # def func(a, b):
# #     a = int(a[:-1])
# #     if b == 'km':
# #         return str(a // 1000) + 'km'
# #     if b == 'cm':
# #         return str(a * 100) + 'cm'
# #     if b == 'mm':
# #         return str(a * 1000) + 'mm'

# # print(func('2000m', 'km'))



# # 7
# # Создать функцию, которая будет рассчитывать расход топлива автомобиля, будет принимать 2 аргумента 1-й сколько всего километров проехали, второй сколько понадобилось топлива на это, затем функция должна рассчитать сколько ушло топлива на 100 км и вернуть результат вида: 'На 100км было расходовано 10л горючего'


# # def func(a, b):
# #     return 'На 100км было расходовано ' + str(round(b / a * 100, 2)) + 'л горючего'
# # print(func(100, 10))



# # 8
# # Расчет премии сотрудникам
# # salary- это заработная плата в месяц, overTime- количество часов, которое сотрудник взял сверхурочно, задача: создать функцию, которая будет добавлять к основной зарплате сверхурочное время(1час=200$), функция должна принимать список со словарями и возвращать также список, но уже с измененными данными пример: [{'name': 'Jack', 'salary': 10000, 'overTime': 4}] -> [{'name': 'Jack', 'salary': 10800}]

# # employees = [
# #   {'name': 'Jack', 'salary': 10000, 'overTime': 4},
# #   {'name': 'Tom', 'salary': 15000, 'overTime': 3},
# #   {'name': 'Jessica', 'salary': 20000, 'overTime': 9},
# #   {'name': 'Helen', 'salary': 25000, 'overTime': 2},
# #   {'name': 'Peter', 'salary': 30000, 'overTime': 7}
# # ]
# # def over_time(employees):
# #     for employee in employees:
# #         employee['salary'] += employee['overTime'] * 200
# #     return employees 

# # print(over_time(employees))


# # 9
# # Создать функцию, которая в качестве аргумента будет принимать список со строками и числами, задача, отсортировать числа в отдельный список, а строки в отдельный и распечатать оба списка


# ls = ['one', 'two', '', 'list', '100', '12', 'din']
# res = []
# for x in ls:
#     if x.isdigit():
#         res.append(x)
#     else:
#      print(x)
# print(res,)



# 10
# # Создайте функцию, которая будет в качестве аргумента принимать список такого вида как указан выше, и будет возвращать отсортированный список (сортировать по убыванию оценок, используйте sort())
# students = [
#   {'student': 'Jack', 'marks': 43},
#   {'student': 'Tom', 'marks': 92}, 
#   {'student': 'Helen', 'marks': 85}, 
#   {'student': 'Peter', 'marks': 58},
#   {'student': 'Jessica', 'marks': 78}
# ]
# res = sorted(students, key=lambda x: x['marks'], reverse=True)
# print(res)

# 11
# Создайте функцию, которая будет принимать строку, а затем будет смотреть на все товары и возвращать только те, у которых в названии есть данная строка (учесть, что название может быть полным, а может быть частичным)
# products = [
#   {
#     'title': 'Samsung S10', 
#     'price': 800, 
#     'count': 6, 
#     'category': 'samsung'},
#   {
#     'title': 'iPhone 13 Pro', 
#     'price': 1200, 
#     'count': 9, 
#     'category': 'apple'},
#   {
#     'title': 'Xiaomi Mi 10', 
#     'price': 500, 
#     'count': 2, 
#     'category': 'xiaomi'},
#   {
#     'title': 'Samsung S9', 
#     'price': 600, 
#     'count': 4, 
#     'category': 'samsung'},
#   {
#     'title': 'iPhone 11', 
#     'price': 850, 
#     'count': 1, 
#     'category': 'apple'}
# ]
# res =  filter(lambda x: 'Samsung' in x['title'], products)
# print(list(res))

# 12
# # Используя из предыдущей задачи список с товарами, реализовать фильтрацию по категориям, функция должна в качестве аргумента принимать строку с категорией и возвращать список, в котором будут только те товары, у которых категория полностью совпадает с переданной



# res = filter(lambda x: x['category'] == 'samsung', products)
# print(list(res))

# 13
# # Создать счетчик расходов, есть некая переменная, которая будет хранить данные о вашем балансе, создать две функции, первая будет записывать расходы, вторая просто пополнять баланс, первая функция: ее основная задача получать 2 аргумента на что потрачено и сколько потрачено, дальше формировать словарь типа: {'target': 'Products', 'spend': 400}, затем сохранять эти данные в список и соответственно вычитать из баланса сумму трат, вторая функция просто получает в качестве аргумента сумму, которую нужно добавить на баланс, также необходимо реализовать проверку, достаточно ли средств на балансе для совершения расходов
# res = 0
# def spend(target, spend):
#     global res
#     res += spend
#     return res

# print(f' {spend("Products", 400)}')



# 14
# # Дан пустой список, необходимо использовать его в качестве базы данных для словарей типа {title: 'str', price: num, category: 'str'}, задача реализовать полный CRUD(create(должна быть возможность создавать данные, в нашем случае объекты), read(возможность получения/чтения данных), update(изменение данных(можно использовать индекс)), delete(удаление данных(можно использовать индекс))), за каждое действие должна отвечать отдельная функция


# ls = []
# CRUD = ['create', 'read', 'update', 'delete']

# # Define lambda functions
# create = lambda item: ls.append(item)
# read = lambda: ls
# update = lambda index, item: ls.__setitem__(index, item) if 0 <= index < len(ls) else None
# delete = lambda index: ls.pop(index) if 0 <= index < len(ls) else None

# # Test the CRUD operations
# create({'title': 'str', 'price': 10, 'category': 'str'})
# print(read())
# update(0, {'title': 'updated', 'price': 20, 'category': 'updated'})
# print(read())
# delete(0)
# print(read())



# """Comprehensions extra"""
# 8
# """
# Из списка 
# list1 = [44,54,64,74,104]
# Создайте новый list2, прибавив к каждому числу 6
# """
# list1 = [44,54,64,74,104]

# res = [x + 6 for x in list1]
# print(res)


# 9
# """Из списка
# list1 = [2, 4, 6, 8, 10, 12, 14]
# Создайте новый, внеся туда только те числа квадрат которых больше 50
# """
# res = list(filter(lambda x: x ** 2 > 50 , list1))
# print(res)


# 10
# """
# Из сторки string = "happy birthday!"
# Создайте список list_, внесите туда все символы из строки кроме пробела и '!'
 
# Вывод:
# ['h', 'a', 'p', 'p', 'y', 'b', 'i', 'r', 't', 'h', 'd', 'a', 'y']
# """

# string = "happy birthday!"
# list_ = list(filter(lambda x: x != ' ' and x != '!', string))
# print(list_)




# 11
# """
# Дан словарь:
# dict_ = {'a': {'d': 3, 'e': 45}, 'b': {'f': 23, 'j': 9}, 'c': {'h': 12, 'i': 89}}
# Используйте его чтобы создать список, из значений внутренних словарей

# Вывод:
# [3, 45, 23, 9, 12, 89]
# """


# dict_ = {'a': {'d': 3, 'e': 45}, 'b': {'f': 23, 'j': 9}, 'c': {'h': 12, 'i': 89}}

# list_ = []
# for i in dict_:
#     for j in dict_[i]:
#         list_.append(dict_[i][j])
# print(list_)



# 12
# """
# Из списка:
# list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ] 
# Создайте словарь, занесите только те имена, длина которых больше 4.
# Ключами будут имена, а значениями их длины, возведенные  
# в квадрат. 

# Вывод:
# {'george': 36, 'ringo': 25, 'patty': 25, 'cynthia': 49, 'linda': 25}
# """
# list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ] 
# res = { x: len(x) ** 2 for x in list_name if len(x) > 4}
# print(res)


# 13
# """
# Дан словарь
# dict_ = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Miivan": 1600, "Vann": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
# Пройдитесь по словарю и добавьте в список только те ключи, значение, которых
# в диапазоне от 200 до 5000, добавленные в список ключи должны быть в верхнем регистре.
# Нужно использовать comprehension.
# """
# dict_ = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Miivan": 1600, "Vann": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
# res = [x.upper() for x in dict_ if dict_[x] > 200 and dict_[x] < 5000]
# print(res)



# 14
# """
# Дан словарь:
# dict1 = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Miivan": 1600, "Vann": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
# Создайте словарь dict2:
# - Ключи должны быть те же, что и в первом словаре, но каждый символ 'i' замените на ''
# - Значением должно быть количество повторений символа 'i' в этом ключе

# Вывод:
# {'Sedan': 0, 'SUV': 0, 'Pckup': 1, 'Mvan': 2, 'Vann': 0, 'Sem': 1, 'Bcycle': 1, 'Motorcycle': 0}
# """

# dict1 = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Miivan": 1600, "Vann": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}
# res = {x.replace('i', ''): x.count('i') for x in dict1}
# print(res)



# 15
# """
# Из списка 
# list1 = [1, 2, 3, 0, None, 'a', 'abc', [], 23, [1, 2, 3, 4], '', {'a': 1, 'b': 2}, 'drf', []]
# Создайте новый list2, не добавляя все пустые значения(0, None, [], {}, '') 

# Вывод:
# [1, 2, 3, 'a', 'abc', 23, [1, 2, 3, 4], {'a': 1, 'b': 2}, 'drf']
# """

# list1 = [1, 2, 3, 0, None, 'a', 'abc', [], 23, [1, 2, 3, 4], '', {'a': 1, 'b': 2}, 'drf', []]

# res = [x for x in list1 if x]
# print(res)



# 16
# """
# Дан список SPL_Patrons. Каждый его подсписок содержит две части информации
# о посетителях библиотеки:
# - имя посетителя
# - количество книг, которые они одолжили за последний год
# Используйте list comprehension, 
# чтобы создать список readers имен меценатов, 
# которые в прошлом году одолжили более 100 книг


# SPL_Patrons = [
# ['Kim Tremblay', 134],
# ['Emily Wilson', 42],
# ['Jessica Smith', 215],
# ['Alex Roy', 151],
# ['Sarah Khan', 105],
# ['Samuel Lee', 220],
# ['William Brown', 24],
# ['Ayesha Qureshi', 199],
# ['David Martin', 56],
# ['Ajeet Patel',69]
# ]

# res = [x[0] for x in SPL_Patrons if x[1] > 100]
# print(res)


# Вывод:
# ['Kim Tremblay', 'Jessica Smith', 'Alex Roy', 'Sarah Khan', 'Samuel Lee', 'Ayesha Qureshi']
# """



# 17
# """
# Из предыдущего списка SPL_Patrons:
# предположим, что посетитель экономит в среднем 11,95 доллара, 
# одалживая книгу вместо того, чтобы покупать ее. 
# Используйте list comprehension, чтобы создать список saved_amount 
# сэкономленной суммы для каждого клиента


# SPL_Patrons = [
# ['Kim Tremblay', 134],
# ['Emily Wilson', 42],
# ['Jessica Smith', 215],
# ['Alex Roy', 151],
# ['Sarah Khan', 105],
# ['Samuel Lee', 220],
# ['William Brown', 24],
# ['Ayesha Qureshi', 199],
# ['David Martin', 56],
# ['Ajeet Patel',69]
# ]

# res = [x[1]*11.95 for x in SPL_Patrons]
# print(res)

# Вывод:
# [1601.3, 501.9, 2569.25, 1804.45, 1254.75, 2629.0, 286.79, 2378.05, 669.19, 824.55]
# """



# 18
# """
# Используйте comprehensions для создания списка из списков, 
# где каждый подсписок состоит из имени пирата и стоимости 
# его / ее награбленных мешков с зерном 
# (рассчитайте стоимость зерна, предположим, 
# что средняя рыночная стоимость мешка зерна составляет 42 доллара, 
# но включите только тех пиратов, которые любят попугаев)

# prairie_pirates = [
# ['Tractor Jack', 1000, True],
# ['Plowshare Pete', 950, False],
# ['Prairie Lily', 245, True],
# ['Red River Rosie', 350, True],
# ['Mad Athabasca McArthur', 842, False],
# ['Assiniboine Sally', 620, True],
# ['Thresher Tom', 150, True],
# ['Cranky Canola Carl', 499, False]
# ]

# Вывод:
# [['Tractor Jack', 42000], ['Prairie Lily', 10290], ['Red River Rosie', 14700], ['Assiniboine Sally', 26040], ['Thresher Tom', 6300]]
# """

# res = [x for x in prairie_pirates if x[2] == True]
# print(res)




# 19
# """
# По данному ниже словарю, пройдитесь циклом
# - Найдите сумму лайков всех пользователей, рейтинг которых выше 3
# используйте list comprehension

# dict_ = {
#     'Sasha': {
#         'likes': 23,
#         'comments': 2,
#         'rating': 4
#     },
#     'Aliya': {
#         'likes': 34,
#         'comments': 5,
#         'rating': 5
#     },
#     'Dasha': {
#         'likes': 15,
#         'comments': 3,
#         'rating': 2
#     },
#     'Luna': {
#         'likes': 12,
#         'comments': 2,
#         'rating': 1
#     },
#     'Rena': {
#         'likes': 26,
#         'comments': 7,
#         'rating': 2
#     }
# }

# res = sum([x['likes'] for x in dict_.values() if x['rating'] > 3])
# print(res)
# Вывод:
# 57
# """



# 20
# """
# Используя приведенный словарь dict_, создайте список из id, 
# которые хранятся под ключом comments. Берите только те комментарии, 
# количество которых больше 3

dict_ = {
    'Dasha': {
        'likes': 15,
        'comments': [
            {'id': 1, 'text': 'some text'},
            {'id': 2, 'text': 'some text'},
        ],
        'rating': 2
    },
    'Luna': {
        'likes': 12,
        'comments': [
            {'id': 1, 'text': 'some text'},
            {'id': 2, 'text': 'some text'},
            {'id': 3, 'text': 'some text'},
        ],
        'rating': 1
    },
    'Rena': {
        'likes': 26,
        'comments': [
            {'id': 1, 'text': 'some text'},
            {'id': 2, 'text': 'some text'},
            {'id': 3, 'text': 'some text'},
            {'id': 4, 'text': 'some text'},
            {'id': 5, 'text': 'some text'},
            {'id': 6, 'text': 'some text'},
        ],
        'rating': 2
    }
}

res = [x['id'] for x in dict_['Rena']['comments'] if x['id'] > 3 and x['text'] == 'some text' ]
print(res)

# Вывод:
# [1, 2, 3, 4, 5, 6]
# """