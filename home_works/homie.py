# EXTRA TASKS:
# Модуль time в Python включает в себя несколько очень полезных функций
# для работы со временем. Одна из таких функций – asctime – считывает
# текущее системное время компьютера и возвращает его в удобном для
# восприятия виде. Используйте эту функцию для отображения на экране
# текущей даты и времени. Никакого ввода от пользователя на этот раз вам
# не потребуется.
# ---------
# Создайте программу, в которой пользователь сможет ввести временной
# промежуток в виде количества дней, часов, минут и секунд и узнать общее
# количество секунд, составляющее введенный отрезок.
# ---------
# Для этого упражнения вам необходимо будет написать программу, кто то будет запрашивать у пользователя расстояние в футах. После этого
# она должна будет пересчитать это число в дюймы, ярды и мили и вывес­
# ти на экран. Коэффициенты для пересчета единиц вы без труда найдете
# в интернете.

# day = int(input('enter the number of days:'))
# hour = int(input('enter the number of hours:'))
# minute = int(input("enter the number of minutes:"))
# seconds = int(input('enter the number of seconds'))
# # calculate the number of seconds
# total_seconds = day * 24 * 60 * 60 + hour * 60 * 60 + minute * 60 + seconds
# print(total_seconds)

# # inches, yards and miles
# feet = float(input("Enter the distance in feet: "))
# # convert inches to feet
# inches = feet *12 

# # convert to yards 
# yards = inches /36 
 
# # convert to miles
# milles = feet / 5280

# res = inches, yards, milles
# print(res)