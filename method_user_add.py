pizza = ['pipperoni', 'chilli', 'mozarella']
print(pizza)
for piz in pizza:
    print(piz + " I like it")

for pis in pizza:
    print("Do you like " + pis.title() + ".\n")
print("Bla bla bla")

for value in range(1,5):
    print(value)

for value in range(1,9):
    print(value)

numbers = list(range(1,6))
print(numbers)

even_number = list(range(0,21,5))
print(even_number)

squares = []
for value in range(1,10):
    squar = value**2
    squares.append(squar)
print(squares)

squares_1 = []
for value in range(1,11):
    squares_1.append(value**3)
print(squares_1)
