class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


    def descriptive_name(self):
        full_name = self.make +' '+ self.model + ' ' + str(self.year)
        return full_name.title()


my_new_car = Car('Toyota', 'camry', 2015)
print(my_new_car.descriptive_name())