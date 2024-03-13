# sentence = input('vvedite predlojenie')
# res = 'yes, voprositelnoe \' noye' if sentence[-1] == '?' else 'normal one'
# print(res)

 
# if sentence[-1] == '?' :
#     print('yes viprositelnoe')
# else:
#     print('normal one') 



# ternary operators(тернарные операторы) - это констуркция которая по своему действию аналогична конструкции if/else ,но при этом записывается в одну строчку 

# num = int(input('vvedite chislo'))
# print('even num 'if num %2 == 0 else 'ood num') 

# ls = [55, 65, 75, 89, 100, 15, 6,]
# choice = input('vvedite max/min').lower().strip()
# res = max(ls) if choice == 'max' else min(ls) if choice == 'min' else 'invavalid operator'
# print(res)


#  ---------------------



# from ast import Break
# import operator


# flag = True
# symbols ='0123456789' + '-' +  '.' 
# while flag: 
#     num1 = input('vvedite pervoe chislo:')
#     is_correct_num = True
#     for x in num1 :
#         if x not in symbols:
#             print('ne correctnoe chislo ')
#             is_correct_num = False
#             break
#     if not is_correct_num:
#         continue


#     num2 = input('vvedite vtoroe chislo:')
#     is_correct_num = True
#     for x in num2 :
#         if x not in symbols:
#             print('ne correctnoe chislo ')
#             is_correct_num = False
#             break
#     if not is_correct_num:
#         continue
            
#     num1 =  float(num1) if '.' in num1 else int(num1)
#     num2 =  float(num2) if '.' in num2 else int(num1)

#     # print(num1, type(num1))
#     # print(num2, type(num2))
#     operator = input('vvedite operaciu(+, -, *, /): ').strip()
#     if operator == '+':
#         print(f'результат: { num1 + num2}')
#     elif operator == '-':
#         print(f'результат: { num1 -num2}')
#     elif operator == '*':
#         print(f'результат: { num1 * num2}')    
#     elif operator == '/' :
#         print(f'результат: { num1 / num2}' if num2 != 0  else 'на ноль делить нельзя !')
#     else:
#         print('vy vveli nevernyi operator')
      
    
#     choice = input('hotite prodoljit (yes/no)?:')
#     if choice.lower().strip() != 'yes':
#         flag = False
#         print('BYE')

