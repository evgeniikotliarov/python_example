class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 100


    def descriptive_name(self):
        long_name = str(self.make) + ' ' + str(self.model) + ' ' + str(self.year)
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " kilometers on it.")


    def update_odometer(self, kilometer):
        if kilometer >= self.odometer_reading:
            self.odometer_reading = kilometer
        else:
            print("OOPS, You can't roll back an odometer!")


    def increment_odometer(self, km):
        self.odometer_reading += km



my_used_car = Car("Audi", "A6", 2010)
print(my_used_car.descriptive_name())
my_used_car.update_odometer(130100)
my_used_car.read_odometer()
my_used_car.increment_odometer(5505)
my_used_car.read_odometer()

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 70
        self.battery = Battery()

    def fill_gas_tank(self):
        print("This car doesn't need a gas tank!")

class Battery():
    def __init__(self, battery_size=40):
        self.battery_size = battery_size


    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

my_tesla = ElectricCar('tesla', "model's", 2016)
my_tesla.battery.describe_battery()