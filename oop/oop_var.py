class Car:
    wheels = 5

    def __init__(self):
        # Instance variable
        self.milage = 10
        self.company = 'BMW'


my_car1 = Car()
my_car2 = Car()

# Changing the class variable
Car.wheels = 6

print(my_car1.milage, my_car1.company, my_car1.wheels)
print(my_car2.milage, my_car2.company, my_car2.wheels)
