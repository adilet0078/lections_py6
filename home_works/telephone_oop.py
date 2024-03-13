# Создайте класс мобильного телефона. Определите атрибуты для imei, уровня заряда батареи, краткой информации об установленной ОС. Изначальный уровень заряда
# батареи – 100%, он не может опуститься ниже 0. Методы доступа к данным расходуют 0,5 % заряда при каждом обращении.
# Определите 2 метода: для прослушивания музыки, и для просмотра видео.
# При каждом прослушивании музыки расходуется 5% заряда, а при просмотре видео – 7%.
# Если заряд достигает уровня ниже 10% - не давайте пользователю просматривать видео. При
# полной разрядке все методы телефона не доступны (выбрасывайте ошибку, что телефон
# разряжен).
# Также предусмотрите возможность заряжания батареи.

# class MobilePhone:
#     def __init__(self, imei, os_info):
#         self.imei = imei
#         self.battery_level = 100
#         self.os_info = os_info

#     def __str__(self):
#         return f"IMEI: {self.imei}, Battery Level: {self.battery_level}%, OS: {self.os_info}"

#     def __battery_consumption(self, percentage):
#         if self.battery_level <= 0:
#             raise ValueError("Phone is discharged")
#         self.battery_level -= percentage
#         if self.battery_level < 0:
#             self.battery_level = 0

#     def play_music(self):
#         self.__battery_consumption(5)
#         return "Playing music..."

#     def watch_video(self):
#         if self.battery_level < 10:
#             return "Battery level is too low to watch video"
#         self.__battery_consumption(7)
#         return "Watching video..."

#     def charge_battery(self, percentage):
#         if self.battery_level <= 0:
#             raise ValueError("Phone is discharged")
#         self.battery_level += percentage
#         if self.battery_level > 100:
#             self.battery_level = 100
#         return f"Battery charged by {percentage}%"

# # Пример использования:

# phone = MobilePhone("1234567890", "Android 12")
# print(phone)  # Вывод: IMEI: 1234567890, Battery Level: 100%, OS: Android 12

# print(phone.play_music())  # Вывод: Playing music...
# print(phone.battery_level)  # Вывод: 95

# print(phone.watch_video())  # Вывод: Watching video...
# print(phone.battery_level)  # Вывод: 88

# phone.charge_battery(20)
# print(phone.battery_level)  # Вывод: 100

# phone.charge_battery(10)  # ValueError: Phone is discharged
