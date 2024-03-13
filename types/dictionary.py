# dic - словарь -> упорядоченная коллекция элементов, которая хранит пары "ключ-значение"(python 3.7->ordered). 

# ассациятивный масссив, hash table, object(js), structure == dictionary(py)

# ключами могут быть только неизменяемые типы данных и в словаре сохраняются только уникальнык ключи 
# тогда как значениями могут выступать любые типы данных любые значения

# thisdict = {
#     'brand': 'Ford',
#     'model': 'Mustang',
#     'year': 1967
# }
# ls = ['Ford', 1967, 'Mustang']
# print(thisdict, type(thisdict))
# print(thisdict['year'])

# thisdict['motor'] = 'GTI Turbo'
# thisdict['model'] = 'fiesta'
# print(thisdict)

# ----------------------------------------

# print(dir(dict))
# # items, keys, values 

# user_info = {
# #     'first_name': 'John',
#     # 'last_name': 'Snow',
#     'age': 24,
#     'email': '5QkQj@example.com',
#     'role': 'admin'
# }
# print(user_info)
# ls = list(user_info.keys())
# print(ls)
# ls2 = list(user_info.values())
# print(ls2)
# ls3 = list(user_info.items())
# print(ls3)
print('/nValues:')
# for value in user_info.values():
#     print(value)

# print('/nKeys:')
# for key in user_info.keys():
#     print(key)

# print('/nItems:')
# for key,value  in user_info.items():
#     print(f'keys: {key} ,values: {value}')


# изменение 
# dict_ = {'name': 'John', 'age': 24}
# print(dict_)
# dict_['name'] = 'Jack'
# dict_['address'] = 'WinterFell'
# print(dict_)
# dict_.update(age=17, address ='BlackCastle' )
# print(dict_)
# dict_.update({'name': 'John Snow', })
# print(dict_)  
 
# dict_ = {1: 'Pizza',2:'Burger', 3: 'Steak'}
# print(dict_[3], '!!!')
# print(dict_.get(5, 'Not found'))

# dict_ = {1: 'banana', 2: 'pineapple', 3: 'apple'}
# print(dict_.get (2))
# print(dict_.get(4, 'Not found'))

# setdefault() - работает так же как и get(), но если ключа нет то он создает его и присваивает значение по умолчанию

# dict_ = {1: 'banana', 2: 'pineapple', 3: 'apple'}
# print(dict_.setdefault(5, 'mango'))
# print(dict_)

# -------------------
# создание - fromkeys()
# ls = list(range(1, 20))
# new_dict = dict.fromkeys(ls, 'default')
# print(new_dict)

# -------------------
# удаление элементов
# pop, popitem, del

# pop('<key>') - удаляет элемент по ключу
# popitem() - удаляет последний пару 
# del <key> - удаляет элемент по ключу

# dict_ = {'name': 'john': 'last_name': 'snow' 'age': 24}
# print(dict_)
# removed = dict_.pop('last_name')
# print(dict_)
# print(removed)
# # print('-----------------------------')
# print  = dict_.popitem()
# print(dict_)
# print(removed)


# roles = {
#     1: 'Admin',
#     2: 'User',
#     3: 'Moderator'
# }
# users = {
#   55:{
#     'id': 55, 'role': roles[3], 'username': 'Tiron'},
#       12: {
#     'id': 12, 'role': roles[1], 'username': 'John Snow'},
#     4: {
#     'id': 4, 'role': roles[2], 'username': 'Raychel'}}
# print(users)

# product = {
#     'id': 1,
#     'title': 'samsung galaxy s23 ultra',
#     'description': 'loren ipsum',
#     'price': 10000,
# }
# print(product)
# id_user = int(input('vvedite id:'))
# if users[id_user]['role'] == roles [1]:
#     product['description'] = input('vvedite opisanie:') 
# else:
#  print('you don/t have permission')
# print()
# print(product)

