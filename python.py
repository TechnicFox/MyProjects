# def plus(a,b):
#     return a+b
# print(plus(a=1,b=9999))

# def plus(a,b,c,d):
#     return a*b*c*d
# print(plus(2,8,d=8,c=95))

# def plus(a,b,*args):
#     a = 0
#     for i in args:
#         a+=i
#     return a
# print(plus(1))

# def plus(**kwargs):
#     return kwargs
# print(plus(hello='world'))

# a = lambda x,y:x+y
# print(a(10,78874654))

# print((lambda x,y:x+y)(10,78874654))

# def biggest(*args):
#     biggest_num = 0 
#     for i in args:
#         if i > biggest_num:
#             biggest_num=i
#     return biggest_num
# print(biggest(87,8,78,789,8,4,94,5,84,84,89,89,4,98,5))

# def add(numbers=3):
#     if numbers==[]:
#         return 0
#     result = 0
#     for i in numbers:
#         result+=i
#     return result

# print(add([4,9,4,894,84,8,48,48,94,984,8,4,894,894,89,489,489,4,84,84,8,4,498,4,894,89,489,48,48948948,94,89898944444984894984]))

# def get_even(*args):
#     evens = []
#     for i in args:
#         if i % 2 != 1:
#             evens.append(i)
#     return evens
# print(get_even(0,46,78,464,8,48,64,64,79))

# def pack(*args):
#     new = []
#     for i in args:
#         new.append(i)
#     lst = new[:4]
#     x = int(new[4:5][0])
#     y = int(new[5:6][0])
#     z = int(new[6:7][0])
#     return lst,x,y,z
# print(pack(1,2,3,4,5,6,7))


# def sqr(*args):
#     sqeured=[]
#     for i in args:
#         sqeured.append(i*i)
#     return sqeured

# print(sqr(1,2,3,4,5,6,7,8,9))

# get_sq = lambda x:x*x
# print(get_sq(48789))

model = lambda x:x if x>0 else -x
print(model(-4646446))