a = [1, 2, 3, 4, 5]
b = [1, 2, 0, 5]


def sumValues(iterator):
    s = 0
    for i in iterator:
        s += i
    return s


def productValues(iterator):
    s = 1
    for i in iterator:
        if i != 0:
            s *= i
    return s


# print(sum([1, 2, 3, 4, 5]))
# print(sum((1, 2, 3, 4)))
# print(sum({1, 2, 3}))
# print(sum("Hello"))

# print(productValues([1, 2, 0, 4, 5]))
# print(productValues((1, 2, 0, 4)))
# print(productValues({1, 2, 3}))
# print(sum("Hello"))
