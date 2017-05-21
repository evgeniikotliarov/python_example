class Users:
    def __init__(self, first_name, last_name, age, mail):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.mail = mail

    def describe_user(self):
        print('First name '+self.first_name.title())
        print('Last name '+self.last_name.title())
        print('Age ' + self.age)


    def greet_user(self):
        print(" Hello "+ self.first_name.title()+ " we are greeting you")

user = Users('ala', 'lada', '24', 'asa')
user_1 = Users('vova', 'doe', '21', 'gsd')
user_2 = Users('Iuriy', 'Li', '20', 'lju')

user.describe_user()
user.greet_user()
user_1.describe_user()
user_2.greet_user()
user_2.describe_user()
user_1.greet_user()
