# task 1 Опишите полный синтаксис конструкции try-except:


# try:
    # <body>  # код, который нужно выполнить
# except:
    # <body>  # код, который выполняется при возникновении исключения
# else:
    # <body>  # код, который выполняется при отсутствии исключений
# finally:
    # <body>  # код, … выполняется в любом случае


# task 2 . Дан следующий код:
# b = 10
# c = 11
# print(a)
# Обработайте ошибку, которая может возникнуть. 
# try:
#     b = 10 
#     c = 11 
#     print(a)
# except Exception as e:
#     print('a is not defined {e.__class__}')
    
    
# task 3) Напишите программу которая будет получать два числа через input и делить одно на другое. Обработайте ошибку, которая возникнет в случае, если второе число окажется 0 и выведите сообщение.
# try: 
#     num1 = int(input('enter the number1 '))
#     num2 = int(input('enter the number 2 '))
#     print(f'{num1}/{num2} == {num1 / num2}')
# except ZeroDivisionError:
#     print('the number cannot be divided by 0 ')    


# task 4 ) Напишите программу, которая будет получать через инпут 2 числа и будет печатать их сумму. Обработайте ошибку, которая возникнет, если пользователь введёт не числовое значение и выведите сообщение.

# try:
#     num1 = int(input('enter the number1'))
#     num2 = int(input('enter the number2'))
#     print(f'{num1}+{num2} == {num1 + num2}')

# except ValueError:
#     print('значение не числовое. Введите число')

# 5) Дан словарь. Попытайтесь получить значение по ключу. Обработайте ошибку, возникающую в том случае, если запрашиваемый ключ не существует.
# dict = {1 : 'a', 2 : 'd', 3 : 'i'}
# try:
#     key = int(input('enter the key'))   
#     print(dict[key])
# except KeyError:
#     print('the key doesnt exist')


# task 6)  Дан список. Обработайте исключение при попытке обращения к несуществующему элементу.

# ls = [1, 2, 3, 4, 5]
# try:
#     num = int(input('enter the number'))
#     print(ls[num])
# except IndexError:
#     print('the index doesnt exist')

# task 7) Попытайтесь в блоке try принять 2 числа и разделить одно на другое. В блоке except обработайте сразу 2 возможных исключения.
# try:
#     num1 = int(input('enter the number1'))
#     num2 = int(input('enter the number2'))  
#     print(f'{num1}/{num2} == {num1/ num2} ')
# except ZeroDivisionError:
#     print('the number cannot be divided by 0 ')
# except ValueError:
#     print('ivalid value')    

# task 8 😍 Запросите у пользователя сумму, которая у него сейчас есть в бумажнике. Если он введёт сумму, меньшую чем 0, то выбросите исключение с текстом "Сумма не может быть отрицательной!"

# sum = int(input('enter the sum that you have'))
# if sum < 0:
#     raise ValueError('Сумма не может быть отрицательной!')
# else:
#     print('great!')


# task 9)  В блоке try запросите у пользователя ввод его возраста. Затем в том же блоке проверьте его возраст на совершеннолетие. Если пользователь несовершеннолетний, выбросите исключение с текстом "Доступ запрещён". Обработайте также исключение если пользователь вводит текст вместо числа с сообщением 'Введен некорректный возраст'. Если ошибок не возникло, то распечатайте сообщение "Спасибо!", а затем "До свидания", вне зависимости от того, произошла ошибка или не

# try :
#     age = int(input('enter your age'))
#     if age < 18:
#         print(ValueError('Доступ запрещён'))
# except ValueError:
#     print('Введен некорректный возраст') 
# else:
#     print('спасибо!')
#     print('до свидания')


