# importing functools for reduce()
from functools import reduce

l1 = [2, 5, 6, 8]
l2 = [2, 58]
l3 = [2, 5, 6]
l4 = [2, 5, 60, 58]


def double(l):
    output = []
    for i in l:
        output.append(i * 2)
    return output


def triple(l):
    output = []
    for i in l:
        output.append(i * 3)
    return output


def quadruple(l):
    output = []
    for i in l:
        output.append(i * 4)
    return output


# d1 = double(l1)
# d2 = double(l2)

# t1 = triple(l1)
# t2 = triple(l2)


# q1 = quadruple(l1)
# q2 = quadruple(l2)


# print("\nDouble🎈🎈")
# print(l1, d1)
# print(l2, d2)
# print("\nTriple🎈🎈🎈")
# print(l1, t1)
# print(l2, t2)
# print("\nQuadruple🎈🎈🎈")
# print(l1, q1)
# print(l2, q2)
# print(q3)
# print(q4)


def hof(logicFunc, l):
    output = []
    for i in l:
        output.append(logicFunc(i))
    return output


# def double(i):
#     return i * 2

# double = lambda i: i * 2

# def triple(i):
#     return i * 3

# triple = lambda i: i * 2

# def quadruple(i):
#     return i * 4

# quadruple = lambda i: i * 2

# d1 = hof(double, l1)
# t1 = hof(triple, l1)
# q1 = hof(quadruple, l1)

# d1 = hof(lambda i: i * 2, l1)
# t1 = hof(lambda i: i * 3, l1)
# q1 = hof(lambda i: i * 4, l1)

# d1 = tuple(map(lambda i: i * 2, l1))
# t1 = list(map(lambda i: i * 3, l1))
# q1 = list(map(lambda i: i * 4, l1))


# print("\nDouble🎈🎈")
# print(l1, d1)
# print("\nTriple🎈🎈")
# print(l1, t1)
# print("\nQuadruple🎈🎈")
# print(l1, q1)
# print(d2)
# print(t1)
# print(q1)


# reduce


# def sum(l):
#     acc = 0

#     for i in l:
#         acc += i

#     return acc


def myReduce(logicFunc, l1, initialValue=None):
    acc = initialValue
    if initialValue == None:
        acc = l1[0]
        l1 = l1[1:]

    for i in l1:
        returnValue = logicFunc(acc, i)
        if returnValue != None:
            acc = returnValue
    return acc


def logicFunc(acc, cv):
    # print("accumalator", acc)
    # print("current value", cv)
    # print()
    return acc * cv


print(l1)
# s1 = reduce(logicFunc, l2)
# s2 = myReduce(logicFunc, l2)
s1 = reduce(lambda acc, cv: acc * cv, l2)
s2 = myReduce(lambda acc, cv: acc * cv, l2)
# s = sum(l1)
# print("s", s)
print("s1", s1)
print("s2", s2)
