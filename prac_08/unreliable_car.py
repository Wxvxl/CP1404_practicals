from prac_08.car import Car
import random


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = 0

    def drive(self, distance):
        breakdown_chance = random.uniform(0, 100)
        if breakdown_chance > self.reliability:
            print("Uh Oh! Something unfortunate happened!")
            driven_distance = 0
            return driven_distance
        else:
            driven_distance = super().drive(distance)
            return driven_distance
