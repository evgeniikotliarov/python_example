country = ["russia", "poland", "israel", "china", "usa", "germany", "turkey", "egypt"]
var = sorted(country)
print(var)
print(country)
country.sort(reverse=True)
print("=============================")
print(country)
country.reverse()
print(country)
var_1 = len(country)
print(var_1)
river = ["nil", "amazonka", "nooruz", "huanhe", "volga"]
mountian = ["tibet", "ural", "tian-shan", "andi", "alpy"]
city = ["riekyavik", "moskow", "warshaw", "berlin", "new-york", "tokio"]
list = []
list.append(country[1])
list.append(river[0])
list.append(mountian[-1])
list.append(city[-2])
poped = list.pop(-1)
print(list)
print(poped)