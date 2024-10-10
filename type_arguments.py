# Arbitrary Arguments, *args
# def sum(*a):
#     s = 0
#     for i in a:
#         s += i
#     return s


# def product(*a):
#     p = 1
#     for i in a:
#         if i != 0:
#             p *= i
#     return p


# print(sum(5, 8))
# print(sum(3, 9))
# print(sum(3, 9, 0, 6))
# print(product(3, 9, 0, 6))
# print(sum(3, 9, 6, 5))
# print(sum(3))


# Keyword Arguments


# def student(name, age, location):
#     print(f"Name: {name}")
#     print(f"Age: {age}")
#     print(f"Location: {location}")


# student(age=20, location="pondy", name="Ramya")
# student("Pushpaja", 19, "pondy")


# Arbitrary Keyword Arguments, **kwargs


# def student(**data):
#     print(data)
#     print(type(data))
#     # print(f"Name: {data["name"]}")
#     # print(f"Age: {data["age"]}")
#     # print(f"Location: {data["location"]}")


# student(age=20, location="pondy", name="Ramya")
# student()


# Default Parameter Value


def student(name, age, location="pondy"):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Location: {location}")


student("abc", 22, "chennai")
student("xyz", 20)
