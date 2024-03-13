# области видимости и пранстранство имен (scopes)
# технология которая определяет контекст имени, в рамках которого мы можем ее использовать

# global
# local
# nonlocal

# a = 5 

# def func():
#     b = 10
#     print(a)
#     print(b)

# func()

# built-ins(встроенные область видимости) -   print, len, min, max
# global(глобальная область видимости) - a, b, c
# <enclosed> ( замкнутая(не локальная,nonlocal) 
# local(локальная область видимости) -> область внутри функции


# a = 10 # global
# print # built-in

# def hello():  # global
#     a = 'hello' # local
#     print(a, 'local, inside in func ' )

# hello()
# print(a, 'global, outside in func ' )
# LEGB - local, enclosing, global, built-in
#----------->>>>>>>>>>>>



#----------------------------------------------------

# enclosed 
# замкнутое пространство имен - локальное пространство, у которого есть внутреннее(вложенное) локальное прмостранство

# x = 'global'
# print(x, '1') # global

# def enclosed( ): # global  
#     x = 'enclosed'
#     print(x, '2') # enclosed
#     def local(): # enclosed
#         x = 'local'
#         print(x, '3') # local
#     local()
#     print(x, '4') # enclosed
# enclosed()
# print(x, '5') # global


# var = 0 

# def increment():  #LEGB
#     global var
#     var = var + 1
#     if var == 15 :
#         increment()
    
# increment()
# print(var)
#  global -> позволяет изменять значение глобальной переменной внутри локальной области 

# nonlocal -> позволяет изменять значение не локальной(замкнутой)переменной внутри локальной области


# def counter():
#     num = 0 
#     def increment():
#         nonlocal num
#         num = num + 1
#         return num
#     return increment

# c_steps = counter()
# c_jumps = counter()
# print(c_steps)
# for i in range(1, 10000): 
#     c_steps()


# print(c_steps(), 'steps')
# print(c_jumps(), 'jumps')
# print(c_jumps(), 'jumps')
# print(c_jumps(), 'jumps')




