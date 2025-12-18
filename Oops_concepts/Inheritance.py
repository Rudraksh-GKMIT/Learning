from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, model, fuel, fuel_capacity):
        self.__model = model  # private
        self.__fuel = fuel  # private
        self.__fuel_capacity = fuel_capacity #private

    def get_model(self):  # getter function
        return self.__model

    def get_fuel(self):
        return self.__fuel

    def refuel(self, amount):
        total = amount + self.__fuel
        if amount < 0:
            print("Amount should be positive")
        elif total > self.__fuel_capacity:
            print("Amount added exceed the fuel capacity")
        else:
            self.__fuel = total

    def use_fuel(self, amount):
        if 0 < amount <= self.__fuel:
            self.__fuel -= amount

    def status(self):
        return f"{self.__fuel}/{self.__fuel_capacity}"

    @abstractmethod
    def horn(self):
        pass


class Car(Vehicle):  # Single Inheritance
    def __init__(self, model, fuel, fuel_capacity):
        super().__init__(model, fuel, fuel_capacity)

    def horn(self):
        return "honk honk "


class Bike(Vehicle):  # Hierarchical Inheritance
    def __init__(self, model, fuel, fuel_capacity):
        super().__init__(model, fuel, fuel_capacity)

    def horn(self): 
        return "beep beep"


class BMW(Car):  # Multilevel Inheritance
    def __init__(self, model, fuel, fuel_capacity):
        super().__init__(model, fuel, fuel_capacity)

    def info(self):
        return "This car fall under the brand BMW "


class Electric:
    def __init__(self):
        self.__battery = 100
        self.__efficiency = 2.5
    
    def battery_status(self):
        return f"Battery left is {self.__battery}"

    def battery_usage(self, usage):
        if usage <= 0 or usage >= 100:
            print("Enter a valid value")
        elif usage > self.__battery:
            print("The usage cannot exceed the current battery level")
        else:
            self.__battery -= usage

    def km_left(self):
        dis = self.__battery * self.__efficiency
        return f"Total distance can be covered is {dis}"

    def charge(self, upload):
        if upload <= 0 or upload > 100:
            print("Enter a valid number")
        elif (upload + self.__battery) > 100:
            print("Battery charge can't exceed 100")
        else:
            self.__battery += upload


class Hybrid(Vehicle, Electric):  # Multiple Inheritance
    def __init__(self, model, fuel, fuel_capacity):
        Vehicle.__init__(self, model, fuel, fuel_capacity)
        Electric.__init__(self)

    def access(self):
        return "There can work on both Electric and Petrol for fuel"


class HybridBMW(Hybrid, BMW):  # Hybrid Inheritance
    def __init__(self, model, fuel, fuel_capacity):
        Vehicle.__init__(self, model, fuel, fuel_capacity)
        Electric.__init__(self)


def test_horn(vehicle):  # duck type polymorphism
    print(f"{vehicle.get_model()} says: {vehicle.horn()}")


car = Car("2500 CC", 10, 40)
print(car.get_fuel())  # 10
car.refuel(10)
print(car.get_fuel())  # 20
print(car.horn())  # honk honk
print("fuel status", car.status())
print()
test_horn(car)
hb = HybridBMW("Hybrid-BMW", 5, 60)
print("HybridBMW model:", hb.get_model())
print("HybridBMW fuel:", hb.get_fuel())
print("HybridBMW horn:", hb.horn())
print("HybridBMW km left:", hb.km_left())
print("HybridBMW",hb.battery_status())
hb.battery_usage(50)
print("HybridBMW km left", hb.km_left())
print("HybridBMW",hb.battery_status())
