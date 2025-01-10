# def greet(name):
#     def greeting():
#         print("Hello", name)
#     return greeting

# greetPerson1 = greet("pushpaja")
# greetPerson2 = greet("ramya")


# greetPerson1()
# greetPerson2()

# def add5(num2):
#     return 5 + num2

# def add10(num2):
#     return 10 + num2

# print(add5(50))
# print(add10(10))


# def add(num1):
#     return lambda num2: num1 + num2


# add_5 = add(5)
# add_10 = add(10)

# print(add_5(2))
# print(add_10(15))
# print(add_5(3274683))

# def greet(name, messageFunc):
#     return  messageFunc() + " " + name.capitalize() 

# @greet
# def morningMessage():
#     return "Good Morning"

# def eveningMessage():
#     return "Good Evening"


# person1 = greet("pushpaja")
# # person2 = greet("ramya")

# # person1 = greet("pushpaja", morningMessage)
# # person2 = greet("ramya", eveningMessage)

# print(person1)
# print(person2)




# importing libraries
import time
import math

# decorator to calculate duration
# taken by any function.
def calculate_time(func):
    
    # added arguments inside the inner1,
    # if function takes any arguments,
    # can be added like this.
    def inner1(*args, **kwargs):

        # storing time before function execution
        begin = time.time()
        
        func(*args, **kwargs)

        # storing time after function execution
        end = time.time()
        print("Total time taken in : ", func.__name__, end - begin)

    return inner1



# this can be added to any function present,
# in this case to calculate a factorial
@calculate_time
def factorial(num):

    # sleep 2 seconds because it takes very less time
    # so that you can see the actual difference
    time.sleep(2)
    print(math.factorial(num))

# calling the function.
factorial(10)
