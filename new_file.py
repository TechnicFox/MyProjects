# class Cat:
#     def __init__(self,name,city):
#         self.name = name
#         self.lives = 0
#         self.city = city
#     def printname(self):
#         print(self.name)
#     def info(self):
#         print(f'Кота звать {self.name} у нього {self.lives} життів і він живе в {self.city}')
#     def grow(self):
#         self.lives+=1
#         print(f'LIVES:{self.lives}')
# kitkat = Cat('CAT','kiev')
# kitkat.lives=5
# kitkat.grow()

# import time

# class Car:
#     def __init__(self,max_speed,color,brand):
#         self.max_speed = max_speed
#         self.color = color
#         self.brand = brand
#         self.speed = 0
#         self.speedometre = 0
#     def wash():
#         print('машина чиста')
#     def change_color(self, color):
#         self.color = color
#         print(f'yours car is now {self.color}')   
#     def prindbrand(self):
#         print(f'твоя машина {self.brand}')    
#     def speed_up(self,some):
#         if self.speed+some <= self.max_speed:
#             self.speed  += some
#         else:
#             print('youre car cant go faster')
            
#         print(f'you`re speed == {self.speed}')


# class ElectricCar(Car):
#     def __init__(self,max_speed,color,brand,battery):
#         super().__init__(max_speed,color,brand)
#         self.battery = battery
#     def charge_batery(self,some):
#         if self.battery+some <= 100:
#             self.battery += some
#         else:
#             print('💥💥💥💥💥')
#         print(f'batery{self.battery}')




# class ElectricTruck(ElectricCar):
#     def __init__(self,max_speed,color,brand,battery,tonns):
#         super().__init__(max_speed,color,brand,battery)
#         self.tonns = tonns
#     def change_tonns(self,some):
#         self.tonns+=some
#         print(f'weight:{self.tonns}')

# car1 = ElectricTruck(1000,'red','мерседес',100,200) 
# car1.speed_up(1000)
# car1.change_tonns(10)
# car1.charge_batery(1000000)

        












# while True:
#     time.sleep(1)
#     car1.speedometre+=car1.speed/360
#     car1.speedometre=round(car1.speedometre,2)
#     car1.battery-=1
#     print(f'battery == {car1.battery}')
#     print(f'Speedometre == {car1.speedometre}km')
        

# from typing import Any


# class User:
#     def __init__(self,first_name,last_name,number,age,height):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.number = number
#         self.age = age
#         self.height = height
#     def describe_user(self):
#         print(f'Name: {self.first_name} {self.last_name}\nNumber: {self.number}\nAge: {self.age}\nHeight: {self.height}')
#     def greet_user(self):
#         print(f'heloooo, {self.first_name} {self.last_name}')
# class Admin(User):
#     def __init__(self,first_name,last_name,number,age,height,text,delete,ban):
#         super().__init__(first_name,last_name,number,age,height)
#         self.priviliges = {'Allow text':text,'Allow delete users':delete,'Ban users':ban}
#     def show_priviliges(self):
#         print(f'Allow text = {self.priviliges['Allow text']}\nAllow delete users = {self.priviliges['Allow delete users']}\nAllow ban = {self.priviliges['Ban users']}')


# andrii = Admin('Андрій','Хаян',123,11,"tall",True,True,True)
# andrii.describe_user()
# andrii.greet_user()
# andrii.show_priviliges()



# class Circle:
#     def __init__(self,radius):
#         self.__radius=radius
#     def area(self):
#         print(f"Area: {self.__radius*2*3.14**2}")
#     def long(self):
#         print(f"Long: {self.__radius*2*3.14}")


# circle = Circle(3)

# circle.area()
# circle.long()


# class Student:
#     def __init__(self,salary):
#         self.__salary = salary
#     def display_salary(self):
#         print(f'Salary: {self.__salary}$$$$$$$$$$$$$$$$$$$')


# student = Student(123445687)
# student.display_salary()

# class BankAccount:
#     def __init__(self,balance,ID):
#         self.__ID = ID
#         self.__balance = balance
#     def __balance_amount(self):
#         print(self.__balance,self.__ID)
#     def __deposit(self,amount):
#         self.__balance+=amount
#     def __withdraw(self,amount):
#         self.__balance+=amount
#     def all(self):
#         self.__balance_amount()
#         self.__deposit(54564564)
#         self.__withdraw(454562002
#                         )

# banker0001 = BankAccount(0,1)
# banker0001.all()

# class Rectangle:
#     def __init__(self,height,weidth):
#         self.height = height
#         self.weidth = weidth
#     def area(self):
#         print(self.height*self.weidth)

# square = Rectangle(2,2)
# square.area()

# class Shape:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color

# class Circle(Shape):
#     def __init__(self, name, color):
#         super().__init__(name, color)

#     def draw(self):
#         print(f"Color is {self.color}")

# class Rectangle(Shape):
#     def __init__(self, name, color):
#         super().__init__(name, color)

#     def draw(self):
#         print(f"Color is {self.color}")

# class Triangle(Shape):
#     def __init__(self, name, color):
#         super().__init__(name, color)

#     def draw(self):
#         print(f"Color is {self.color}")

# circle = Circle("Circle", "red")
# circle.draw()

# rectangle = Rectangle("Rectangle", "blue")
# rectangle.draw()

# triangle = Triangle("Triangle", "green")
# triangle.draw()

# class Vechile:
#     def __init__(self,mark,model):
#         self.mark = mark
#         self.model = model
# class Car(Vechile):
#     def __init__(self,mark,model):
#         super().__init__(mark,model)
#         self.drive_boleen = False
#     def drive(self):
#         if self.drive_boleen:
#             print("car driving")
#             self.drive_boleen = False
#         else:
#             print('car stoped')
#             self.drive_boleen = True
#     def display_info(self):
#         print(f'MODEL: {self.model}')
#         print(f'MODEL: {self.mark}')
#         if self.drive_boleen:
#             print("car driving")
#         else:
#             print('car stoped')
            
# class Motorcycle(Vechile):
#     def __init__(self,mark,model):
#         super().__init__(mark,model)
#         self.drive_boleen = False
#     def drive(self):
#         if self.drive_boleen:
#             print("car driving")
#             self.drive_boleen = False
#         else:
#             print('car stoped')
#             self.drive_boleen = True
#     def display_info(self):
#         print(f'MODEL: {self.model}')
#         print(f'MODEL: {self.mark}')
#         if self.drive_boleen:
#             print("car driving")
#         else:
#             print('car stoped')
            

# class Bicycle(Vechile):
#     def __init__(self,mark,model):
#         super().__init__(mark,model)
#         self.drive_boleen = False
#     def drive(self):
#         if self.drive_boleen:
#             print("car driving")
#             self.drive_boleen = False
#         else:
#             print('car stoped')
#             self.drive_boleen = True
#     def display_info(self):
#         print(f'MODEL: {self.model}')
#         print(f'MODEL: {self.mark}')
#         if self.drive_boleen:
#             print("car driving")
#         else:
#             print('car stoped')
            

# car = Car("BMW",'SUPER')
# car.display_info()
# car.drive()
# car.display_info()
# motorcycle = Motorcycle("BMW",'SUPER')
# motorcycle.display_info()
# motorcycle.drive()
# motorcycle.display_info()
# bicycle = Bicycle("BMW",'SUPER')
# bicycle.display_info()
# bicycle.drive()
# bicycle.display_info()


# class Device:
#     def __init__(self,name,conected):
#         self.name = name
#         self.conected = conected
#     def conect(self):
#         self.conected=True
#         print('Device connected')
#     def disconect(self):
#         self.conected=False
#         print('Device disconnected')

# class Phone(Device):
#     def __init__(self,name,conected):
#         super().__init__(name,conected)
#     def display_info(self):
#         print(f'Name: {self.name}')
#         print(f'Conected: {self.conected}')
#     def conect(self):
#         self.conected=True
#         print('Phone connected')
#     def disconect(self):
#         self.conected=False
#         print('Phone disconnected')

# class Tablet(Device):
#     def __init__(self,name,conected):
#         super().__init__(name,conected)
#     def display_info(self):
#         print(f'Name: {self.name}')
#         print(f'Conected: {self.conected}')
#     def conect(self):
#         self.conected=True
#         print('Tablet connected')
#     def disconect(self):
#         self.conected=False
#         print('Tablet disconnected')
            
# class Laptop(Device):
#     def __init__(self,name,conected):
#         super().__init__(name,conected)
#     def display_info(self):
#         print(f'Name: {self.name}')
#         print(f'Conected: {self.conected}')
#     def conect(self):
#         self.conected=True
#         print('Laptop connected')
#     def disconect(self):
#         self.conected=False
#         print('Laptop disconnected')

# phone = Phone('iPhone', False)
# phone.conect()
# phone.disconect()
# phone.display_info()

# tablet = Tablet('iPad', False)
# tablet.conect()
# tablet.disconect()
# tablet.display_info()

# laptop = Laptop('iMac', False)
# laptop.conect()
# laptop.disconect()
# laptop.display_info()

class Shoping_kart:
    def __init__(self):
        self.items__ = []
    def add(self,item):
        self.items__.append(item)
    def remove(self,item):
        self.items__.remove(item)
    def list_items(self):
        print('Items in your Kart:')
        for i in self.items__:
            print('• '+i)

kart = Shoping_kart()
kart.add('banana')
kart.add('tomato')
kart.remove('tomato')
kart.list_items()

