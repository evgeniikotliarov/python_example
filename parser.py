string = 'name=vasya&password=123456&age=120'
string_1 = string.split('&')
data = {}
for entry in string_1:
    key, value = entry.split("=")
    data[key] = value

