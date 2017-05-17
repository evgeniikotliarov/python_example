# from car.get_car import make_car
#
# view_car = make_car('Toyota', 'Rav4', year='2017', color='silver')
# print(view_car)

# from car.get_car import arifmetic
#
# a = int(input("Enter first number "))
# b = int(input("Enter second number "))
# c = int(input("Enter third number "))
#
# arifmetic(a,b,c)
from car.get_car import arifmetic, full_name
name = input("Enter your name ")
surname = input("Enter your surname ")
year = int(input("When were your born "))
country = input("Where are you from ")

age = arifmetic(year)
f_name = full_name(name, surname)

print("Hello, "+f_name+". ""Your are "+str(age+" years old ." "You are living from "+country+" !")