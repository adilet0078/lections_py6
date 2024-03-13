# 1. Напишите класс MyList, который наследуется от list. Сделайте так, чтобы индексация
# элементов начиналась с 1. Например:
# x = MyList([1,2,3,4,5])
# x[1] → 1
# class MyList(list):
#     def __getitem__(self, index):
#         # Сдвигаем индекс на 1, если он больше нуля
#         if isinstance(index, int) and index > 0:
#             index -= 1
#         # Делегируем операцию получения элемента родительскому классу
#         return super().__getitem__(index)

# x = MyList([1, 2, 3, 4, 5])
# print(x[1])  # Выведет: 1
 

# 2. Напишите класс Word и переопределите методы 'больше чем', 'меньше чем', 'больше или равно', 'меньше или равно' для сравнения объектов класса - строк по длине(len). 
# Также в методе new напишите условие для удаления
# пробелов и пустых строк в созданных словах.
# print('15'<'ABC')
# class Word(str):
#     def __new__(cls, obj):
#         obj =obj.replace(' ', '')
#         return super().__new__(cls, obj)
    
#     def __init__(self, obj):
#         super().__init__()
#         self.obj = obj 

#     def __gt__(self, other):
#         print('gt worked')
#         print(self, '---', other)
#         if len(self) >len(other):
#             return self
#         elif len(self) <len(other):
#             return other
#         else:
#             return "eq"
        
#     def __lt__(self, other) -> bool:
#         return len(self) < len(other)
    
#     def __eq__(self, other) -> bool:
#         return len(self) == len(other)
    

# obj = Word('     hello junior')
# obj2 = Word('dream codify')

# print(obj > obj2)
# print(obj < obj2)
# print(obj == obj2)

# 3. Создайте класс BankAccount, представляющий банковский счет. Реализуйте магические методы init, str, add и sub, чтобы поддерживать инициализацию счета, вывод информации о счете и операции пополнения и снятия средств.

# class BankAccount:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.balance = balance
    
#     def __str__(self):
#         return f"Bank account of {self.owner} with balance: {self.balance}"
    
#     def __add__(self, amount):
#         self.balance += amount
#         return f"Amount {amount} deposited. New balance is {self.balance}"
    
#     def __sub__(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             return f"Amount {amount} withdrawn. New balance is {self.balance}"
#         else:
#             return "Insufficient funds"
        

# # Пример использования:
# account = BankAccount("John Doe", 1000)
# print(account)  # Выведет: Bank account of John Doe with balance: 1000

# print(account + 500)  # Выведет: Amount 500 deposited. New balance is 1500
# print(account - 200)  # Выведет: Amount 200 withdrawn. New balance is 1300

# print(account - 1500)  # Выведет: Insufficient funds
