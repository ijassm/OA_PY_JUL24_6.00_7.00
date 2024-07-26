import datetime

current_date = datetime.date.today()

print(current_date.month)
print(current_date.year)
print(current_date.day)
print(current_date.weekday())
# print(current_date.)

day = current_date.weekday()

match day:
    case 0:
        print("Monday")
    case 1:
        print("Tuesday")
    case 2:
        print("Wednesday")
    case 3:
        print("Thursday")
    case 4:
        print("Friday")
    case 5:
        print("Saturday")
    case 6:
        print("Sunday")
    case _:
        print("Invalid")
