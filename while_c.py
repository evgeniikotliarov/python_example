# name = input('Please enter your name: ')
# print("Hello " + name.title() + '!')
#
# promt = "If you tell us who you are, we can personalize the message you see"
# promt += "\nWhat's is your first name? "
# name = input(promt)
# print(name)
# print("Hello " + name.title() + " !")
# # name = int(name)
# # f = name >= 10
# # print(f)
#
# height = input("Enter your height ")
# height = int(height)
# if height <= 150:
#     print('No')
# else:
#     print("Yes")
# num = input("Enter your number ")
# num = int(num)
#
# if num % 2 == 0:
#     print("\n Your number good " + str(num) + " !")
# else:
#     print("\n No false " + str(num) + "not good")
#
# request = input("Сколько человек будет за столом?")
# request = int(request)
# if request >= 8:
#     print("За один стол " + str(request)+ " человек не поместяться")
# else:
#     print("Good " + str(request)+ " человек сядите")
#
# example = "\nTell me world"
# example += "\n enter 'quit' to end the program"
#
# active = True
# while active:
#     message = input(example)
#     if message == 'quit':
#          active = False
#     else:
#         print(message)
#
# example = "\n Введите город в котором вы бывали"
# example += "\n Введите 'q' если нужно выйти "
#
# while True:
#     city = input(example)
#     if city == 'q':
#         break
#     else:
#         print("Я тоже бывал в " + city.title() + " классно там")
# current_number = 0
# while current_number < 10:
#     current_number+=1
#     if current_number % 2 == 0:
#         continue
#     print(current_number)

# age = 'Enter your age '
# age = input(age)
# age = int(age)
# age1 = range(0,99999)
# if age in age1:
#     print('True')
# else:
#     print('False')



# if age == int(age):
#     if age < 3:
#         print('Your age ' + str(age) + 'price 3 dollars')
#     elif age <= 12:
#         print('Your age ' + str(age) + 'price 10 dollars')
#     elif age > 12:
#         print('Your age ' + str(age) + 'price 15 dollars')
#
# elif age == str(age):
#     print("Thank you")


# x = 1
# while x<1000000:
#     x+=1
#     print(x)

def wear(size, trademark):
    print("This size "+ size +" I love python "+'and '+trademark.title())

wear('l', 'adidas')
wear('M', 'nike')
wear(size = "Like", trademark = 'adidas')


def animal(name, type='dog'):
    print("This is "+name.title()+" is a "+type+" !")

animal(name='charly')
animal('pussy', type='cat')


def describe_city(city, country='russia'):
    print(country.title()+" city is "+city.title())

describe_city("Russia", 'moscow')
describe_city('kazan')
describe_city('ufa')
