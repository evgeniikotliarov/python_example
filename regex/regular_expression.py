import re


input_filename = "../regex/text.txt"
result_file = "../regex/results.txt"

inputfile = open(input_filename, mode='r', encoding='Latin-1')
resultfile = open(result_file, mode='w', encoding='Latin-1')
mytext = inputfile.read()
inputfile.close()

lookfor = r"[\w.-]+@[A-Za-z-]+\.[\w.]+"

results = re.findall(lookfor, mytext)

for item in results:
    resultfile.write(item)
    print(item)



resultfile.close()

print("Total: " + str(len(results)))
