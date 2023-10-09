"""
(автор, издательство, кол-во страниц, стоимость, ISBN)
"""
from dataclasses import dataclass
from random import randint


@dataclass
class Book:
    author: str
    publisher: str
    pages: int
    cost: int
    isbn: str


def get_random_book() -> Book:
    return Book(
        f"author #{randint(0, 2000)}",
        f"publisher #{randint(0, 2000)}",
        randint(30, 2000),
        randint(0, 2000),
        f"{randint(1, 9)}-{randint(1000, 9999)}-{randint(1000, 9999)}-{randint(1, 9)}"
    )


def get_random_book_with_pages(pages: int) -> Book:
    book: Book = get_random_book()
    book.pages = pages
    return book


def get_random_book_with_cost(cost: int) -> Book:
    book: Book = get_random_book()
    book.cost = cost
    return book


def get_random_book_with_author(author: int) -> Book:
    book: Book = get_random_book()
    book.author = str(author)
    return book