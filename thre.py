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
# a = "ducatti"
# motobikes.append(a)
# dream = "I want " + "motobike " + motobikes[-1].capitalize()
# print(dream.title())
# print(motobikes)
#
# max = "Maxim"
# omka = "Omurbek"
# misha = "Mikhail"
# names.append(max)
# names.append(omka)
# print(names)
# del names[-2]
# poped_names = names.pop(1)
# names.remove("Dima")
# message = "Studens "
# print(message, names)
# print(poped_names)
# print(names)
# print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
# names.insert(1, misha)
# print(names)
# two_guys = names.pop(0)
# print(names)
# message_2 = "Don't come to " + two_guys + ", I'm sorry"
# message_3 = "Don't come to " + names.pop(2) + ", I'm sorry"
# print(message_2)
# print(message_3.title())
# print(names)
# del names[0]
# del names[0]
# print(names)