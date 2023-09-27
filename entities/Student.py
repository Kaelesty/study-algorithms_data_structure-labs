"""
Student (минимум 10 элементов),
содержащие следующие поля (ФИО, номер группы, курс, возраст, средняя оценка за время обучения),
где в качестве ключевого элемента при добавлении будет выступать средняя оценка.
"""

from dataclasses import dataclass
from random import randint

@dataclass
class Student:
    fullname: str
    group: int
    year: int
    age: int
    avr_rating: float


def get_random_student() -> Student:
    return Student(
        f"student #{randint(1, 50)}",
        randint(1000, 9999),
        randint(1, 4),
        randint(18, 50),
        randint(100, 500) / 100
    )


def student_to_dict(student: Student) -> dict:
    return {
        "fullname": student.fullname,
        "group": student.group,
        "year": student.year,
        "age": student.age,
        "avr_rating": student.avr_rating
    }


def student_from_dict(raw: dict) -> Student:
    return Student(
        raw["fullname"], raw["group"], raw["year"], raw["age"], raw["avr_rating"]
    )


def get_random_student_with_avr_rating(rating: float) -> Student:
    student: Student = get_random_student()
    student.avr_rating = rating
    return student
