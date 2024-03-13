# Ассосация - принцип ООП, в котором два класса связаны друг с другом . Связь обозначает то что внутри одного объекта будет существовать другой объект от другого класса.
# агрегации -слабая связь 

# композиция - сильная связь 
# class Batery:
#     _power = 100

#     def charge(self):
#         if self._power < 100:
#             self._power += 10
#             self._power = 100

# class Iphone:
#     def __init__(self, color) -> None:
#         self.color = color
#         self.battery = Batery()
#         # когда мы создаем внутри класса объект от другого класса - композиция

# a = Iphone('black')
# print(a.battery._power)
# a.battery._power -= 50
# print(a.battery._power)
# a.battery.charge()
# print(a.battery._power)
# del a
# print(a.battery._power)

# class Nokia:
#     def __init__(self, color, battery) -> None:
#         self.color = color
#         self.battery = battery
#         # агрегация -  когда объект создается из вне класса и передается внутрь - агрегация

# battery = Batery()
# nokia  = Nokia('white', battery)
# print(nokia.battery._power)
# del nokia
# # print(nokia.battery._power)

# nokia2 = Nokia('black', battery)
# # при удалении обьекта Nokia, ,batery остается 
# print(nokia2.battery._power)