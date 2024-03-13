

"""
1. Создайте класс BankAccount, в конструкторе которого определена переменная
экземпляра класса balance = 0. Определите метод withdraw с параметром amount,
который будет отнимать сумму от баланса и возвращать текущий баланс. Также
добавьте метод deposit, который также имеет параметр amount и соответсвенно
добавляет сумму к балансу, возвращает баланс.
"""
# class BankAccount:
#     def __init__(self):
#         self.balance = 0

#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Недостаточно средств на счете!")
#             return self.balance
#         self.balance -= amount
#         return self.balance

#     def deposit(self, amount):
#         self.balance += amount
#         return self.balance

# # Пример использования класса BankAccount
# account = BankAccount()
# print("Начальный баланс:", account.balance)

# account.deposit(100)
# print("После депозита:", account.balance)

# account.withdraw(50)
# print("После снятия:", account.balance)

# account.withdraw(100)  # Попытка снять больше, чем есть на счете
# print("После неудачного снятия:", account.balance)


"""
2. Вам дан такой код:

winner1 = Nobel("Литература", 1971, "Пабло Неруда")
print(winner1.category, winner1.year, winner1.winner)
print(winner1.get_year())

winner2 = Nobel("Литература", 1994, "Кэндзабуро Оэ")
print(winner2.category, winner2.year, winner2.winner)
print(winner2.get_year())

который выводит в терминал такие значения:

Литература 1971 Пабло Неруда
выиграл 50 лет назад

Литература 1994 Кэндзабуро Оэ
выиграл 27 лет назад

Напишите класс Nobel и метод класса get_year() таким образом, чтобы данный вам код вывел указанные значения в терминале. Даты внутри класса не хардкодить.
# """
# class Nobel:
#     def __init__(self, category, year, winner):
#         self.category = category
#         self.year = year
#         self.winner = winner

#     def get_year(self):
#         current_year = 2023  # Assuming the current year is 2023
#         age = current_year - self.year
#         return f"выиграл {age} лет назад"
    

# winner1 = Nobel("Литература", 1971, "Пабло Неруда")
# print(winner1.category, winner1.year, winner1.winner)
# print(winner1.get_year())

# winner2 = Nobel("Литература", 1994, "Кэндзабуро Оэ")
# print(winner2.category, winner2.year, winner2.winner)
# print(winner2.get_year())

"""
3. Создайте класс Password, экземеплярами класса являются пароли в виде строк. У класса должен быть метод validate для валидации пароля:
- пароль должен быть минимум 8 символов, но меньше 15
- пароль должен содержать цифры
- пароль должен содержать буквы
- пароль должен содержать хотя бы один из символов:
    '@', '#', '&', '$', '%', '!', '~', '*'

если одно из условий не выполнено, выводите кастомное исключение, 
если же все условия выполнены метод validate должен возвращать строку: 'Ваш пароль сохранен'.

Также переопределите метод str, чтобы при попытке распечатать
сам пароль, вам выдавалась строка из звездочек,
к примеру пароль - 'joe@123456'
в терминале выйдет - ******
"""

# class Password:
#     def __init__(self, password):
#         self.password = password

#     def validate(self):
#         if len(self.password) < 8 or len(self.password) > 15:
#             raise ValueError("Password must be between 8 and 15 characters long.")
#         if not any(char.isdigit() for char in self.password):
#             raise ValueError("Password must contain at least one digit.")
#         if not any(char.isalpha() for char in self.password):
#             raise ValueError("Password must contain at least one letter.")
#         if not any(char in ['@', '#', '&', '$', '%', '!', '~', '*'] for char in self.password):
#             raise ValueError("Password must contain at least one special character.")
#         return "Ваш пароль сохранен."

#     def __str__(self):
#         return "*" * len(self.password)
    

# password = Password("joe@123456")
# print(password)

"""
4. Создайте класс Math, экземпляром которого должно быть число.
У классa Math должно быть 3 метода:
- get_factorial - выводит факториал числа
- get_sum - выводит сумму цифр числа
- get_mul_table - выводит таблицу умножения для числа до 10. Создайте экземпляр класса и примените к нему все методы. 
"""

# class Math:
#     def __init__(self, number):
#         self.number = number

#     def get_factorial(self):
#         factorial = 1
#         for i in range(1, self.number + 1):
#             factorial *= i
#         return factorial

#     def get_sum(self):
#         sum = 0
#         for digit in str(self.number):
#             sum += int(digit)
#         return sum

#     def get_mul_table(self):
#         for i in range(1, 11):
#             print(f"{self.number} * {i} = {self.number * i}")


# number = int(input("Enter a number: "))
# math = Math(number)
# print(math.get_factorial())
# print(math.get_sum())
# math.get_mul_table()
"""
5. Создайте класс ToDo, экземплярами данного класса являются строки-задачи(сходить в кино, сделать домашку, выгулять собаку и.т.д)

У класса есть метод give_priority который записывает вашу задачу в список(переменная класса) с ключом в виде числа, 
приоритет который вы даете вашей задаче -
к примеру {3: 'сходить в кино'}
приоритет сходить в кино у вас не самый высокий.

У класса должен быть метод list_of_tasks, который выдает вам список отсортированных задач 
по приоритету:
[(1, 'сделать домашку'), (2, 'выгулять собаку'), (3, 'сходить в кино')]

# """

# class ToDo:
#     tasks = {}

#     def give_priority(self, task):
#         priority = len(self.tasks) + 1
#         self.tasks[priority] = task
#         return self.tasks

#     def list_of_tasks(self):
#         sorted_tasks = sorted(self.tasks.items(), key=lambda x: x[0])
#         return sorted_tasks
    

# todo = ToDo()
# todo.give_priority("сходить в кино")
# todo.give_priority("сделать домашку")
# todo.give_priority("выгулять собаку")
# print(todo.list_of_tasks())

