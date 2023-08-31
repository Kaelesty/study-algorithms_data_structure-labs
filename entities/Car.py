from random import randint

class Car:
    def __init__(self, brand, vin, engineCap, price, averageSpeed):
        self.brand = brand
        self.vin = vin
        self.engineCap = engineCap
        self.price = price
        self.averageSpeed = averageSpeed

    def __str__(self):
        return f"[{self.vin}]"

    def toDict(self):
        return {
            "brand": self.brand,
            "vin": self.vin,
            "engineCap": self.engineCap,
            "price": self.price,
            "averageSpeed": self.averageSpeed
        }


def carFromDict(raw):
    return Car(
        raw["brand"],
        raw["vin"],
        raw["engineCap"],
        raw["price"],
        raw["averageSpeed"]
    )

def getRandomCar():
    return Car(
        f"brand #{randint(0, 50)}",
        randint(0, 10),
        randint(0, 50),
        randint(0, 50),
        randint(0, 50),
    )
