# Function Polymorphism

# print(len("hello"))
# print(len([1,3,54,12,56,3]))
# print(len((1,3,54,12,56,3)))
# print(len({
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }))


# Polymorphism class

# class Car:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Drive!")

# class Boat:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Sail!")

# class Plane:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Fly!")

# car1 = Car("Ford", "Mustang")       #Create a Car object
# boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
# plane1 = Plane("Boeing", "747")     #Create a Plane object

# for x in (car1, boat1, plane1):
#   x.move()

# class Vehicle:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     return "Move!"

# class Car(Vehicle):
#   pass

# class Boat(Vehicle):
#   def move(self):
#     return "Sail!"

# class Plane(Vehicle):
#   def move(self):
#     return ["Fly!"]

# car1 = Car("Ford", "Mustang")       #Create a Car object
# boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
# plane1 = Plane("Boeing", "747")     #Create a Plane object

# for x in (car1, boat1, plane1):
#   print(x.brand)
#   print(x.model)
#   print(x.move())
#   print()

# a = 1
# a = 5



# First product method.
# Takes two argument and print their
# product



# def product(a, b):
#     p = a * b
#     print(p)

# Second product method
# Takes three argument and print their
# product


# def product(a, b, c):
#     p = a * b*c
#     print(p)

# Uncommenting the below line shows an error
# product(4, 5)


# This line will call the second product method
# product(4, 5, 5)


# Function to take multiple arguments
def add(datatype, *args):

    # if datatype is int
    # initialize answer as 0
    if datatype == 'int':
        answer = 0

    # if datatype is str
    # initialize answer as ''
    if datatype == 'str':
        answer = ''

    # Traverse through the arguments
    for x in args:

        # This will do addition if the
        # arguments are int. Or concatenation
        # if the arguments are str
        answer = answer + x

    print(answer)


# Integer
add('int', 5, 6)

# String
add('str', 'Hi ', 'ocean🌊')
