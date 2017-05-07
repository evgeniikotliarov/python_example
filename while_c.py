name = input('Please enter your name: ')
print("Hello " + name.title() + '!')

promt = "If you tell us who you are, we can personalize the message you see"
promt += "\nWhat's is your first name? "
name = input(promt)
print(name)
print("Hello " + name.title() + " !")
# name = int(name)
# f = name >= 10
# print(f)

height = input("Enter your height ")
height = int(height)
if height <= 150:
    print('No')
else:
    print("Yes")
