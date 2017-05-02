# cars = ['audi', 'Bmw', 'vw', 'Honda', 'seat', 'db', 'Toyota', 'subaru', 'lexus', 'ford', 'lada' ]
# used_cars = []
# other_cars = []
# another_cars = []
# for value in cars:
#     if len(value) <= 4:
#         used_cars.append(value.title())
#     elif len(value) >= 6:
#         other_cars.append(value.title())
#     elif value.lower:
#         another_cars.append(value)
#     elif value in 'db':
#         used_cars.append(value.title())
#     elif value == 'toyota':
#         used_cars.append(value.title())
#     elif value == 'lada':
#         used_cars.append(value.title())
# print(used_cars)
# print(other_cars)
# print(another_cars)

# users = ['Dima', 'Admin', 'borya', 'zara', 'misha', 'oleg', 'Zina']
# for user in users:
#     if user == "Admin":
#         print("Hello " + user + " I see you")
#     else:
#         print(user.title() + " we glad to sse")
#
# pizza = ['d']
# if pizza:
#     for p in pizza:
#         print('Adding ' + p + " element")
# else:
#     print("\n Finish")
#

# users = ['Dima', 'Admin', 'borya', 'zara', 'misha', 'oleg', 'Zina']
# current_users = ['vasya', 'masha', 'Zara', 'sima', 'Oleg']
# current_users_low = []
# for c_user in current_users:
#     current_users_low.append(c_user.lower())
# p = 'User exsist'
# d = 'Such a name exsist'
# for user in users:
#     if user.lower() in current_users_low:
#         print(p)
#         break
#     else:
#         print(d)

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
numbers_parser = []
for num in numbers:
    if num == '1':
        num = '1st'
        numbers_parser.append(num)
    elif num == '2':
        num = '2nd'
        numbers_parser.append(num)
    elif num == '3':
        num = '3th'
        numbers_parser.append(num)
    else:
        numbers_parser.append(num)
print(numbers_parser)



