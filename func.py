a = 2
b = 5
c = 0


# Function declaration
def sum(x, y):
    global c
    c = x + y


# Function call

# sum(5, 8)
# print("starting")
# sum(10, 7)
# print("ending")
# sum(3, 4)


sum(a, b)

print(c)
