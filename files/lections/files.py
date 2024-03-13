# Работа с файлами 

# каретка - указатель - курсор

# open('путь до файла)
# file = open('files.py') # относительный путь
# ~working -> Desktop/py.6/files/lections/files.py
# files working -> lections/files.py

# path = '/home/adilet/Desktop/py.6/files/lections/files.py'
# files.py # абсолютный путь
# file = open(path, 'r')
# data = file.read()
# print(data, type(data))
# file.close()

# режими работы с файлами 
# 1) r/r+/rb -> read - для чтение файлов  
# 2) w/w+/wb -> write - для записи в файл
# 3) a/a+ -> append - для добавления в файл
#  b , x  

# file = open('test.txt', 'r')
# print(file.read())
# file.close()

# file = open('test.txt', 'r')
# print(file.readlines())
# file.close()

# # контекстный менеджер with
# with open ('test.txt', 'r') as file:
#     print(file.readline())
#     print(file.readline())
#     # print(file.readline())
#     print('!!!!')
#     print(file.readline())

# file.tell() # (позиция курсора) возвращает индекс где находится каретка (курсор)(указатель)
# file.seek(0) # перемещение курсора в (начало файла) индекс который вы передали 

# with open('test.txt', 'r') as file:
#     print(file.tell()) #0
#     data = file.read()
#     print(data, '!!')
#     print(file.tell()) # 9
#     file.seek(0) # 0
#     data = file.read()
#     print(data, '!!')
#     print(file.tell()) # 9

# with open('test.txt', 'w') as file:
#     file.write('Hello World!\n')
#     file.write("My name is John Snow \n")
#     file.write("I\'m Ned Stark bastard\n") 
#     file.seek(0)
#     data = ['Test 1 stroka\n , Test 2 stroka\n ']
#     file.writelines(data)

# with open('test.txt', 'a+') as f:
#     f.write('\n John is a king of the North \n')
#     f.write('I\'m Ned Stark ')
#     f.seek(0)
#     f.read()
#     print(f.read())
#-------------------------------------------------
# from PIL import Image
# import pytesseract
# import re

# base_url = '/home/adilet/Desktop/py.6/files/lections/'


# def get_imei_codes(image_path: str):
#     string = pytesseract.image_to_string(image_path)
#     # print(string)
#     list_of_imei = re.findall(r'IMEI\d.\s\d+', string)
#     print(list_of_imei)
    
#     with open ('imei_codes.txt', 'w') as file:
#         file.writelines(f'{x}\n' for x in list_of_imei)

# image_path = base_url + 'imei.jpg'
# get_imei_codes(image_path)

