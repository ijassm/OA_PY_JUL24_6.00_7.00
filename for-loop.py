# range(10) - range(0,10,1)
# range(3,10) - range(3,10,1)
# range(3,10,2) - range(3,10,2)

matrix = int(input("Enter number : ")) + 1

# for i in range(1, matrix):
#     print("{:2d} ".format(i) * matrix)

# for i in range(1, matrix):
#     print("* " * matrix)

# loops = (matrix**2)

# for i in range(1, loops):
#     print("{:3d}".format(i), end="")
#     if i % matrix == 0:
#         print()

# for i in range(1, matrix):
#     print("✨ " * i)

# for i in range(matrix, 0, -1):
#     print("✨ " * i)

space = matrix - 2

for i in range(1, matrix):
    print(" " * space, end="")
    print("# " * i)
    space -= 1


#         *
#        * *
#       * * *
#      * * * *
#     * * * * *
