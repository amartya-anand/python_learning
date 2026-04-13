class Car:
    def __init__(self, brand, model):  # Constructor method
        self.brand = brand,
        self.model = model,

    def full_name(self):
        return f"{self.brand} {self.model}"


my_car = Car("Toyota", "Corolla")  # my_car object
print(my_car.model)
print(my_car.full_name())	            # Instance of a class

my_new_car = Car("Honda", "Civic")  # Instance of a class
print(my_new_car.brand)
print(my_new_car.full_name())  # Instance of a class
