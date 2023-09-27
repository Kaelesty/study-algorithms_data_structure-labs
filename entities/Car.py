from random import randint

from dataclasses import dataclass

from typing import Union


@dataclass
class Car:
    brand: str
    vin: int
    engine_cap: float
    cost: int
    avr_speed: float


def get_random_car() -> Car:
    return Car(
        f"brand #{randint(0, 50)}",
        randint(100000, 999999),
        randint(1, 160) / 10,
        randint(10, 100),
        randint(5, 200),
    )

def get_random_car_with_cost(cost: int) -> Car:
    car: Car = get_random_car()
    car.cost = cost
    return car


def car_to_dict(car: Car) -> dict[str, Union[str, int, float]]:
    return {
        "brand": car.brand,
        "vin": car.vin,
        "engine_cap": car.engine_cap,
        "cost": car.cost,
        "avr_speed": car.avr_speed,
    }


def car_from_dict(raw: dict[str, Union[str, int, float]]) -> Car:
    return Car(
        raw["brand"], raw["vin"], raw["engine_cap"], raw["cost"], raw["avr_speed"]
    )
