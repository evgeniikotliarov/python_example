var = "Hello "
var_1 = "Dima, "
var_2 = "would you like to learn some Python today?"

message = var + var_1 + var_2 +  "!"
print(message)

name = "dima"
last_name = "ivanov"
person = "director"
man = name + " " +  last_name + " " + person
console = man.upper()
console_1 = man.lower()
console_2 = man.title()
print(console, console_1, console_2)

variable = "Albert Einstein once said"
variable_1 = "A person who never made a mistake never tried anything new."
result = variable + ", " + '"' + variable_1.lower() + '"'
print(result)

name = "dima "
name = name.rstrip()
last_name = " ivanov"
last_name = last_name.lstrip()
person = "   director "
person = person.strip()
man = name + " " +  last_name + " " + person
console = man.upper()
console_1 = man.lower()
console_2 = man.title()
print(console, console_1, console_2)
