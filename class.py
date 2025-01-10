class Student():
    pass

obj1 = Student()
obj2 = Student()



# print(Student)

def fullName(self):
    print(self.firstName + " " + self.lastName)

Student.fullName = fullName

obj1.firstName = 'xyz'
obj1.lastName = "abc"

obj2.firstName = 'pqr'
obj2.lastName = 'def'


obj1.fullName()
obj2.fullName()
# print(obj1)
# print(obj1.firstName + ' ' + obj1.lastName)

# print(obj2)
# print(obj2.firstName + ' ' + obj2.lastName)
