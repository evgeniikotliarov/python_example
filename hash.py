# print(man['last_name'], man['first_name'])
# numbers = {'Dima':5, 'Leha':7, 'Alex':9}
# print(numbers["Leha"])

# favorite_language = {
#     'Matz': 'ruby',
#     'Jen': 'python',
#     'Sarah': 'c',
#     'Joshua': 'java'
# }
# print("We love " + favorite_language['Matz'].upper() + " very" "\n" "and " + favorite_language['Joshua'].title() + " very nice")

# for k,v in favorite_language.items():
#     print('\n' + k.upper())
#     print(v.title())

# friends = ['Jen', 'Cola', 'Java']
# for name in favorite_language.values():
#     print(name.title())
#     for fr in friends:
#         if fr in favorite_language:
#             print('Hi ' + name.title() + ' I like to.')


# people = []
# for i in range(10):
#     new_man = {'nationality':'russian', 'country':'russia', 'age':'20'}
#     people.append(new_man)
#     for pip in people[0:3]:
#         if pip['age'] == '20':
#             pip['age'] = '25'
#             pip['country'] = 'France'
#             pip['nationality'] = 'French'
#
# for d in people:
#     print(d)
#
# print("Total " + str(len(people)))

favorite_places = {
    'city':['John'],
    'river': ['Vasia', 'Katya', 'Gena'],
    'mountain': ['sasha', 'sveta', 'Omka']
}
for k,v in favorite_places.items():
    print('\n'"Thi is " + k.title() + " very nice")
    for t in v:
        print("\t" + t.title())


# man_1 = {
#     'first_name': 'Dima',
#     'last_name': 'Kinder',
#     'age': '30',
#     'hair_color':'Red'}
#
# man = {
#     'first_name':'Jack',
#     'last_name':'Doe',
#     'age':'30',
#     'hair_color':'Black'
# }
# woman = {
#     'first_name':'Jena',
#     'last_name':'Jackson',
#     'age':'25',
#     'hair_color':'White'
# }
# people = [man, man_1, woman]
#
# for i in people:
#     print(i)

