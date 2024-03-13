# 1) Дан список list_ = [1, 2, 3, 4]. Выведите сумму всех этих чисел.
# list_ = [1, 2, 3, 4]
# res = sum(list_)
# print(res)

# """
# # писать код здесь



# """
# 2) Дан списка из чисел. Проверьте, что все числа больше трёх.
# """
# # писать код здесь
# """
# def chek_numbers_generate(list):
#     for i in list:
#         if i < 3:
#             return False
#     return True

# print(chek_numbers_generate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))



# 3) Даны список из чисел. Проверьте, что в нём есть отрицательные числа.

# """
# # писать код здесь

# def chek_num(list):
#     res = any(i < 0 for i in list)
#     return res
# print(chek_num([1, 2, 3, 4, 5, 6, 7, 8, 9, -10]))


# 4) Дан список, состоящий из числами. Создайте новый список, состоящий из квадратов этих чисел.
# ls = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# res =  [i**2 for i in ls]
# print(res)


# """
# # писать код здесь
# """
# 5) Дан список с числами. Отфильтруйте этот список, оставив только чётные числа.
# ls = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# res = filter(lambda x: x % 2 == 0 ,ls)
# print(list(res))
# # писать код здесь



# """
# 6) Дан список, со строками. Отфильтруйте этот список, оставив только те строки, длина которых больше 7 символов.
# """
# # писать код здесь
# ls = ['hello', 'world', 'python', 'is', 'great', 'expectation'] 
# res = filter(lambda x: len(x) > 7 ,ls )
# print(list(res))

# """
# 7) Дан список list_ = [5, 6, 7, 8]. Выведите произведение всех этих чисел.
# """
# # писать код здесь

# from functools import reduce
# list_ = [5, 6, 7, 8]
# res =reduce(lambda x, y: x * y, list_)
# print(res)


# 8ю Дан список, с числами. Посчитате количество чётных и нечётных чисел в этом списке.
# """
# # писать код здесь


# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# res = filter(lambda x: x % 2 == 0 ,list_)
# print(len(list(res)))



# 9) Дан список list_ = [-1, 2, 3, 0, 5, -3, 7,]. Если число в списке меньше 0, замените его на False, если больше, то на True .

# list_ = [-1, 2, 3, 0, 5, -3, 7,]
# res = map(lambda x: x > 0, list_)
# print(list(res))



# 10) Дан список из имён. Найдите самое длинное имя из списка функцией reduce.
# """
# # писать код здесь

# from functools import reduce
# names = ['Helen', 'Peter', 'Jessica']
# res = reduce(lambda x, y: x if len(x) > len(y) else y, names)
# print(res)