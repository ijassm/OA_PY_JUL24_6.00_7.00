name = input("Enter your name: ")
location = input("Enter your location: ")

output = "Myself" + " " + name + "😊" + " " + "I am from" + " " + location

print(name + " " + "Welcome to Ocean Academy🖐🌊🙌")
print(output)
print(f"Myself {name}😊 I am from {location}")
print("Myself {}😊 I am from {}".format(name, location))
print("Myself {1}😊 I am from {0}".format(location, name))

number = 1
print("{:05d}".format(number))
