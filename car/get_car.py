class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 23


    def descriptive_name(self):
        full_name = self.make +' '+ self.model + ' ' + str(self.year)
        return full_name.title()

    def reading_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("False")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


my_new_car = Car('Toyota', 'camry', 2015)
print(my_new_car.descriptive_name())
my_new_car.odometer_reading = 100
my_new_car.update_odometer(222)
my_new_car.increment_odometer(15000)
my_new_car.reading_odometer()

