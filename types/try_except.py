# обработка исключий 
# операторы try......except
# ошибки errors - синтаксические ошибки связанные с кодом
# syntaxErrror
#  indentationError
# TabError

# Исключение  exceptions -> связаны с непрвильными данными которые передаются в код, операции
# ZeroDivisionError
# ArithmeticError
# NameError
# IndexError
# ValueError
# BaseException прородитель всех исключений
# KeyError
# from optparse import Values


# try:
#     num1 = int(input('enter the number1 '))
#     num2 = int(input('enter the number 2 '))
#     print(f' {num1}/ {num2} = {num1 / num2}')
# except: 
#     print('invalid Values')
#     print('very ecpesailly')

# try:
#     num1 = int(input('enter the number1 '))
#     num2 = int(input('enter the number 2 '))
#     print(f' {num1}/ {num2} = {num1 / num2}')
# except ValueError:
#     print('you entered the wrong info')
# except ZeroDivisionError:
#     print('na nol delit nelza')

# print('ecspecially valuable ingo')    

# try:
#   <body>      # код с вероятным исключением
# except:
# <body>        #срааботает только если ошибка в try 
# <else> :
# <body>  сработает только если нет ошибки в try 
# <finally>:  
# <body>  срабатывает в любом случаи 

# from multiprocessing.sharedctypes import Value


# dict_ = {1: 'one', 2 : 'two', 3: "three"}

# try:
#     key = int(input('enter the key'))
#     print(dict_)
# except ValueError:
#     print('invalid value for key!') 
# except KeyError:
#     print('key doesnt existst')   
# else: 
#     print('no errors')
# finally :
#     print('the end!')

# ------------------------
# отоображения ошибки 

# 1, import sys 
# import sys 
# ls = [1, 2, 3, 4, 5]
# try:
#     index = int(input('enter the index'))
#     print(ls [index])
# except:
#      print(f'oops we catched {sys.exc_info()[0]} error!')

# 2. exception as <name(e)>


# ls = [1, 2, 3, 4, 5]
# while True :
#     try:
#         index = int(input('enter the index'))
#         print(ls [index])
#     except Exception as e: 
#         print(f'oops we catched  {e.__class__} error!')


   




