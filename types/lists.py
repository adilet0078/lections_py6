# list() -(списки, массив) - изменямый, последовательный тип данных, который представляет набор элементов(каких-либо объктов) внутри себя

# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 

# my_list = [1, 'str', 'hello', False , None, [1, 2, 3 ]]

# print(list)
# print(my_list, type(my_list))

# range() - возвращает последовательность чисел от start до stop (с шагом step)
# num = range(1, 101)
# print(num)
# ls = list(num)
# print(ls, type(ls))

# ls = list('hello world')
# print(ls)


# индексаация в списках 
# ls =[1, 2, 3, 4, 5, 'string', [True, False, None ], 5]
# print(ls, len(ls))
# print(ls[5], ls[-1])
# print(ls[6][0])
# print(ls[3:6])

# i = 0
# while i < 5 :
#     print(i)
#     i += 1

# ls = range(0, 11)
# for num in ls:
#     print(num)

# ls = [ 'John', 'Tiron', 'Sara', 'Eddartr', 'Jamie']
# for name in ls:
#     print(name)
# for x in ls:
#     print(f'Hellomr/mrs {x}! Welcome to our party!')

# for num in range(1, 20):
#     # print(num)
#    if num % 2 == 0:
  
#     print(f'число {num} четное, куб: {num ** 2}')
#    else:
#     print(f'число {num} четное, куб: {num ** 3}') 

# методы списков 
# print(dir(list))
 
# append(element) - добавляет элемент в конец списка
# ls = [1, 2, 3, 4, 5]
# ls.append(6)
# ls.append(7)
# ls.append(8)
# ls.append('hello')
# ls.append([True , False])
# print(ls)

#  extend(container) - расщирает список на указанное количество элементов
# ls = [1, 2, 3, ]
# ls.extend('HELLO')
# print(ls)
# ls.extend([True, False])
# print(ls)

# ls = [1, 2, 3]
# ls1 = [4, 5, 6]
# print(ls + ls1)

# # insert(index, element) - добавляет элемент по указанному индексу
# ls = [1, 2, 3, 4, 5]
# ls.insert (4, 'hello world')
# # ls.insert(2, 'hello')
# print(ls)
 
# from random import randint
# ls = []
# for x in range (1, 101):
#     ls.append(randint(1, 100))
   
#     print(ls)  
#     ls = list (set(ls))
# ls.sort()
# print('After:/n',ls )

# remove - удаляет указанный элемент из списка
# pop([index])- удаляет последний элемент из списка , при этом возвращается удаленный элемент по index, но если индекс не обьялен то удаляет последний элемент
# ls = [5, 1, 2, 3, 4, 5, 5, 5]
# print(ls)
# ls.remove(5) 
# print(ls)

# while 5 in ls:
#     ls.remove (5)
#     print(ls)

# ls.pop()
# print(ls)
# ls.pop(0)
# print(ls)
# ls = [1, 2, 3]
# deleted = ls.pop()
# print(ls)
# print(deleted)
# update-------------------
# update = [1, 2, 't', 3, 4, 5, 6, None, 8]
# update[2] = 3
# print(update)
# I = update.index(None)
# update[I] = 7 
# print(update)