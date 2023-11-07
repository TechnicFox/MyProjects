# a = int(input('Number a:'))
# b = int(input('Number b:'))
# if a > b:
#     print('a більше')
# elif a < b:
#     print('b більше')
# else:
#     print('a дорівнює b')


# for i in range(1, 11):
#     print(i)


# while True: 
#     number = int(input('>>>>'))
#     if number == 0:
#         break


# a,b = 5, 6
# a,b = b, a
# print(a,b, sep='@', end='>>>>>>>>>>>>>>>')
# print(5, 9)

# name = input('Як тебе звати?\n>>>')
# print('Привіт', name)
# age = int(input('Скільки тобі років?\n>>>'))
# if age<12:
#     print(name, 'ти ще дитина')
# elif age<18:
#     print(name, 'ти підліток')
# else:
#     print(name, 'ти дорослий')
# while True:
#     hobby = input('Чим ти любиш займатися?\n>>>')
#     if hobby != '':
#         print("О круто!")
#         break
# country = input('У якій країні ти живеш?\n>>>')
# if country.lower() == 'в україні': 
#     print('Я там теж живу!')
# else:
#     print('Це крута країна!')

# city = input('У якій місті ти живеш?\n>>>')
# if city.lower() == 'у києві': 
#     print('А я у Львові!')
# else:
#     print('Це круте місто!')

# weather = input('Яка сьогодні погода?\n>>>')
# if weather.lower() == 'сонячно': 
#     print('😁')
# elif weather.lower() == 'йде дощ': 
#     print('😓')
# else:
#     print('❓')
# sum = 0
# for i in range(1, 5):
#     sum += i
# print(sum)

# a = 3
# print(a >=3)

# a = int(input('Number A>>>'))
# b = int(input('Number B>>>'))
# c = int(input('Number C>>>'))
# result = 0
# for i in (a, b, c):
#     if i > 0:
#         result+=1
# print(result)

# a = int(input('Number A>>>'))
# b = int(input('Number B>>>'))
# c = int(input('Number C>>>'))

# if a < b and a < c:
#     print('A найменше')
# elif b < c:
#     print('B найменше')
# else:
#     print('C найменше')
    
# number = int(input('Number A>>>'))
# if number > 0:
#     print(1)
# elif number < 0:
#     print(-1)
# else:
#     print(0)

# number = int(input('Number>>>'))

# if number % 4 == 0 and not number % 100 == 0:
#     print('YES')
# else:
#     print('NO')

# product1 = round(float(input('What price of first product? >>> $')), 2)
# product2 = round(float(input('What price of second product? >>> $')), 2)
# money = round(float(input('How much money do you have?>>> $')), 2)

# if money >= product1 + product2:
#     print('You have enough dollars.')
# else:
#     print(f'You need ${round(product1 + product2 - money, 2)} more.')

# minute = int(input('Minutes>>>'))

# if minute%5 == 4 or minute%5 == 0:
#     print('🟥')
# else:
#     print('🟩')

# num_1 = int(input('Enter number 1:'))
# num_2 = int(input('Enter number 2:'))
# if num_1 % num_2 == 0:
#     print(round(num_1/num_2))
# else:
#     print('не діляться')


# num_1 = int(input('Enter number 1:'))
# num_2 = int(input('Enter number 2:'))
# if num_1 < num_2:
#     print('number 1 smaller')
# elif num_1 > num_2:
#     print('number 2 smaller')
# else:
#     print('Дорівнюють')
    

# num_1 = int(input('Enter number 1:'))
# num_2 = int(input('Enter number 2:'))
# num_3 = int(input('Enter number 3:'))

# if num_1 == num_2 and num_2 == num_3:
#     print(3)
# elif num_1 != num_2 and num_2 != num_3 and num_3 != num_1:
#     print(0)
# else:
#     print(2)

# x_1 = int(input('Enter x1:'))
# y_1 = int(input('Enter y1:'))
# x_2 = int(input('Enter x2:'))
# y_2 = int(input('Enter y2:'))
# if x_1 > 0 and x_1 < 9 and x_2 > 0 and x_2 < 9 and y_1 > 0 and y_1 < 9 and y_2 > 0 and y_2 < 9:
#     if x_1 == x_2 or y_1 == y_2:
#         print('yes')
#     else:
#         print('NOOOOOOOOO')
# else: 
#     print('ERROR 404')
# number = 0
# N = int(input('Enter N:'))
# while number <= N:
#     number += 1
#     print(number) 


# N = int(input('Enter N:'))
# number = 0
# while number <= N*N-1:
#     number += 1
#     print(number)


# result = 0
# while True:
#     a = int(input('>>>')) 
#     result += 1
#     if a == 0:
#         break   
    
# print('Result: '+ str(result))
# suma = 0
# while True:
#     num = int(input(">>>"))
#     if num == 0:
#         break
#     suma += num

# print("Сума: ", suma)
# times = 0
# suma = 0
# while True:
#     num = int(input(">>>"))
#     if num == 0:
#         break
#     print(str(num)[-1])
#     if str(num)[-1] == '0':
#         suma += num
#         times += 1

# print("Середнє: ", suma/times)


# small = 0
# num = int(input(">>>"))
# small = num
# while True:
#     if num == 0:
#         break
#     if num < small:
#         small = num
#     num = int(input(">>>"))

# print("Small: ", small)

# km = int(input(">>>"))
# day=1
# while True:
#     km *= 1.1
#     day+=1
#     if km >= 1000:
#         print(round(km, 2), 'M', day, 'DAYS')
#         break



# import random

# setting = input('Enter range(exp. 1-10):')
# random_num = random.randint(int(setting.split('-')[0]), int(setting.split('-')[1]))
# gueses = int(input('Enter lives:'))
# num = int(input('Guese:'))

# while True:

#     if  num == random_num:
#         print('Win')
#         break
#     elif num > random_num: num = int(input('Lower:'))
#     elif num < random_num: num = int(input('Higher:'))
#     gueses-=1
#     if  gueses == 0:
#         print('Looser')
#         break

# def calc(num1, sign, num2):
#     if sign == '+':
#         print('\n',num1,'\n',sign,'\n',num2,'\n', '=','\n',num1+num2)
#         return(num1+num2)
#     elif sign == '-':
#         print('\n',num1,'\n',sign,'\n',num2,'\n', '=','\n',num1-num2)
#         return(num1-num2)
#     elif sign == '*':
#         print('\n',num1,'\n',sign,'\n',num2,'\n', '=','\n',num1*num2)
#         return(num1*num2)
#     elif sign == '/':
#         print('\n',num1,'\n',sign,'\n',num2,'\n', '=','\n',num1/num2)
#         return(num1/num2)
#     elif sign == '//':
#         print('\n',num1,'\n',sign,'\n',num2,'\n', '=','\n',num1//num2)
#         return(num1//num2)
#     elif sign == '%':
#         print('\n',num1,'\n',sign,'\n',num2,'\n', '=','\n',num1%num2)
#         return(num1%num2)
#     elif sign == '^' or sign == '**':
#         print('\n',num1,'\n',sign,'\n',num2,'\n', '=','\n',num1**num2)
#         return(num1**num2)

# num1 =  int(input('Enter first number:'))
# sign1 =  input('Enter sign:')
# num2 =  int(input('Enter second number:'))
# sign2 =  input('Enter sign:')
# num3 =  int(input('Enter second number:'))
# calc(calc(num1, sign1, num2), sign2, num3)



# x_1 = int(input('Enter x1:'))
# y_1 = int(input('Enter y1:'))
# x_2 = int(input('Enter x2:'))
# y_2 = int(input('Enter y2:'))

# pos_x = abs(x_1-x_2)
# pos_y = abs(y_1-y_2)
# if pos_x == 2 and pos_y == 1 or pos_x == 1 and pos_y == 2:
#     print('yes')



