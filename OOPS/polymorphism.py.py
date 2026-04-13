class Car:
    def __init__(self, brand, model):  # Constructor method
        self.brand = brand,
        self.model = model,

    def full_name(self):
        return f"{self.brand} {self.model}"

    def fuel_type(self):
        return "Petrol/Diesel"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric"


my_car = Car("Toyota", "Corolla")  # my_car object
print(my_car.fuel_type())

my_tesla = ElectricCar("Tesla", "Model Y", "85kWH")
# print(my_tesla.brand)
print(my_tesla.fuel_type())
