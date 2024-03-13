
# Created: 2024-01-08 10:00
# Deadline: 2024-02-27 18:00
# Max score: 100

# 1. Напишите класс Subscriber, у которого есть переменные экземпляра:
#         firstname
#         lastname
#         Сделайте так, чтобы метод __repr__ возвращал firstname + lastname
# 2. Напишите класс Provider, у которого есть:
#         переменный экземпляра name -- название провайдера
#         переменный экземпляра subscribers -- список, в котором будут храниться экземпляры класса Subscriber
#         переменный экземпляра payments -- словарь, ключём которого является экземпляр класса Subscriber, значением 
#         является сумма (вещественное число)
        # метод register_payment, который принимает экземпляр класса Subscriber, и сумму, затем проверяет, есть ли такой экземпляр Subscriber в списке subscribers. 
#             Если есть, записывает экземпляр в словарь payments в качестве ключа, а сумму в качестве значения
#             Если нет, выкидывает (raise) ошибку ValueError
# 3. Напишите класс Terminal, у которого есть
#         переменная экземпляра amount = 0
#         переменная экземпляра providers = [ ]
#         Регистрировать провайдера через метод register, который принимает экземпляр класса Provider и добавляет в providers
#         Принимать деньги в счет провайдера (pay), который принимает экземпляр класса Provider, экземпляр класса Subscriber и сумму (вещественное число). Внутри метода должен вызываться метод register_payment экземпляра класса Provider. register_payment успешно сработал, то в переменую amount нужно добавить сумму.

# class Subscriber:
#     def __init__(self, firstname, lastname):
#         self.firstname = firstname
#         self.lastname = lastname
    
#     def __repr__(self):
#         return f"{self.firstname} {self.lastname}"


# class Provider:
#     def __init__(self, name):
#         self.name = name
#         self.subscribers = []
#         self.payments = {}

#     def register_payment(self, subscriber, amount):
#         if subscriber in self.subscribers:
#             if subscriber in self.payments:
#                 self.payments[subscriber] += amount
#             else:
#                 self.payments[subscriber] = amount
#         else:
#             raise ValueError("Subscriber not found in the list of subscribers.")

# class Terminal:
#     def __init__(self):
#         self.amount = 0
#         self.providers = []

#     def register(self, provider):
#         self.providers.append(provider)

#     def pay(self, provider, subscriber, amount):
#         if provider in self.providers:
#             provider.register_payment(subscriber, amount)
#             self.amount += amount
#         else:
#             raise ValueError("Provider not found in the list of registered providers.")

# # Создаем объекты Subscriber
# subscriber1 = Subscriber("John", "Doe")
# subscriber2 = Subscriber("Jane", "Smith")

# # Создаем объект Provider
# provider = Provider("Example Provider")
# provider.subscribers.append(subscriber1)
# provider.subscribers.append(subscriber2)

# # Регистрируем провайдера в терминале
# terminal = Terminal()
# terminal.register(provider)

# # Делаем платежи
# terminal.pay(provider, subscriber1, 50.0)
# terminal.pay(provider, subscriber2, 75.0)

# # Проверяем сумму в терминале
# print(terminal.amount)  # Выведет: 125.0

# # Проверяем сумму по платежам
# print(provider.payments[subscriber1])  # Выведет: 50.0
# print(provider.payments[subscriber2])  # Выведет: 75.0