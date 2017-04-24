# pizza = ['pipperoni', 'chilli', 'mozarella']
# print(pizza)
# for piz in pizza:
#     print(piz + " I like it")
#
# for pis in pizza:
#     print("Do you like " + pis.title() + ".\n")
# print("Bla bla bla")
#
# for value in range(1,21):
#     print(value)
#
# for value in range(1,9):
#     print(value)
#
# numbers = list(range(1,6))
# print(numbers)
#
# even_number = list(range(0,21,5))
# print(even_number)
#
# squares = []
# for value in range(1,10):
#     squar = value**2
#     squares.append(squar)
# print(squares)
#
# squares_1 = []
# for value in range(1,11):
#     squares_1.append(value**3)
# print(squares_1)

# nymbers = list(range(1, 1000001))
# for value in nymbers:
#     print(value)
# numbers_1 = list(range(1,1000001))
# a = min(numbers_1)
# b = max(numbers_1)
# c = sum(numbers_1)
# print(b)
# print(a)
# print(c)
#
# numbers = list(range(-20, 0))
# for count in numbers:
#     print(count)

# numb = list(range(3,31,3))
# for value in numb:
#     print(value)
squar = []
numbers = list(range(1,11))
for value in numbers:
    val = value**3
    squar.append(val)
print(squar)

squares = [value**3 for value in range(1,11)]
print(squares)