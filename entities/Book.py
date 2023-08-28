from random import randint


class Book:
    def __init__(self, author, publisher, pages, price, isbn):
        self.author = author
        self.publisher = publisher
        self.pages = pages
        self.price = price
        self.isbn = isbn

    def __str__(self):
        return f"[{self.isbn}]"


def getRandomBook():
    return Book(
        f"Author #{randint(0, 50)}",
        f"Publisher #{randint(0, 50)}",
        randint(0, 50),
        randint(0, 50),
        randint(0, 50),
    )
