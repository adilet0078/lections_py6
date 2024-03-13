# # # Типы данных числа -> int, float

# # # =  -> оператор присваивание 
# # num  = 5
# # print(num) # 5
# # num = 79  # переопределение 
# # print(num) # 79  
# # num += 1 # num += 1 
# # print(num) # 80
# # num -= 5 
# # print(num) # 75

# # abc -> нижний регистр
# # ABC -> верхний регистр

# # PEP8
# # tomorrow_day = "11.01.2024" # snake_case
# # tomorrow_Day = "11.01.2024" # camelCase

# # +
# num1 = 5 
# num2 = 15 
# result = num1 + num2
# print(result)

# # -
# num1 = int(input("Enter the num1: "))
# num2 = int(input("Enter the num2: "))
# print(num2, "-", num1, "=", num2 - num1)

# # * 
# num1 = int(input("Enter the num1: "))
# num2 = int(input("Enter the num2: "))
# print(num2, "*", num1, "=", num2 * num1)

# # / and // and % 
# / - обычное деление
# // -деление без остатка(целочисленное деление)
# % - остаток от деления (модулное деление)
 
# num1 = 17 
# num2 = 5
# print("/", num1 / num2)
# print("//", num1 // num2)
# print("%", num1 % num2) 
 
# ** -> возведение в степень 

# print(5 ** 2)
# print(17 ** 55)

# print(144 ** 0.5)  #квадратный корень 
# print(36 ** 0.5)   # (1/2)

# res = 5 * (15 +5)                                                                                     
# print(res)

# pow - возведение в степень
# (pow(num1, num2, <mod>)
# print(pow(5, 2))     #5 ** 2
# print(pow(5, 2, 2))  #5 ** 2 % 2

# a = 6 
# c = 3
# res = pow(a, c , 50)
# print(res)

# abc() - абсолютное значение числа -> abc (-5) -> 5
#                                        # |-5| -> 5

# a = abs(-16)
# b = abs(15)
# c = abs(-2.5)
# print(a, b, c)

# round() - округление число до определенного количества знаков после запятой(с плавающей точ)
# a = 5.57 
# print(round(a))
 
# b = 5.43269
# print(round(b, 2)) 

# divmod(a, b) - она выводит два числа, первое число это результат целого деление//, ф второе это модулное деление чисел a и b
 
# print(22/5) # 4.4 
# print(divmod(22, 5))

# import math
# from random import randint 

# a = 5 
# print(round(math.sqrt(a),1))

# множественное присваивание 
# a = "milk"
# b = "water"
# c = None
# c = b 
# b = a 
# a = c 
# print(a, b)

# a = "milk" 
# b = "water"
# a, b = b, a 
# print(a, b)

# num1, num2, num3 = input("num1: "), input("num2: "), input("num3: ")
# print(num1)
# print(num2)
# print(num3)

# import math
# katet1 = 5 
# katet2 = 6 
# gipotenuza =math.sqrt (katet1 ** 2 + katet2 ** 2) 
# print(round (gipotenuza, ))

# from math import pi 
# r = int(input("Enter the r: "))
# resP = 2 * pi * r
# resS = pi * r ** 2
# print('S okrujnosti: ', round(resS, 2))
# print('P okrujnosti: ', round(resP, 2))

# from random import randint
# num = randint (1, 10)
# print(num)

# num =  randint(1, 10) # 5 
# print(num)
# i = 0
# while i < 3:
#     guess = int(input("guess the number: ")) # 5
#     if guess == num:
#         print("you win!")
#         i = 3
#     i += 1

