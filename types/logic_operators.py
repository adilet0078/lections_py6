# Операторы сравнения
# Услоовные операторы
# Логические операторы


# операторы сравнения
#  <, >, ==(равно), != (не равно), <=, >=
# 1 > 7 --> False
# 7 < 9 --> True

# print('ABC1234124' > 'abc123') # Он сравнивает по ASCll

# 1 2 4 8 16 32 64 128 256 512 1024 2048
# 0  0  1 1  0   1 # справа на лево
# 44 --> 101100
# 15 --> 1111
# 20 --> 10100

# a = 'A'
# b = 'b'
# print(ord(a), ord(b)) # функция
# num = 65
# print(chr(num)) # обратная функция

# Условные оператторы
# if
# elif
# else

# if <condition>:
#     <body if> # сработает, если в conditon if придет True
# [elif] <confition>: # а если:
#     <body elif>
# [else]:
#     <body else> # сработает, если во всех стоящих условиях пришло False

# string = input('Enter smth: ').lower()

# if string == 'hello':
#     print('Hello, It\'s me, I was wonderung if after all these you\'d like like to meet!')
# elif string == 'John Snow':
#     print('Welcome back, John Snow! The king of North!')
# elif string == 'abra-kadabra':
#     print('Sim salamon kadabra!')
# else:
#     print('No match found.')


# print('Registration Form')
# email =  input('Enter email: ')
# if '@' not in email:
#     raise ValueError('Invalid email address')
# password = input('Enter password: ')
# password1 = input('enter password confirmation: ')
# if len(password) < 8:
#     raise ValueError('Password must be at least 8 characters long')
# elif password.isdigit():
#     raise ValueError('Password must contain at least one letter')
# elif password.isalpha():
#     raise ValueError('invalid password , only alphabets are allowed')
# elif password != password1:
#     raise ValueError('Passwords do not match')
# index = email.find('@')
# print(f'Successfully registrated! Hellomr/mrs {email[:index]}!')


# age = int(input('enter your age: '))
# if age.isdigit():
#     age = int(age)
# else:
#     raise Exception('Age must be an integer')
# if age < 18:
#     print(f'You are too young. You need {18 - age} more years')
# else:
#     print('Welcome!')


# лщгические операторы
# and - Логические и 
# or - Логические или
# not - Логические отрицание

# money = 1_000_000
# status = 'base'

# if money > 100_000 and status == 'vip':
#     print('You are president of the company')
# elif money > 1_000_000 and status == 'vip':
#      print('You are the minister of the company')
# else :
#     print('You are honorable member of the company')
