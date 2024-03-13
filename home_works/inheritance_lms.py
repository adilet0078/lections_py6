

# # """1) Создайте класс Auto в нем реализуйте метод ride который выводит сообщение Riding on a ground, создайте класс Boat реализуйте метод swim, который выводит floating on water.
# # Создайте класс Amphibian который наследуется от класса Auto и Boat. Создайте от него объект и вызовите все методы.
# # """

# # # class Auto():
# # #     def ride(self):
# # #         print("Riding on a ground")

# # # class Boat():
# # #     def swim(self):
# # #         print("Floating on water")

# # # class Amphibian(Auto, Boat):
# # #     pass

# # # amphibian = Amphibian()
# # # amphibian.ride()
# # # amphibian.swim()


# # # 

# # """2) Создайте класс RadioMixin в нем реализуйте метод для проигрывания музыки play_music который принимает в себя название песни. Создайте класс Auto, Boat, Amphibian и расширьте функционал этих классов при помощи миксина"""


# # # class RadioMixin:
# # #     def play_music(self, song):
# # #         print(f"Playing {song}")

# # # class Auto:
# # #     def ride(self):
# # #         print("Riding on a ground")

# # # class Boat:
# # #     def swim(self):
# # #         print("Floating on water")

# # # class Amphibian(Auto, Boat, RadioMixin):
# # #     pass

# # # amphibian = Amphibian()
# # # amphibian.ride()
# # # amphibian.swim()
# # # amphibian.play_music("Happy")




# # """3) Будильник
# # Создайте класс Clock, у которого будет метод показывающий текущее время и класс Alarm, с методами для включения и выключения будильника.
# # Далее создайте класс AlarmClock, который наследуется от двух предыдущих классов. Добавьте к
# # нему метод для установки будильника, при вызове которого должен включатся будильник."""

# # # class Clock():
# # #     def show_time(self, time):
# # #         print("Current time: 12:00")

# # # class AlarmClock(Clock):
# # #     def on(self):
# # #         print("Alarm is on")

# # #     def off(self):
# # #         print("Alarm is off")

# # # alarm = AlarmClock()
# # # alarm.show_time("12:00")
# # # alarm.on()
# # # alarm.off()




# # """4) Разработчики
# # Напишите класс Coder с атрибутами experience, count_code_time = 0 и абстрактными методами
# # get_info и coding.
# # Создайте классы Backend и Frontend, которые наследуют все атрибуты и методы от класса Coder. Класс Backend должен принимать дополнительно параметр languages_backend, а Frontend — languages_frontend соответственно.
# # Переопределите в обоих классах методы get_info и coding (так, чтобы он принимал количество часов кодинга и при каждом вызове этого метода добавлял это значение к count_code_time). 
# # Так же бывают FullStack разработчики и
# # поэтому создайте данный класс и чтобы у него были атрибуты и методы предыдущих классов. Создайте несколько экземпляров от классов Backend, Frontend, FullStack и вызовите их методы."""

# # # class Coder:
# # #     def __init__(self, experience):
# # #         self.experience = experience
# # #         self.count_code_time = 0

# # #     def get_info(self):
# # #         print(f"Experience: {self.experience}")

# # # class Backend(Coder):
# # #     def __init__(self, experience, languages_backend):
# # #         super().__init__(experience)
# # #         self.languages_backend = languages_backend

# # #     def coding(self, hours):
# # #         self.count_code_time += hours
# # #         print(f"Code time: {self.count_code_time}")

# # # class Frontend(Coder):
# # #     def __init__(self, experience, languages_frontend):
# # #         super().__init__(experience)
# # #         self.languages_frontend = languages_frontend

# # #     def coding(self, hours):
# # #         self.count_code_time += hours
# # #         print(f"Code time: {self.count_code_time}")

# # # class FullStack(Coder):
# # #     def __init__(self, experience, languages_backend, languages_frontend):
# # #         super().__init__(experience)
# # #         self.languages_backend = languages_backend
# # #         self.languages_frontend = languages_frontend

# # #     def coding(self, hours):
# # #         self.count_code_time += hours
# # #         print(f"Code time: {self.count_code_time}")


# # # coder = Coder(5)
# # # backend = Backend(5, "Python")
# # # frontend = Frontend(5, "JavaScript")
# # # fullstack = FullStack(5, "Python", "JavaScript")

# # # coder.get_info()
# # # backend.coding(5)
# # # frontend.coding(5)
# # # fullstack.coding(5)
# # # -------------------------------------------------------------------------------------------------------------
# # # from abc import ABC, abstractmethod

# # # class Coder(ABC):
# # #     def __init__(self, experience=0, count_code_time=0):
# # #         self.experience = experience
# # #         self.count_code_time = count_code_time

# # #     @abstractmethod
# # #     def get_info(self):
# # #         pass

# # #     @abstractmethod
# # #     def coding(self, hours):
# # #         pass

# # # class Backend(Coder):
# # #     def __init__(self, experience=0, count_code_time=0, languages_backend=None):
# # #         super().__init__(experience, count_code_time)
# # #         self.languages_backend = languages_backend

# # #     def get_info(self):
# # #         return f"Backend Developer with {self.experience} years of experience. Languages: {self.languages_backend}"

# # #     def coding(self, hours):
# # #         self.count_code_time += hours
# # #         print(f"Coding in Backend. Total code time: {self.count_code_time} hours.")

# # # class Frontend(Coder):
# # #     def __init__(self, experience=0, count_code_time=0, languages_frontend=None):
# # #         super().__init__(experience, count_code_time)
# # #         self.languages_frontend = languages_frontend

# # #     def get_info(self):
# # #         return f"Frontend Developer with {self.experience} years of experience. Languages: {self.languages_frontend}"

# # #     def coding(self, hours):
# # #         self.count_code_time += hours
# # #         print(f"Coding in Frontend. Total code time: {self.count_code_time} hours.")

# # # class FullStack(Backend, Frontend):
# # #     def __init__(self, experience=0, count_code_time=0, languages_backend=None, languages_frontend=None):
# # #         Backend.__init__(self, experience, count_code_time, languages_backend)
# # #         Frontend.__init__(self, experience, count_code_time, languages_frontend)

# # #     def get_info(self):
# # #         return f"FullStack Developer with {self.experience} years of experience. Backend Languages: {self.languages_backend}. Frontend Languages: {self.languages_frontend}"

# # # # Создание экземпляров
# # # backend_dev = Backend(experience=3, languages_backend=["Python", "Java"])
# # # frontend_dev = Frontend(experience=2, languages_frontend=["HTML", "CSS", "JavaScript"])
# # # fullstack_dev = FullStack(experience=5, languages_backend=["Python", "Java"], languages_frontend=["HTML", "CSS", "JavaScript"])

# # # # Вызов методов
# # # print(backend_dev.get_info())
# # # backend_dev.coding(8)

# # # print(frontend_dev.get_info())
# # # frontend_dev.coding(6)

# # # print(fullstack_dev.get_info())
# # # fullstack_dev.coding(10)

# # # Sanzhar Shadybekov, [2024/2/23 14:25]
# # # Создайте класс мобильного телефона. Определите атрибуты для imei, уровня заряда батареи, краткой информации об установленной ОС. Изначальный уровень заряда
# # # батареи – 100%, он не может опуститься ниже 0. Методы доступа к данным расходуют 0,5 % заряда при каждом обращении.
# # # Определите 2 метода: для прослушивания музыки, и для просмотра видео.
# # # При каждом прослушивании музыки расходуется 5% заряда, а при просмотре видео – 7%.
# # # Если заряд достигает уровня ниже 10% - не давайте пользователю просматривать видео. При
# # # полной разрядке все методы телефона не доступны (выбрасывайте ошибку, что телефон
# # # разряжен).
# # # Также предусмотрите возможность заряжания батареи.
# # class MobilePhone:
# #     def __init__(self, imei, os_info):
# #         self.imei = imei
# #         self.battery_level = 100
# #         self.os_info = os_info

# #     def get_battery_level(self):
# #         self._consume_battery()
# #         return self.battery_level

# #     def play_music(self):
# #         if self.battery_level <= 0:
# #             raise Exception("Phone is discharged. Please charge the phone.")
# #         self._consume_battery(5)
# #         return "Playing music..."

# #     def watch_video(self):
# #         if self.battery_level <= 0:
# #             raise Exception("Phone is discharged. Please charge the phone.")
# #         if self.battery_level < 10:
# #             raise Exception("Battery level too low to watch video. Please charge the phone.")
# #         self._consume_battery(7)
# #         return "Watching video..."

# #     def charge_battery(self, amount):
# #         if self.battery_level <= 0:
# #             raise Exception("Phone is discharged. Please charge the phone.")
# #         self.battery_level = min(100, self.battery_level + amount)

# #     def _consume_battery(self, percentage=0.5):
# #         if self.battery_level <= 0:
# #             raise Exception("Phone is discharged. Please charge the phone.")
# #         self.battery_level = max(0, self.battery_level - percentage)

# # # Пример использования:

# # phone = MobilePhone("123456789", "Android 12")

# # print(phone.get_battery_level())  # Output: 99.5
# # print(phone.play_music())         # Output: Playing music...
# # print(phone.get_battery_level())  # Output: 94
# # phone.charge_battery(50)
# # print(phone.get_battery_level())  # Output: 100
# # print(phone.watch_video())        # Output: Watching video...
# # print(phone.get_battery_level())  # Output: 93

# import pygame
# import time
# import random

# pygame.init()

# # Определение цветов
# white = (255, 255, 255)
# yellow = (255, 255, 102)
# black = (0, 0, 0)
# red = (213, 50, 80)
# green = (0, 255, 0)
# blue = (50, 153, 213)

# # Определение размеров экрана и ячеек
# dis_width = 800
# dis_height = 600
# dis = pygame.display.set_mode((dis_width, dis_height))
# pygame.display.set_caption('Змейка')

# clock = pygame.time.Clock()

# snake_block = 10
# snake_speed = 15

# font_style = pygame.font.SysFont(None, 50)

# # Определение функции, рисующей змейку на экране
# def our_snake(snake_block, snake_list):
#     for x in snake_list:
#         pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

# # Определение функции вывода сообщения на экран
# def message(msg, color):
#     mesg = font_style.render(msg, True, color)
#     dis.blit(mesg, [dis_width / 6, dis_height / 3])

# # Основной игровой цикл
# def gameLoop():
#     game_over = False
#     game_close = False

#     x1 = dis_width / 2
#     y1 = dis_height / 2

#     x1_change = 0
#     y1_change = 0

#     snake_list = []
#     length_of_snake = 1

#     foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
#     foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

#     while not game_over:

#         while game_close == True:
#             dis.fill(blue)
#             message("Вы проиграли! Нажмите Q-Выход или C-Новая Игра", red)
#             pygame.display.update()

#             for event in pygame.event.get():
#                 if event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_q:
#                         game_over = True
#                         game_close = False
#                     if event.key == pygame.K_c:
#                         gameLoop()

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 game_over = True
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_LEFT:
#                     x1_change = -snake_block
#                     y1_change = 0
#                 elif event.key == pygame.K_RIGHT:
#                     x1_change = snake_block
#                     y1_change = 0
#                 elif event.key == pygame.K_UP:
#                     y1_change = -snake_block
#                     x1_change = 0
#                 elif event.key == pygame.K_DOWN:
#                     y1_change = snake_block
#                     x1_change = 0

#         if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
#             game_close = True
#         x1 += x1_change
#         y1 += y1_change
#         dis.fill(blue)
#         pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
#         snake_head = []
#         snake_head.append(x1)
#         snake_head.append(y1)
#         snake_list.append(snake_head)
#         if len(snake_list) > length_of_snake:
#             del snake_list[0]

#         for x in snake_list[:-1]:
#             if x == snake_head:
#                 game_close = True

#         our_snake(snake_block, snake_list)

#         pygame.display.update()

#         if x1 == foodx and y1 == foody:
#             foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
#             foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
#             length_of_snake += 1

#         clock.tick(snake_speed)

#     pygame.quit()
#     quit()

# gameLoop()
