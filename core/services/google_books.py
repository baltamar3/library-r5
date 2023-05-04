import requests


def search_book(query):
    r = requests.get(
        f"https://www.googleapis.com/books/v1/volumes?q={query}&maxResults=5"
    )
    return r.json()


def get_book_by_id(id):
    r = requests.get(f"https://www.googleapis.com/books/v1/volumes/{id}")
    return r.json()
