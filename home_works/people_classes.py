
# 1. Создать класс Person с атрибутами fullname, age, is_married
# 2. Добавить в класс Person метод introduce_myself, который бы распечатывал всю
# информацию о человеке
# 3. Создать класс Student наследовать его от класса Person и дополнить его атрибутом
# marks, который был бы словарем, где ключ это название урока, а значение - оценка.
# 4. Добавить метод в класс Student, который бы подсчитывал среднюю оценку ученика по
# всем предметам
# 5. Создать класс Teacher и наследовать его от класса Person, дополнить атрибутом
# experience.
# 6. Добавить в класс Teacher атрибут уровня класса salary
# 7. Также добавить метод в класс Teacher, который бы считал зарплату по следующей
# формуле: к стандартной зарплате прибавляется бонус 5% за каждый год опыта свыше 3х
# лет.
# 8. Создать объект учителя и распечатать всю информацию о нем и высчитать зарплату
# 9. Написать функцию create_students, в которой создается 3 объекта ученика, эти ученики
# добавляются в список и список возвращается функцией как результат.
# 10. Вызвать функцию create_students и через цикл распечатать всю информацию о каждом
# ученике с его оценками по каждому предмету. Также рассчитать его среднюю оценку по
# всем предметам.


# class Person:
#     def __init__(self, fullname, age, is_married):
#         self.fullname = fullname
#         self.age = age
#         self.is_married = is_married

#     def introduce_myself(self):
#         print(f"Full Name: {self.fullname}, Age: {self.age}, Married: {self.is_married}")

# class Student(Person):
#     def __init__(self, fullname, age, is_married, marks):
#         super().__init__(fullname, age, is_married)
#         self.marks = marks

#     def calculate_average_mark(self):
#         total_marks = sum(self.marks.values())
#         average_mark = total_marks / len(self.marks)
#         return average_mark

# class Teacher(Person):
#     def __init__(self, fullname, age, is_married, experience, salary):
#         super().__init__(fullname, age, is_married)
#         self.experience = experience
#         self.salary = salary

#     def calculate_salary(self):
#         bonus_percentage = max(0, (self.experience - 3) * 0.05)
#         total_salary = self.salary * (1 + bonus_percentage)
#         return total_salary

# # Create objects and use the classes
# student1 = Student("Alice Smith", 15, False, {"Math": 85, "Science": 90, "History": 75})
# teacher1 = Teacher("John Doe", 35, True, 5, 50000)

# student1.introduce_myself()
# print(student1.calculate_average_mark())  # Output: 83.3333

# teacher_salary = teacher1.calculate_salary()
# print(f"Teacher Salary: ${teacher_salary}")  # Output: Teacher Salary: $52500.0

# def create_students():
#     students = [
#         Student("Bob Johnson", 16, False, {"Math": 90, "Science": 88, "History": 92}),
#         Student("Eve Williams", 17, False, {"Math": 78, "Science": 85, "History": 80}),
#         Student("Charlie Brown", 15, False, {"Math": 95, "Science": 89, "History": 88})
#     ]
#     return students

# student_list = create_students()
# for student in student_list:
#     student.introduce_myself()
#     print(f"Average Mark: {student.calculate_average_mark()}")