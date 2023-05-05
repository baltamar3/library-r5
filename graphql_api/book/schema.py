from core.services.google_books import search_book as search_book_in_google
from core.services.gutendex import search_book as search_book_in_gutendex

from . import BOOK_SEARCH_FIELDS
from ..utils import filter_by_query_param
from ..descriptions import DESCRIPTIONS
from .types import BookType
from .forms import BookForm
from book.models import Book

import graphene
from graphql_jwt.decorators import login_required
from graphene_django.forms.mutation import DjangoFormMutation
from django.db.models import Value


class BookQueries(graphene.ObjectType):
    books = graphene.List(
        BookType,
        query=graphene.String(
            required=True,
            description=DESCRIPTIONS["books"],
        ),
    )

    @login_required
    def resolve_books(root, info, query):
        books = Book.objects.all().annotate(source=Value("db"))
        qs = filter_by_query_param(books, query, BOOK_SEARCH_FIELDS)
        if not qs:
            google_books = search_book_in_google(query)["items"]
            google_books = [
                dict(
                    id=i["id"],
                    title=i["volumeInfo"]["title"],
                    subtitle=i["volumeInfo"].get("subtitle"),
                    publisher=i["volumeInfo"].get("publisher"),
                    publication_date=i["volumeInfo"].get("publishedDate"),
                    description=i["volumeInfo"].get("description"),
                    categories=i["volumeInfo"].get("categories", []),
                    authors=i["volumeInfo"].get("authors", []),
                    source="google",
                )
                for i in google_books
            ]
            gutendex_books = search_book_in_gutendex(query)["results"]
            gutendex_books = [
                dict(
                    id=i.get("id"),
                    title=i.get("title"),
                    subtitle=i.get("subtitle"),
                    publisher=i.get("publisher"),
                    publication_date=i.get("publishedDate"),
                    description=i.get("description"),
                    categories=i.get("subjects", []),
                    authors=[j["name"] for j in i.get("authors", [])],
                    source="gutendex",
                )
                for i in gutendex_books
            ]
            qs = google_books + gutendex_books
        return qs


class DeleteBook(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        id = graphene.ID(required=True)

    # The class attributes define the response of the mutation
    book = graphene.Field(BookType)

    @login_required
    def mutate(root, info, id):
        book = Book.objects.get(pk=id)
        if book is not None:
            book.delete()
        return DeleteBook(book=book)


class CreateBook(DjangoFormMutation):
    class Meta:
        form_class = BookForm

    @classmethod
    @login_required
    def mutate(cls, root, info, input):
        return super().mutate(root, info, input)
