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

# def wear(size, trademark):
#     print("This size "+ size +" I love python "+'and '+trademark.title())
#
# wear('l', 'adidas')
# wear('M', 'nike')
# wear(size = "Like", trademark = 'adidas')
#
#
# def animal(name, type='dog'):
#     print("This is "+name.title()+" is a "+type+" !")
#
# animal(name='charly')
# animal('pussy', type='cat')
#
#
# def describe_city(city, country='russia'):
#     print(country.title()+" city is "+city.title())
#
# describe_city("Russia", 'moscow')
# describe_city('kazan')
# describe_city('ufa')
#
# def full_name(first_name, last_name, middle_name=''):
#     formated_name = first_name.capitalize()+' '+last_name.capitalize()+' '+middle_name.title()
#     return formated_name
# print(full_name("edison", 'kovanio'))
#
# def build_person(first_name, last_name, age=''):
#     person = {'first':first_name.title(), 'last':last_name.title()}
#     if age:
#         person['age'] = age
#     return person
#
# musculian = build_person('vadim','antonov')
# print(musculian)
# musculian = build_person('misha', 'lotov', '25')
# print(musculian)

# def build_person(f_name, l_name, age=''):
#     full_name = f_name+" "+l_name
#     return full_name.title()
#
# while True:
#     print("Please tell me your name")
#     f_name = input("First name: ")
#     if f_name == "q":
#         break
#     l_name = input("Enter your last name: ")
#     if l_name == 'q':
#         break
#     formatted_name = build_person(f_name, l_name)
#     print("Hello, " + formatted_name + "!")
#
#
# def get_city(country, city, age=''):
#     if age:
#         city_builder = city+", "+country+', '+age
#     else:
#         city_builder = city+', ' + country+ ' !'
#     return city_builder.title()
#
# love_city = get_city('Russia', 'Moscow', '855')
# print(love_city)
#
# love_city = get_city('USA', 'Washington')
# print(love_city)
#
#
# def get_formatted_name(first_name, album, track=''):
#     full_name = {'name':first_name.capitalize(), 'album': album.capitalize()}
#     if track:
#         full_name['track'] = track.capitalize()
#     return full_name
#
# music = get_formatted_name('john bon jovi', 'my live', 'one')
# print(music)
# music = get_formatted_name('michael', 'jackson')
# print(music)
#
# while True:
#     print('\n Enter artist ')
#     first_name = input("Name ")
#     if first_name == "q":
#         break
#     album = input('Album ')
#     if album == 'q':
#         break
#     artist = get_formatted_name(first_name, album)
#     print(artist)
#
# def greet_users(names):
#     for name in names:
#         print("Hello "+name.title()+" !")
#
# users = ['jilia','osborn', 'victor']
# greet_users(users)
#
# names = ['Garry', 'Larry', 'Tom']
# new_names = []
#
# def print_models(unprinted_design, completed_models):
#     while unprinted_design:
#         current_design = unprinted_design.pop()
#         print('Printing model: '+ current_design)
#         completed_models.append(current_design)
#
# def show_completed_models(completed_models):
#     print('\n The following model have been printed:')
#     for model in completed_models:
#         print(model)
# print_models(names, new_names)
# show_completed_models(new_names)

names = ['Garry', 'Larry', 'Tom']
new_magic = []

def show_magician(username):
    for name in username:
        print(name)
show_magician(names)


def make_great(magician):
    for name in magician[:]:
        name = "great "+name
        new_magic.append(name)

a = make_great(names)
show_magician(new_magic)
print(names)
print(new_magic)