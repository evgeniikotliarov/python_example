import re


phone_book = {'\d':"[0-5]"}
print(phone_book)
string = """Armin [User, Katerina],\[33333\]."""

phone_numbers = r'(\d   %s)' % r'|'.join(phone_book.keys())
print(phone_numbers)

print(re.sub(r"([0-9]{n}<left>(?<!\\)\[)(?P<dig>.*?)((?<!\\)\])",
    lambda m1:re.sub( r"\[", r"\[", m1.group('left') +  re.sub(phone_numbers,
    lambda m2:'{number}'.format(number=phone_book[m2.group('dig')]),m1.group('names')) + re.sub( r"\]", r"\]")),string))
