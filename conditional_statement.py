# sysUsername = "mathew"
# sysPassword = "12345"

# username = input("Enter your username : ")
# password = input("Enter your password: ")

# print(username)
# print(password)

# if username == sysUsername and password == sysPassword:
#     print("Your logged in successfully😊")
# else:
#     print("Invalid credentials! ��")


# amount = 1000

# note2000 = amount // 2000
# amount = amount - (2000 * note2000)
# note500 = amount // 500
# amount = amount - (500 * note500)
# note200 = amount // 200
# amount = amount - (200 * note200)

# print("RS 2000 - ", note2000)
# print("RS 500  - ", note500)
# print("RS 200  - ", note200)
# print("remaining amount  - ", amount)

# a = 20
# b = 20
# c = 20

# if a == b == c:
#     print("a b c are equal")
# elif a > b and a > c:
#     print("a is greater than b and c")
# elif b > c:
#     print("b is greater than c and a")
# else:
#     print("c is greater than a and b")


# units = 251
# amount = 0

# print("Units used - ", units)

# amount = amount + (50 * 0.50)
# units -= 50
# print(f"units till 50", amount)

# amount = amount + (100 * 0.75)
# units -= 100
# print(f"for next 100 units", amount)

# amount = amount + (100 * 1.20)
# units -= 100
# print(f"for next 100 units", amount)

# amount = amount + (units * 1.50)
# units = 0
# print(f"For unit above 250", amount)

# print(f"remaining units", units)
# print(f"total amount -", amount)


# print("An additional surcharge of 20% is added to the bill : ", amount * 0.20)

# Nested if

a = 30
b = 22
c = 20

if a == b == c:
    print("a b c are equal")
elif a > b and a > c:
    print("a is greater than all")
    if b < c:
        print("b is lesser than all")
    else:
        print("c is lesser than all")
elif b > c:
    print("b is greater than all")
    if a < c:
        print("a is lesser than all")
    else:
        print("c is lesser than all")
else:
    print("c is greater than all")
    if b < a:
        print("b is lesser than all")
    else:
        print("a is lesser than all")
