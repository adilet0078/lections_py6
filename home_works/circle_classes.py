# 1) Создайте класс Circle, с переменными класса задающие по умолчанию цвет круга - синий, и число Пи(3.14). Экземпляры класса Circle в свою очередь должны иметь обязательный аттрибут - радиус. Также класс должен иметь метод расчета площади круга. Создайте экземпляр класса, переопределите цвет экземпляра и расчитайте площадь фигуры.

# class Circle:
#     default_color = "blue"
#     pi = 3.14

#     def __init__(self, radius, color=None):
#         self.radius = radius
#         self.color = color if color else self.default_color

#     def calculate_area(self):
#         return self.pi * (self.radius ** 2)

# # Create an instance of the Circle class
# circle1 = Circle(radius=5, color="red")

# # Calculate the area of the circle
# area = circle1.calculate_area()

# # Print the area
# print("The area of the circle is:", area)



# 2) Создайте класс для песен Song. Каждая песня имеет название, автора и год выпуска. Добавьте три метода show_author, show_title, show_year, выводящие утверждения о каждом атрибуте экземпляра класса Song, например: "Эта песня вышла в 2010 году". Создайте экземпляр класса с вашей любимой песней и примените все методы.


# class Song:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year

#     def show_author(self):
#         print(f"The author of the song is {self.author}")

#     def show_title(self):
#         print(f"The title of the song is '{self.title}'")

#     def show_year(self):
#         print(f"This song was released in {self.year}")

# # Create an instance of the Song class with favorite song details
# favorite_song = Song("Bohemian Rhapsody", "Queen", 1975)

# # Apply the methods to show the details of the favorite song
# favorite_song.show_author()
# favorite_song.show_title()
# favorite_song.show_year()


# 3) Создайте класс Taxi, объекты которого имеют такие атрибуты как название компании, стоимость посадки, стоимость за каждый пройденный километр. Также добавьте к классу метод расчитывающий стоимость поездки. Создайте три экземпляра класса Taxi для трех разных компаний Namba, Yandex и Jorgo и расчитайте стоимость поездки на каждом из них.
"""
# class Taxi:
#     def __init__(self, company_name, pickup_cost, cost_per_km):
#         self.company_name = company_name
#         self.pickup_cost = pickup_cost
#         self.cost_per_km = cost_per_km

#     def calculate_trip_cost(self, km):
#         return self.pickup_cost + self.cost_per_km * km

# # Create instances of the Taxi class for different companies
# namba_taxi = Taxi("Namba", 200, 150)
# yandex_taxi = Taxi("Yandex", 150, 120)
# jorgo_taxi = Taxi("Jorgo", 180, 130)

# # Calculate the trip cost for each taxi company for a 10 km trip
# trip_distance_km = 10
# cost_namba = namba_taxi.calculate_trip_cost(trip_distance_km)
# cost_yandex = yandex_taxi.calculate_trip_cost(trip_distance_km)
# cost_jorgo = jorgo_taxi.calculate_trip_cost(trip_distance_km)

# # Print the trip cost for each taxi company
# print(f"Trip cost for Namba taxi: {cost_namba} KZT")
# print(f"Trip cost for Yandex taxi: {cost_yandex} KZT")
# print(f"Trip cost for Jorgo taxi: {cost_jorgo} KZT")
# """

# 4) Создайте класс телефонной книги. У контактов должны быть имена и фамилии и номер телефона. Также создайте метод get_info, который выводит информацию о контакте в следующем виде: "Контакт: Иван Петров, телефон: +996555777888".
# Затем объявите экземляр класса и вызовите метод.
"""
class PhoneBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, first_name, last_name, phone_number):
        self.contacts.append({
            "first_name": first_name,
            "last_name": last_name,
            "phone_number": phone_number
        })

    def get_info(self, index):
        contact = self.contacts[index]
        full_name = f"{contact['first_name']} {contact['last_name']}"
        phone_number = contact['phone_number']
        print(f"Contact: {full_name}, phone: {phone_number}")

# Create an instance of the PhoneBook class
phone_book = PhoneBook()

# Add contacts to the phone book
phone_book.add_contact("Ivan", "Petrov", "+996555777888")
phone_book.add_contact("Maria", "Ivanova", "+996777888999")

# Get information about a contact
phone_book.get_info(0)
"""
# 5) Напишите класс Salary для расчета налогов на заработную плату. У класса должна быть обязательная переменная класса - процент налога от зарплаты - 8%. Объекты класса должны иметь сумму зарплаты и стаж работы в качестве атрибутов. Также у класса должен быть метод расчитывающий сумму налога заплаченного за весь стаж работы. Создайте экземпляр класса и посчитайте сумму вашего налога.

# class Salary:
#     tax_percentage = 8  # Class variable for tax percentage

#     def __init__(self, salary_amount, years_worked):
#         self.salary_amount = salary_amount
#         self.years_worked = years_worked

#     def calculate_tax(self):
#         total_tax = (self.salary_amount * self.tax_percentage / 100) * self.years_worked
#         return total_tax

# # Create an instance of the Salary class
# my_salary = Salary(50000, 5)  # Assuming a salary of 50000 and 5 years of work

# # Calculate the total tax paid for the entire work duration
# total_tax_paid = my_salary.calculate_tax()
# print(f"The total tax paid for {my_salary.years_worked} years of work is: {total_tax_paid} USD")