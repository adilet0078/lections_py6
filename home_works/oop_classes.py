

"""

1) Создайте класс Class1 с 2 любыми методами. Создайте второй класс Class2, который наследуется от Class1, и определите в новом классе ещё 2 метода. Создайте экземпляр класса Class2. И вызовите у него все 4 метода.

"""

# class Class1:
#     def method1(self):
#         print("Основной функционал")

#     def method2(self):
#         print("Дополнительный функционал")

# class Class2(Class1):
#     def method3(self):
#         print("Основной функционал")

#     def method4(self):
#         print("Дополнительный функционал")

# class2 = Class2()
# class2.method1()
# class2.method2()
# class2.method3()
# class2.method4()
"""

2) Создайте класс A и определите в нём метод method1, который будет печатать строку "Основной функционал". Затем создайте второй класс B, который наследуется от класса A, и дополните method1 таким образом, чтобы он печатал также строку "Дополнительный функционал". Объявите экземпляр класса B и вызовите метод method1.

"""

# class A:
#     def method1(self):
#         print("Основной функционал")

# class B(A):
#     def method1(self):
#         super().method1()
#         print("Дополнительный функционал")

# b = B()
# b.method1()


"""

3) Создайте класс MyString, который будет наследоваться от str. Определите 2 своих метода:

append, который будет принимать строку и добавлять её в конец исходной

pop, который удаляет из строки последний элемент и возвращает его.

Пример:

# example = MyString('String')

# example.append('hello')

# print(example) -> 'Stringhello'

# print(example.pop()) -> 'o'

# print(example) -> 'Stringhell'

# """
# class MyString(str):
#     def append(self, string_to_append):
#         """Добавляет строку string_to_append в конец текущей строки."""
#         self = self + string_to_append
#         return MyString(self)
       
#     def pop(self):
#         """Удаляет и возвращает последний элемент строки."""
#         popped_char = self[-1]
#         self = self[:-1]
#         return popped_char, MyString(self)

# # Пример использования:
# example = MyString('String')
# example = example.append('hello')
# print(example)  # Output: 'Stringhello'
# popped, example = example.pop()
# print(popped)  # Output: 'o'
# print(example)  # Output: 'Stringhell'    


"""

4) Создайте класс MyDict который будет наследоваться от встроенного класса dict. Переопределите метод .get() таким образом, чтобы при попытке получении несуществующего ключа по умолчанию он вовзращал строку 'Are you kidding?' вместо None.

"""

# class MyDict(dict):
#     def get(self, key, default="Are you kidding?"):
#         if key in self:
#             return self[key]
#         else:
#             return default

# my_dict = MyDict({'a': 1, 'b': 2})
# print(my_dict.get('a'))  # Output: 1
# print(my_dict.get('c'))  # Output: 'Are you kidding?'

"""

5) Создайте класс Person который будет описывать человека, а точнее его имя и возраст. Создайте метод display(), который будет выводит данные об этом человеке.

Создайте второй класс Student, который будет наследоваться от класса Person, он должен принимать все атрибуты, которые были определены в родительском классе и добавьте еще один атрибут, который будет описывать направление студента. Создайте метод display_student(), который будет выводить данные об этом студенте.

Объявите экземпляр класса Student, и выведите данные о нём, как о человеке, затем как о студенте.

"""

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display(self):
#         print(f"Name: {self.name}, Age: {self.age}")

# class Student(Person):
#     def __init__(self, name, age, course):
#         super().__init__(name, age)
#         self.course = course

#     def display_student(self):
#         super().display()
#         print(f"Course: {self.course}")

# student = Student("John", 20, "Computer Science")
# student.display_student()


"""

6) Создайте класс ContactList, который должен наследоваться от встроенного класса list. В нем должен быть реализован метод search_by_name, который должен принимать имя и возвращать список всех совпадений. Создайте экземпляр класса all_contacts и передайте список ваших контактов.

"""

# class ContactList(list):
#     def search_by_name(self, name):
#         return [contact for contact in self if contact['name'] == name]

# all_contacts = ContactList([
#     {'name': 'John', 'phone': '123-456-7890'},
#     {'name': 'Jane', 'phone': '987-654-3210'},
#     {'name': 'Bob', 'phone': '555-555-5555'},
# ])

# print(all_contacts.search_by_name('Jane'))
"""

7. Создайте класс Smartphone, экземпляры класса должны иметь такие свойства - name, color, memory, battery. battery по умолчанию

должно быть 0. Переопредилите метод str так чтобы при распечатке он выдавал строку с названием и памятью смартфона.

У данного класса также должен быть метод charge, который увеличивает значение батареи на указанную величину.

 

Создайте два дочерних класса от Smartphone - Iphone и Samsung.

У Iphone должен быть дополнительный аттрибут - ios и метод send_imessage - возвращает строку с сообщением и от какого телефона оно было выслано.

А у Samsung должен быть дополнительный аттрибут android и метод show_time, который показывает текущее время.

Создайте объекты от данных классов и примените все методы.

"""

# class Smartphone:
#     def __init__(self, name, color, memory, battery=0):
#         self.name = name
#         self.color = color
#         self.memory = memory
#         self.battery = battery

#     def __str__(self):
#         return f"{self.name} {self.memory}"

#     def charge(self, battery):
#         self.battery += battery

#     def send_imessage(self, message):
#         return f"{message} {self.name}"
    

# class Iphone(Smartphone):
#     def __init__(self, name, color, memory, ios):
#         super().__init__(name, color, memory)
#         self.ios = ios

#     def send_imessage(self, message):
#         return f"{message} {self.ios}"
    

# class Samsung(Smartphone):
#     def __init__(self, name, color, memory, android):
#         super().__init__(name, color, memory)
#         self.android = android

#     def show_time(self):
#         return f"{self.name} {self.android}"
    

# iphone = Iphone("iPhone", "blue", 128, "iOS 15")
# samsung = Samsung("Samsung", "black", 256, "Android 11")


# print(iphone)
# print(samsung)
 

"""

8. Создайте класс Spell для магических заклинаний, экземпляры класса имеют два аттрибута - name - название и formula - полное произношение заклинания.

 

У класса есть два метода: get_description() - дает полное описание заклинания и execute() - совершает заклинание.

 

Переопределите у класса метод str, чтобы он выдавал вам название, формулу и описание вместе, к примеру:

 

Открытие замков: Alohomora

позволяет магу попасть в любую комнату,

способно открыть любую закрытую замочную скважину.

 

Наследуя от класса Spell создайте три заклинания,переопределяя в них родительские методы. Создайте объекты этих трех заклинаний. Вызовите все методы

"""
# class Spell:
#     def __init__(self, name, formula):
#         self.name = name
#         self.formula = formula

#     def get_description(self):
#         """Дает полное описание заклинания."""
#         return f"{self.name}: {self.formula}"

#     def execute(self):
#         """Совершает заклинание."""
#         print(f"The spell {self.name} is being executed!")

#     def __str__(self):
#         """Переопределение метода str."""
#         return f"{self.get_description()}, allows the mage to perform magic."


# # Создаем три заклинания, переопределяя родительские методы
# spell1 = Spell("Открытие замков", "Alohomora")
# spell2 = Spell("Огненный шар", "Incendio")
# spell3 = Spell("Очищение", "Reparo")

# # Вызываем все методы для каждого заклинания
# print(spell1.get_description())
# spell1.execute()
# print(spell1)

# print(spell2.get_description())
# spell2.execute()
# print(spell2)

# print(spell3.get_description())
# spell3.execute()
# print(spell3)

"""

9. Напишите класс CustomError который наследуется от встроенного класса исключений Exception. Переопределите init таким образом

чтобы через экземпляр класса можно было передавать сообщение и создавать новые виды исключений.

Создайте исключение от этого класса с сообщением:

"ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ"

 

Напишите функцию проверяющую строки на регистр и если строка не написана в верхнем регистре выбросите исключение созданное классом CustomError:

 

Traceback (most recent call last):

  File "inheritance.py", line 121, in <module>

    check_letters(a)

  File "inheritance.py", line 117, in check_letters

    raise capitals_error

main.CustomError: ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ

 

"""

# class CustomError(Exception):
#     def __init__(self, message):
#         super().__init__(message)


# def check_letters(string):
#     """Проверяет строку на регистр и выбрасывает исключение, если строка не в верхнем регистре."""
#     if not string.isupper():
#         raise CustomError("ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ")


# # Пример использования:
# a = "Hello"
# try:
#     check_letters(a)
# except CustomError as capitals_error:
#     print(capitals_error)


"""

10. Создайте класс Character с помощью которого можно создавать героев для игры. Экземпляры класса должны иметь аттрибут name. У класса должна быть переменная power_list, в которой хранится словарь:

power_list = { 'мудрость': 0, 'харизма': 0, 'интеллект': 0, 'сила': 0, 'ловкость': 0 }

 

Класс должен иметь методы:

give_weapon - выбирает случайное оружие из списка

 

give_role - выбирает случайную роль из списка, к примеру:

["Варвар","Бард", "Клерик", "Боец", "Лесничий", "Паладин", "Чернокнижник"]

 

give_powers, передавая силу и значение можно менять power_list для определенного героя, к примеру:

char1.give_powers('ловкость', 5)

увеличит ловкость вашего героя.

 

Создайте три разных дочерьних класса от класса Character - Elf, Orc, DragonBorn,

дайте каждому из классов уникальный метод и добавьте уникальные аттрибуты экземпляра класса,наследуя init от Character. Создайте несколько героев от этих классов и вызовите их методы и методы родительского класса Character.

# """
# import random

# class Character:


#     def __init__(self, name):
#         self.power_list = {'мудрость': 0, 'харизма': 0, 'интеллект': 0, 'сила': 0, 'ловкость': 0}
#         self.name = name

#     def give_weapon(self):
#         weapons = ['меч', 'лук', 'палица', 'клинок', 'копье']
#         return random.choice(weapons)

#     def give_role(self):
#         roles = ["Варвар", "Бард", "Клерик", "Боец", "Лесничий", "Паладин", "Чернокнижник"]
#         return random.choice(roles)

#     def give_powers(self, power, value):
#         if power in self.power_list:
#             self.power_list[power] = value


# class Elf(Character):
#     def __init__(self, name):
#         super().__init__(name)
#         self.race = 'Эльф'
    
#     def special_ability(self):
#         return "Скрытность в лесах"


# class Orc(Character):
#     def __init__(self, name):
#         super().__init__(name)
#         self.race = 'Орк'
    
#     def special_ability(self):
#         return "Берсерк"


# class DragonBorn(Character):
#     def __init__(self, name):
#         super().__init__(name)
#         self.race = 'Драконорожденный'
    
#     def special_ability(self):
#         return "Дыхание дракона"


# # Пример использования:
# elf1 = Elf("Леголас")
# print(elf1.name)
# print(elf1.give_weapon())
# print(elf1.give_role())
# elf1.give_powers('ловкость', 8)
# elf1.give_powers('харизма', 8)
# elf1.give_powers('мудрость', 8)
# elf1.give_powers('интеллект', 8)
# elf1.give_powers('сила', 8)
# print(elf1.power_list)
# print(elf1.special_ability())

# orc1 = Orc("Громм")
# print(orc1.name)
# print(orc1.give_weapon())
# print(orc1.give_role())
# orc1.give_powers('сила', 10)
# orc1.give_powers('ловкость', 10)
# orc1.give_powers('мудрость', 10)
# orc1.give_powers('харизма', 10)
# orc1.give_powers('интеллект', 10)
# print(orc1.power_list)
# print(orc1.special_ability())

# dragonborn1 = DragonBorn("Смауг")
# print(dragonborn1.name)
# print(dragonborn1.give_weapon())
# print(dragonborn1.give_role())
# dragonborn1.give_powers('интеллект', 7)
# dragonborn1.give_powers('мудрость', 7)
# dragonborn1.give_powers('ловкость', 7)
# dragonborn1.give_powers('харизма', 7)
# dragonborn1.give_powers('сила', 7)
# print(dragonborn1.power_list)
# print(dragonborn1.special_ability())

 
