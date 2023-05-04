import requests


def search_book(query):
    r = requests.get(f"https://gutendex.com/books/?search={query}")
    return r.json()


def get_book_by_id(id):
    r = requests.get(f"https://gutendex.com/books/{id}")
    return r.json()
