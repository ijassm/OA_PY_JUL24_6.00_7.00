l1 = [2, 5, 6, 8]
l2 = [2, 58]
l3 = [2, 5, 6]
l4 = [2, 5, 60, 58]


# def double(l):
#     output = []
#     for i in l:
#         output.append(i * 2)
#     return output


# def triple(l):
#     output = []
#     for i in l:
#         output.append(i * 3)
#     return output


# def quadruple(l):
#     output = []
#     for i in l:
#         output.append(i * 4)
#     return output


# d1 = double(l1)
# d2 = double(l2)
# d3 = double(l3)
# d4 = double(l4)

# t1 = triple(l1)
# t2 = triple(l2)
# t3 = triple(l3)
# t4 = triple(l4)

# q1 = quadruple(l1)
# q2 = quadruple(l2)
# q3 = quadruple(l3)
# q4 = quadruple(l4)


# print(d1)
# print(d2)
# print(d3)
# print(d4)
# print()
# print(t1)
# print(t2)
# print(t3)
# print(t4)
# print()
# print(q1)
# print(q2)
# print(q3)
# print(q4)


def hof(func, l):
    output = []
    for i in l:
        output.append(func(i))
    return output


def double(i):
    return i * 2


def triple(i):
    return i * 3


def quadruple(i):
    return i * 4


d1 = hof(double, l1)
d2 = list(map(double, l1))
t1 = hof(triple, l1)
q1 = hof(quadruple, l1)

print(d1)
print(d2)
print(t1)
print(q1)
