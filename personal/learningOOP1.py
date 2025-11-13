class Car:
    CONSUMPTION_RATE = 10 #fuel consumption rate per hour
    def __init__(self, make, speed):
        self.make = make
        self.speed = speed
        self.__fuel = 100 #hidden attribute
        self.__distance = 0 #fully private now with __ instead of just hidden with _

    def drive(self, hours):
        if self.__fuel - hours * Car.CONSUMPTION_RATE < 0:
            print("Not enough fuel!")
            return
        if hours < 0:
            print("Can't drive negative hours!")
            return
        self.__distance += self.speed * hours
        self.__fuel -= hours * Car.CONSUMPTION_RATE

    def report(self):
        print(f"{self.make} has driven {self.__distance} miles with {self.__fuel} fuel remaining.")

    def reset_trip(self):
        self.__distance = 0

    #double underscore makes it follow private, not just hidden,
    #now, in order to change __distance, we have to use getters
    #and setters

    def get_distance(self): #getter
        return self.__distance

    def set_distance(self, value): #setter
        if value < 0:
            print("Distance can't be negative!")
            return
        self.__distance = value

    def get_fuel(self): #getter
        return self.__fuel

    def set_fuel(self, value): #setter
        if value < 0 or value > 100:
            print("Fuel must be between 0 and 100!")
            return
        self.__fuel = value

#subclass ElectricCar that inherits from Car, allows for code reuse with different data
class ElectricCar(Car):
    def __init__(self, make, speed):
        super().__init__(make, speed) #lets you use methods from parent class
        self.__battery = 100

    def drive(self, hours):
        if self.__battery - hours * Car.CONSUMPTION_RATE < 0:
            print("Not enough battery!")
            return
        if hours < 0:
            print("Can't drive negative hours!")
            return
        self.set_distance(self.get_distance() + self.speed * hours)
        self.__battery -= hours * Car.CONSUMPTION_RATE

    def report(self):
        print(f"{self.make} has driven {self.get_distance()} miles with {self.__battery} battery remaining.")

    def get_battery(self):
        return self.__battery

    def set_battery(self, value):
        if value < 0 or value > 100:
            print("Battery must be between 0 and 100!")
            return
        self.__battery = value

class HybridCar(Car):
    MAX_BATTERY = 50
    MAX_FUEL = 50

    def __init__(self, make, speed):
        super().__init__(make, speed)
        self.__battery = HybridCar.MAX_BATTERY
        self.set_fuel(HybridCar.MAX_FUEL)

    def drive(self, hours):
        if (self.get_fuel() + self.__battery) - hours * Car.CONSUMPTION_RATE < 0:
            print("Not enough fuel or battery!")
            return
        if hours < 0:
            print("Can't drive negative hours!")
            return
        self.set_distance(self.get_distance() + self.speed * hours)
        self.__battery -= hours * Car.CONSUMPTION_RATE
        if self.__battery < 0:
            self.set_fuel(self.get_fuel() - abs(self.__battery))
            self.set_battery(0)

    def report(self):
        print(f"{self.make} has driven {self.get_distance()} miles with {self.get_fuel()} fuel and {self.__battery} battery remaining.")

    def get_battery(self):
        return self.__battery

    def set_battery(self, value):
        if value < 0 or value > 50:
            print("Battery must be between 0 and 50!")
            return
        self.__battery = value

class Garage:
    def __init__(self):
        self.cars = [] #list to hold cars

    def add_car(self, car):
        if not isinstance(car, Car):
            print("Only cars can be added!")
            return
        self.cars.append(car) #add car to garage

    def test_drive_all(self, hours):
        if hours < 0:
            print("Can't drive negative hours!")
            return
        for car in self.cars: #test drive all cars in garage for given hours
            car.drive(hours)

    def report_all(self):
        for car in self.cars: #report status of all cars in garage
            car.report()


# Create cars
car1 = Car("Toyota", 60)
car2 = ElectricCar("Tesla", 80)
car3 = HybridCar("Prius", 70)

# Create garage
garage = Garage()

# Add cars
garage.add_car(car1)
garage.add_car(car2)
garage.add_car(car3)

# Drive them all
garage.test_drive_all(5)

# Report all
garage.report_all()