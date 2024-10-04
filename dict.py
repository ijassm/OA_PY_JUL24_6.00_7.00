# se = {31, 2, 3, 4, 4, True, 1, 0, 5646}
# l = [31, 2, 3, 4, 4, True, 1, 0, 5646]
# t = (31, 2, 3, 4, 4, True, 1, 0, 5646)
# s = "Hello"

# print(type(d))
# print(d)

# for i in s:
#     print(i)

# example

# l = ["XYZ", 20, "pondy", "+91 9876543210"]

# l[3] = 20

# print(l)

# ages = [20, 45, 36, 75]
# names = ["xyz", "abc", "tui"]

doc1 = {
    "name": "Mathew",
    "age": 18,
    "address": {
        "street": "ABC Street",
        "city": "Pondy",
        "state": "Tamil Nadu",
        "country": "India",
    },
    "skills": ["Python", "HTML", "CSS", "C", "C++"],
}

doc2 = {
    "name": "Ramya",
    "age": 20,
    "skills": ["Python", "HTML", "CSS", "C", "PHP"],
    "address": {
        "street": "ABC Street",
        "city": "Pondy",
        "state": "Tamil Nadu",
        "country": "India",
    },
}

doc3 = {
    "name": "Pushpaja",
    "age": 19,
    "skills": ["Python", "HTML", "CSS", "Java", "C++"],
    "address": {
        "street": "ABC Street",
        "city": "Pondy",
        "state": "Tamil Nadu",
        "country": "India",
    },
}


# doc1["age"] = 21
# doc1["gender"] = "male"

# print(doc1)
# print(type(doc1))
# print("Name : ", doc1["name"])
# print("Age : ", doc1["age"])
# print("Street : ", doc1["address"]["street"])
# print("City : ", doc1["address"]["city"])
# print("State : ", doc1["address"]["state"])
# print("Country : ", doc1["address"]["country"])

print("\n")

# print(doc2)
# print(doc2["name"])
# print(doc2["age"])
# print(doc2["location"])
# print(type(doc2))


students = [
    {
        "name": "Mathew",
        "age": 18,
        "address": {
            "street": "ABC Street",
            "city": "Pondy",
            "state": "Tamil Nadu",
            "country": "India",
        },
        "skills": ["Python", "HTML", "CSS", "C", "C++"],
    },
    {
        "name": "Ramya",
        "age": 20,
        "skills": ["Python", "HTML", "CSS", "C", "PHP"],
        "address": {
            "street": "ABC Street",
            "city": "Pondy",
            "state": "Tamil Nadu",
            "country": "India",
        },
    },
    {
        "name": "Pushpaja",
        "age": 19,
        "skills": ["Python", "HTML", "CSS", "Java", "C++"],
        "address": {
            "street": "ABC Street",
            "city": "Pondy",
            "state": "Tamil Nadu",
            "country": "India",
        },
    },
]


for i in students:
    print("Name : ", i["name"])
    print("Age : ", i["age"])
    print("Street : ", i["address"]["street"])
    print("City : ", i["address"]["city"])
    print("State : ", i["address"]["state"])
    print("Country : ", i["address"]["country"])
    print("")
