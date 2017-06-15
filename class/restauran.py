class Restaurant:
    def __init__(self, title, type):
        self.title = title
        self.type = type

    def describe_restaurant(self):
        print(self.title.title())
        print(self.type.capitalize())

#     def open_rest(self):
#         print("We are " + self.title.title() + " for You")
#         print(self.cuisine_type)
#
# rest.describe_restaurant('diyar', 'chinese')
# print(rest.title)
# rest.open_rest()
    def get_rest(self, title, type):
        rest = Restaurant('diyar', 'chinese')
        rest.describe_restaurant()

a = Restaurant.get_rest('888','4554')



rest_1 = Restaurant('1','2')
rest_1.describe_restaurant()
