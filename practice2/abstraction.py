#Abstract Vehicle
from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass
class Car(Vehicle):
    def start(self):
        print("Car starts with key")
    def stop(self):
        print("car stops")
class Bike(Vehicle):
    def start(self):
        print("bike starts")
    def stop(self):
        print("bike stops")
vehicles=[Car(),Bike()]
for vehicle in vehicles:
    vehicle.start()
    vehicle.stop()