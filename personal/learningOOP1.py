class Car:
    def __init__(self, make, speed, distance = 0):
        self.make = make
        self.speed = speed
        self.distance = distance

    def drive(self, hours):
        self.distance += self.speed * hours
        return self.distance

    def report(self):
        print(self.make + " has driven " + str(self.distance) + " miles.")