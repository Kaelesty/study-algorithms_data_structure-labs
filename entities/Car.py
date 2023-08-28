from random import randint

class Car:
    def __init__(self, brand, vin, engineCap, price, averageSpeed):
        self.brand = brand
        self.vin = vin
        self.engineCap = engineCap
        self.price = price
        self.averageSpeed = averageSpeed

    def __str__(self):
        return f"[{self.averageSpeed}]"


def getRandomCar():
    return Car(
        f"brand #{randint(0, 50)}",
        randint(0, 50),
        randint(0, 50),
        randint(0, 50),
        randint(0, 50),
    )
