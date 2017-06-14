import re

number_mapping = {'1': 'one',
                  '2': 'two',
                  '3': 'three'}
s = "1 testing 2 3"

print( re.sub(r'\d', lambda x: number_mapping[x.group()], s))