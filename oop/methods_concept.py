class Student:
    # Define class variable
    school = 'Wiobiero Secondary'

    # initialization

    def __init__(self, cat1, cat2, final):
        self.cat1 = cat1
        self.cat2 = cat2
        self.final = final

    # define an Instance method to calculate average
    def avg(self):
        return (self.cat1 + self.cat2 + self.final)/3


my_student1 = Student(32, 83, 99)
print(Student.school, my_student1.avg())

my_student2 = Student(27, 37, 82)
print(Student.school, my_student2.avg())
