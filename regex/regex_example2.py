import re

number_mapping = {'\d': '[0-9]',
                  '\w': '[a-zA-Z]',
                  '3': 'three'}
s = "\d testing \w 3"
for k, v in number_mapping.items():
    s = s.replace(k, v)
print(s)
# print( re.sub(r'\d', lambda x: number_mapping[x.group()], s))