# task 1 

# Даны списки:

# a = [1, 1, 2.3, 3, -5, 8, -13, -21, 34.5, 55, 89];

# b = [1, 2.3, 3, 4, -5, 6, 7, 8, 9, -10, 11, -12, -13, 34.5].

# Нужно вернуть список, который состоит из элементов, общих для этих двух списков.

# Продолжите работать с этим списком:

# Используя функции и методы которые прошли на уроке:

# Все отрицательные числа "вырезать" и вставить в новый список negative_list, не изменяя основной (общий) список и распечатать список negative_list
# Всем отрицательным числам  в списке negative_list вернуть абсолютное значение
# Возвести в степень 3, первый и последний элементы в общем списке

# a = [1, 1, 2.3, 3, -5, 8, -13, -21, 34.5, 55, 89]
# b = [1, 2.3, 3, 4, -5, 6, 7, 8, 9, -10, 11, -12, -13, 34.5]

# # Finding common elements in the two lists
# common_elements = list(set(a) & set(b))

# # Printing the common elements
# print("Common elements:", common_elements)

# # Creating a new negative_list with all negative numbers
# negative_list = [num for num in a + b if num < 0]

# # Printing the negative_list
# print("Negative numbers:", negative_list)

# # Returning absolute value to all negative numbers in negative_list
# absolute_values = [abs(num) for num in negative_list]

# # Printing the absolute values
# print("Absolute values of negative numbers:", absolute_values)

# # Raising the first and last elements of the general list to the power of 3
# a[0] = a[0]**3
# a[-1] = a[-1]**3

# # Printing the modified list
 # print("Modified list with first and last elements raised to the power of 3:", a)

# task 2
# banknote_dict = {
#     1: 'Abdylas Maldybaev',
#     5: 'Bubusara Beishenalieva',
#     10: 'Kasym Tynystanov',
#     20: 'Togolok Moldo',
#     50: 'Kurmanjan Datka',
#     100: 'Toktogul Satylganov',  # Added 100 som banknote
#     200: 'New Figure for 200 som',  # Placeholder for the 200 som banknote
#     500: 'New Figure for 500 som',  # Placeholder for the 500 som banknote
#     1000: 'New Figure for 1000 som'  # Placeholder for the 1000 som banknote
# }

# # Replace Benjamin Franklin with Toktogul Satylganov
# banknote_dict[1] = 'Toktogul Satylganov'

# # Ask the user for the denomination of the banknote
# denomination = int(input("Enter the denomination of the banknote: "))

# # Display the name of the figure on the corresponding banknote
# try:
#     figure_name = banknote_dict[denomination]
#     print(f"The figure on the {denomination} som banknote is: {figure_name}")
# except KeyError:
#     print("Error: This denomination does not exist.")


# task 3
# def get_day_name(day_number):
#     days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
#     return days[day_number - 1]


# day_number = int(input("Enter the day of the week number (1-7): "))
# hours_worked = int(input("Enter the number of hours worked (0-8): "))

# if 1 <= day_number <= 7 and 0 <= hours_worked <= 8:
#     day_name = get_day_name(day_number)
#     remaining_hours = 8 - hours_worked

#     if day_number == 5 and remaining_hours < 2:
#         print(f"Today is {day_name}.")
#         print(f"There is {remaining_hours} hour left to work.")
#         print("You can leave early!")
#     else:
#         print(f"Today is {day_name}.")
#         print(f"There are {remaining_hours} hours left to work.")
# else:
#     print("Invalid input. Please enter valid values.")

# task 4 
# # Get input from the user
# number = int(input("Enter a number: "))

# # Check if the number is two-digit or not
# if 10 <= number <= 99:
#     print("The number is two-digit.")
# else:
#     print("The number is not two-digit.")


# task 5 

# rating = int(input('What did you get in math? '))

# if rating == 2 or rating == 3:
#     print('Bad. March to study!')
# elif rating == 4 or rating == 5:
#     print('Well done! You can rest now.')

# task 6 
# original_list = [1, '2', 3, 4, '5', 'six', 'seven']
# modified_list = [int(item) if str(item).isdigit() else ord(item.lower()) - ord('a') + 1 for item in original_list]
# total_sum = sum(modified_list)
# print("Sum of all items:", total_sum)
# even_numbers = [num for num in modified_list if num % 2 == 0]
# odd_numbers = [num for num in modified_list if num % 2 != 0]
# print("Even numbers:", even_numbers)
# print("Odd numbers:", odd_numbers)
