class Vehicle:

    total_vehicles = 0

    def __init__(self, name):
        self.name = name
        Vehicle.total_vehicles += 1

    def start(self):
        print(f"{self.name} is starting.")



class Car(Vehicle):
    def __init__(self, name, brand):
        super().__init__(name)
        self.brand = brand

    def car_info(self):
        print(f"Car Name: {self.name}, Brand: {self.brand}")



class ElectricCar(Car):
    def __init__(self, name, brand, battery_capacity):
        super().__init__(name, brand)
        self.battery_capacity = battery_capacity

    def battery_info(self):
        print(f"{self.name} has a battery capacity of {self.battery_capacity} kWh")



v1 = Vehicle("Truck")
v1.start()

c1 = Car("Sedan", "Toyota")
c1.start()
c1.car_info()

e1 = ElectricCar("Tesla Model 3", "Tesla", 75)
e1.start()
e1.car_info()
e1.battery_info()


print("Total Vehicles Created:", Vehicle.total_vehicles)
