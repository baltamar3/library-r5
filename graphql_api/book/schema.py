import graphene

# from core.services.google.books import search_book

from . import BOOK_SEARCH_FIELDS
from ..utils import filter_by_query_param
from ..descriptions import DESCRIPTIONS
from .types import BookType
from book.models import Book

from django.db.models import Value
from graphql_jwt.decorators import login_required


class BookQueries(graphene.ObjectType):
    books = graphene.List(
        BookType,
        query=graphene.String(required=True, description=DESCRIPTIONS["books"]),
    )

    @login_required
    def resolve_books(root, info, query):
        books = Book.objects.all().annotate(source=Value("db"))
        qs = filter_by_query_param(books, query, BOOK_SEARCH_FIELDS)
        if not qs:
            pass
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
