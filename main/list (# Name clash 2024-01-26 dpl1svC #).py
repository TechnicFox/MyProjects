# all_list = ['str', 123, {'a':123}, True, 1.22548948494, ('aaaa')]
# numbers = [1,2,3,4,5,6,7,8,9,10]
# for i in numbers:
#     if i % 2 == 0:
#         print(i)
#     else:
#         numbers.remove(i)
# print(numbers)
# num_list = []
# while True:
#     num=int(input('Enter number:'))
#     if num == 0:
#         print(num_list)
#         break
#     else:
#         num_list.append(num)

# num_list = [5,6,7,8,9,4,3,1,2]
# for i in range(1,11):
#     num = int(input('Enter number:'))
#     num_list.append(num)
# print(num_list)

# num_list.append(['123','123'])
# num_list.remove(2)
# num_list[3]= 'hello'
# num_list.pop(7)
# num_list.extend({'hello':123})
# num_list.insert(7, 'world')
# print(num_list.index(7))
# print(num_list.count('hello'))
# num_list.reverse()
# num_list.sort(reverse=True)
# print(num_list),


# kortez = (1,8,7,9,4,3,5,6,0,1,1,1,8,7,9,4,3,5,6,0,1,1,1,8,7,9,4,3,5,6,0,1,1,1,8,7,9,4,3,5,6,0,1,1)
# list = [1,8,7,9,4,3,5,6,0,1,1,1,8,7,9,4,3,5,6,0,1,1,1,8,7,9,4,3,5,6,0,1,1,1,8,7,9,4,3,5,6,0,1,1]

# print(kortez.count(1))
# print(kortez.index(5))
# # kortez.append()
# print(kortez)
# print(kortez.__sizeof__())
# print(list.__sizeof__())

# Дано рядок.
# Спочатку виведіть третій символ цього рядка.
# У другому рядку виведіть передостанній символ цього рядка.
# У третьому рядку виведіть перші п'ять символів цього рядка.
# У четвертому рядку виведіть весь рядок, крім останніх двох символів.
# У п'ятому рядку виведіть усі символи з парними індексами (вважаючи, що індексація
# починається з 0, тому символи виводяться починаючи з першого).
# У шостому рядку виведіть усі символи з непарними індексами, тобто починаючи з
# другого символу рядка.
# У сьомому рядку виведіть усі символи у зворотному порядку.
# У восьмому рядку виведіть усі символи рядка через один у зворотному порядку,
# починаючи з останнього.
# У дев'ятому рядку виведіть довжину даного рядка.

# list = [1,2,3,4,5,6,7,8,9,10]
# print(list[2])
# print(list[-2])
# print(list[0:5])
# print(list[0:-2])
# print(list[::2])
# print(list[1::2])
# print(list[::-1])
# print(list[::-2])
# print(len(list))

# num_list=[]
# while True:
#     num = int(input('Enter num>>>'))
#     if num == 0:
#         break
#     num_list.append(num*num)
# print(num_list)




# Написати програму видалення зі списку всіх номерів із кодом "+1" - ['+191734734',
# '+1915125456', '+6915213456', '+4915213456', '+1915634456']

# numbers = ['+191734734', '+1915125456', '+6915213456', '+4915213456', '+1915634456']
# result = []
# for i in numbers:
#     if i[0:2]=='+1':
#         result.append(i)
# for a in result:
#     numbers.remove(a)
# print(numbers)


# numbers = [1,2,3,4,5,6,7,8]
# numbers.remove(6)
# for i in range(0,6):
#     numbers.insert(0,0)
# numbers.insert(len(numbers)//2,100)
# for i in range(0,18):
#     numbers.append(55)
# for i in range(0,18):
#     numbers.remove(55)
# print(numbers)

v = [1205, 1101, 1434, 1320, 923, 874]
print(v[:3])
print(v[-1:-5:-1])
num = [2,52,33,99,1]
for i in num:
    if i % 2 != 0 and (i > 27 and i > 93):
        print(i)

# dictanory = {}
# while True:
#     key = input('Enter Key')
#     if key == '0':
#         break
#     num = int(input('Enter num'))
#     dictanory[key]=num
# print(dictanory)

# # delete = input('Delete:')
# # dictanory.pop(delete)
# # print(dictanory)
# suma = 0
# for i in dictanory.values():
#     suma+=i
#     print(suma)

# Знайти середній бал студента з різних предметів.
# student_grades = {
#  'Математика': 90,
#  'Фізикка': 85,
#  'Хімія': 92,
#  'Англійська': 88
# }

# count = 0
# grade = 0
# for i in student_grades.values():
#     count += 1
#     grade += i
# print(grade/count)

# def biggest(list):
#     biger=0
#     for i in list:
#         if i > biger:
#             biger=i
#     return biger
 
# print(biggest([7,8,1,9,6,48,99,187,2,6]))

# def calc_area(widgth, length):
#     return widgth*length
# print(calc_area(5,78))

# def midle(*args):
#     count = 0
#     grade = 0
#     for i in args:
#         count += 1
#         grade += i
#     print(grade/count)
#     return None

# midle(1,9,7,3,6,100)

# def only(*args):
#     once = []
#     for i in args:
#         if i not in once:
#             once.append(i)
#     print(once)
#     return None        
# only(1,9,7,3,6,100,6,7,3)

# add = lambda x, y: x+y

# print(add(7,4984894))

# minus = lambda num: num%2==0
# print(minus(7))
    
# divide = lambda num1, num2: None if num2 == 0 else num1/num2
# print(divide(7, 7))

