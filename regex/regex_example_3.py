import re

string = "Once you have accomplished small things, you may attempt great ones safely."

print(string)
print("+++++++++++++++++++++++++++++++++++++")
print(re.findall(r"\ba[\w]*", string))


it = re.finditer(r"\ba[\w]*", string)
for match in it:
    print("'{g}' was found between the indices {s}".format(g=match.group(), s=match.span()))

print("=======================================")
print(re.split("\W+", string))

print(re.split("\W+", string, 2))

print(re.split("(:)", string))

print(re.sub("[ ,.]", ":", string))

print(re.sub("[ ,.]", ":", string, 2))

print(re.subn("[ ,.]", ":", string))

print(re.findall(r"\b\w{5}\b", string))

print(re.findall(r"\b\w{5,7}\b", string))

print(re.findall(r"\b\w{8,}\b", string))
