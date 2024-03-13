#  1 Напишите программу,
# которая генерирует случайное число  от 1 до 100,
# а затем предлагает пользователю угадать это число.
# Программа должна предоставить подсказки о том,
# больше или меньше введенное число загаданного.


# Task 1
# import random
# hiden_number =random.randint(1, 100)
# print("Guess the number ", hiden_number)
# while True :
#     guess = int(input())
#     if guess > hiden_number:
#         print("Too high")
#     elif guess < hiden_number:
#         print("Too low")
#     else:
#         print("You guessed!")
#         break


# # Task 2
# import time


# Напишите программу, которая преобразует температуру из градусов Цельсия в градусы Фаренгейта и наоборот.
# Позвольте пользователю выбирать тип преобразования 
# ”””

# def celsius_to_fahrenheit(celsius):
#      """Converts temperature from Celsius to Fahrenheit
#      Args: 
#      celcius(float):temperature in celsius
#      return:temperature in fahrenheit.
#      """
#      return (celsius * 9 / 5) + 32
# def fahrenheit_to_celsius(fahrenheit):
#      """Converts temperature from Fahrenheit to Celsius
#      Args: 
#      fahrenheit(float):temperature in fahrenheit
#      return:temperature in celsius.
#      """
#      return (fahrenheit - 32) * 5 / 9
# conversion_type = input("Choose conversion type (1 for Celsius to Fahrenheit, 2 for Fahrenheit to Celsius): ")
# if conversion_type == "1":
#      celcius = float(input("Enter temperature in Celsius:"))
#      fahrenheit = celsius_to_fahrenheit(celcius)
#      print(f"{celcius}°C is equal to {fahrenheit}°F")
# elif conversion_type == "2":
#      fahrenheit = float(input("Enter temperature in Fahrenheit:"))
#      celcius = fahrenheit_to_celsius(fahrenheit)
#      print(f"{fahrenheit}°F is equal to {celcius}°C")
# else:
#      print("Invalid input")   


# task 3 Реализуйте программу, которая рассчитывает ежемесячные выплаты по ипотеке.
#  Пользователь должен ввести сумму кредита,
# годовую процентную ставку и срок кредита. 
# Программа должна вывести ежемесячную выплату.

# def calculate_monthly_payment(loan_amount, annual_interest_rate, loan_term):
#     monthly_interest_rate = annual_interest_rate / 12 / 100
#     total_payments = loan_term * 12

#     # Calculate the monthly payment using the formula
#     # P = (r * A) / (1 - (1 + r)^(-n))
#     # where P is the monthly payment, r is the monthly interest rate, A is the loan amount, and n is the total number of payments
#     monthly_payment = (monthly_interest_rate * loan_amount) / (1 - (1 + monthly_interest_rate) ** -total_payments)

#     return monthly_payment

# # Get input from the user
# loan_amount = float(input("Enter the loan amount: "))
# annual_interest_rate = float(input("Enter the annual interest rate (%): "))
# loan_term = int(input("Enter the loan term (years): "))

# # Calculate the monthly payment
# monthly_payment = calculate_monthly_payment(loan_amount, annual_interest_rate, loan_term)

# # Print the result
# print("Monthly mortgage payment: $", round(monthly_payment, 2))

# Task 5  Попросите пользователя ввести количество часов,
#  а затем выведите эквивалентное количество минут.

# # Ask the user to enter the number of hours
# hours = int(input("Enter the number of hours: "))
# # calculate the equivalent number of minutes
# minutes = hours *60 
# # print the equivalent number of minutes 
# print("Equivalent number of minutes :", minutes)

# Task 6  Запросите у пользователя цену товара и количество единиц товара,
#  а затем выведите общую стоимость.
 
# # Ask the user to enter the price of the product
# price = float(input("Enter the price of the product: "))
# # Ask the user to enter the number of units
# units = float(input("Enter the number of units: "))
# # calculate the total cost 
# total_cost = price * units
# # display the total cost 
# print("total cost:", total_cost)

# Task 7  Количество дней в годах: Введите возраст пользователя и выведите, сколько дней он прожил (учитывая невисокосные года).

# # Ask the user to enter their age 
# age = int(input("Enter your age: "))
# # calculate the days they have lived
# days = age * 365 
# # display the number of days they have lived
# print("Number of days they have lived:", days)

# Task 8 Попросите пользователя ввести количество дней, а затем выведите, сколько это недель и сколько дней осталось.

# # Ask the user to enter the number of days
# days = int(input("Enter the number of days: "))

# # Calculate the number of weeks and remaining days
# weeks = days // 7
# remaining_days = days % 7

# # Display the result
# print("Equivalent number of weeks:", weeks)
# print("Remaining number of days:", remaining_days)

# Task 9 Extra. Создайте игру "Камень-ножницы-бумага" с компьютером. Пользователь вводит свой выбор, а программа генерирует случайный выбор компьютера.
# import random 
# # Define the choices
# choices = ["rock", "paper", "scissors"]
# # ask the users for their choice 
# ucer_choice = input("Enter your choice (rock, paper, scissors): ")
# # Generate a random choice for the computer
# computer_choice = random.choice (choices)
# # Determine the winner
# if ucer_choice == computer_choice:
#     print("It's a tie!")
# elif ucer_choice == "rock" and computer_choice == "scissors":
#     print("You win!")
# elif ucer_choice == "paper" and computer_choice == "rock":
#     print("You win!")
# elif ucer_choice == "scissors" and computer_choice == "paper":
#     print("You win!")
# else:
#     print("You lose!") 

# Task 4
#  Напишите программу,
# которая генерирует первые n чисел в последовательности Фибоначчи,
# где n вводится пользователем.

# def generate_fibonacci_sequence(n):
#     sequence = [0, 1]
#     for i in range(2, n):
#         next_number = sequence[i - 1] + sequence[i - 2]
#         sequence.append(next_number)
#     return sequence

# n = int(input("Enter the number of terms: "))
# sequence = generate_fibonacci_sequence(n)
# print(sequence)

# n = int(input("enter the number n : "))
# # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55 ....]
# # 4
# default = [0, 1] 
# if n <= 2: 
#     print(default)
# else:
#     i = 2 
# while i < n:
#     res = default[-1] + default[-2]
#     default.append(res)
#     i += 1
# print(default)