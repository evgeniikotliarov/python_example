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

users = ['Dima', 'Admin', 'borya', 'zara', 'misha', 'oleg', 'Zina']
for user in users:
    if user == "Admin":
        print("Hello " + user + " I see you")
    else:
        print(user.title() + " we glad to sse")

pizza = ['d']
if pizza:
    for p in pizza:
        print('Adding ' + p + " element")
else:
    print("\n Finish")