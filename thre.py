names = ["Dima", "Gosha", "Oleg", "Vasiliy"]

message = names[1:3]
print(message)
message_1 = names[:3]
print(message_1)

motobikes = ["honda", "suzuki", "ktm", "yamaha"]
moto = motobikes[-3:]
print(moto)

foods = ['pizza', 'stake', 'bread', 'hot dog', 'cake', 'coffe']
foods_1 = foods[:]
print(foods_1)
foods.append('ice cream')
foods_1.append('lavash')
print(foods_1)
print(foods)
for value in foods:
    print(value)

dimensions = (250, 50)
print(dimensions[0])
# dimensions[0] = 300
for d in dimensions:
    print(d)

eat = ('pizza', 'sushi', 'cola', 'tea', 'mozzarella')
for value in eat:
    print(value)
eat = ('pizza', 'sushi', 'fanta', 'coffee', 'mozzarella')
for value in eat:
    print(value)
