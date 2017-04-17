names = ["Dima", "Gosha", "Oleg", "Vasiliy"]
print(names[0])
print(names[1])
print(names[-1])
print(names[-2])
message = names[0].lower() + " " + "your email"
print(message)

motobikes = ["honda", "suzuki", "ktm", "yamaha"]
a = "ducatti"
motobikes.append(a)
dream = "I want " + "motobike " + motobikes[-1].capitalize()
print(dream.title())
print(motobikes)

max = "Maxim"
omka = "Omurbek"
misha = "Mikhail"
names.append(max)
names.append(omka)
print(names)
del names[-2]
poped_names = names.pop(1)
names.remove("Dima")
message = "Studens "
print(message, names)
print(poped_names)
print(names)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
names.insert(1, misha)
print(names)
two_guys = names.pop(0)
print(names)
message_2 = "Don't come to " + two_guys + ", I'm sorry"
message_3 = "Don't come to " + names.pop(2) + ", I'm sorry"
print(message_2)
print(message_3.title())
print(names)
del names[0]
del names[0]
print(names)