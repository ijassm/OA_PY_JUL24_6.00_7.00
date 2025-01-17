class Vechile:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")

    def start_engine(self):
        print("Engine started...")
    
    def stop_engine(self):
        print("Engine stopped...")
    
    def accelerate(self, speed):
        print(f"Accelerating to {speed} km/h...")


class Car(Vechile):
    def __init__(self, model, year):
        super().__init__("car", model, year)
        self.num_doors = 4
        self.has_sunroof = True
        self.has_airbag = True
        self.num_wheels = 4


obj1 = Car("V1", 2022)

print(obj1.make)
print(obj1.model)
print(obj1.num_doors)
print(obj1.num_wheels)
obj1.start_engine()
obj1.stop_engine()


        