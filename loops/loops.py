# Циклы - это конструкция которая заставляет какой-то блок кода выполнятся несколько раз 

# while <expression>:
#     <body>
# моржевой оператор ':='


# while smt := input('enter something') 
# print(smt)


# while (smt := input('enter something')) == 'ok':
#     print(smt) 

# i = 1
# while (name1 :=  input('imia1:')) != 'John' or \
# ((name2 :=  input('imia2:')) != 'Raichel'):
#     print()

#     if i >= 5 :
#         print('цикл остановлен!')
#         break         #пренудительная остановка 
#         i += 1 
#     else:
#         print(f'вы угадали {name1}, {name2}')

# user = {'username': 'JohnSnow', 'password': 'bastard123'}
# i = 3 
# while passsword := input(F'{user["username"]} vvedite parol\':') != user['password']:
#     i -= 1 
#     if i == 0 :
#         print('vy zablokirovany')
#         break 
#     else:
#         print(f'{user["username"]} vy zashli v sistemu!')



#-------------------------------------



# for <variable > in <iterable object>:
   #<body>
# ls = ['a', 'hello', '55','66', '77', True]
# i = iter(ls)
# print(i)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))


# from random import randint

# dict_= {}
# for x in  range(1, 21):
#     dict_.update({x :randint(1, 50)})
    
# # print(dict_)

# ls = ['Tiron', 'Bilal', 'John', 'Sansa', 'Jamie', 'Eddart']
# for x in ls :
#     if x.startswith('J'):
#         continue
#     print(f'Hello mr/mrs {x}!')

