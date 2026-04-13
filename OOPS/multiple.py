class Battery:
    def battery_info(self):
        return "Battery info"


class Engine:
    def engine_info(self):
        return "Engine info"


class ElectricCarTwo(Battery, Engine):
    pass


my_new_tesla = ElectricCarTwo("Tesla", "Model Y")
print(my_new_tesla.battery_info())
print(my_new_tesla.engine_info())
