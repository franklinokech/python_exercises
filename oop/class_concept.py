class Computer:

    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):

        print('My Configuration is : ', self.cpu, self.ram)


# self is the object you are passing

comp1 = Computer('Core i5', 16)
comp2 = Computer('Core i3', 8)
comp3 = Computer('Core i7', 4)

# Using the object itself to call the method
comp1.config()
comp2.config()
comp3.config()
