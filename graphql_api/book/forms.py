from core.services.google_books import get_book_by_id as get_book_by_id_google
from core.services.gutendex import get_book_by_id as get_book_by_id_gutendex
from book import BookSource
from book.models import Book

from django import forms
from django.contrib.postgres.forms import SimpleArrayField


class BookForm(forms.Form):
    """
    Complex book form. Create books by different sources(DB, GOOGLE and GUTENDEX)
    """

    external_id = forms.CharField(required=False)
    title = forms.CharField(required=False)
    subtitle = forms.CharField(required=False)
    description = forms.CharField(required=False)
    publisher = forms.CharField(required=False)
    publication_date = forms.CharField(required=False)
    image = forms.CharField(required=False)
    categories = SimpleArrayField(forms.CharField(max_length=100), required=False)
    authors = SimpleArrayField(forms.CharField(max_length=100), required=False)
    source = forms.ChoiceField(
        choices=BookSource.CHOICES,
    )

    def clean(self):
        super().clean()
        data = self.cleaned_data
        source = data.get("source")

        required_fields = [
            "external_id",
        ]  # For external sources

        if source == BookSource.DB:
            required_fields = [
                "title",
                "subtitle",
                "description",
                "publisher",
                "publication_date",
                "categories",
                "authors",
            ]

        for field_name in required_fields:
            if not data.get(field_name):
                self.add_error(field_name, f"{field_name} is required")

        return data

    def save(self):
        source = self.cleaned_data.pop("source")
        external_id = self.cleaned_data.pop("external_id")

        if source == BookSource.DB:
            book = Book.objects.create(**self.cleaned_data)
        elif source == BookSource.GOOGLE:
            book_google = get_book_by_id_google(external_id)
            if book_google:
                book = Book.objects.create(
                    title=book_google["volumeInfo"].get("title"),
                    subtitle=book_google["volumeInfo"].get("subtitle", ""),
                    publisher=book_google["volumeInfo"].get("publisher"),
                    publication_date=book_google["volumeInfo"].get("publishedDate", ""),
                    description=book_google["volumeInfo"].get("description", ""),
                    categories=book_google["volumeInfo"].get("categories", []),
                    authors=book_google["volumeInfo"].get("authors", []),
                )
        elif source == BookSource.GUTENDEX:
            book_gutendex = get_book_by_id_gutendex(external_id)
            if book_gutendex:
                book = Book.objects.create(
                    title=book_gutendex.get("title"),
                    subtitle=book_gutendex.get("subtitle", ""),
                    publisher=book_gutendex.get("publisher", ""),
                    publication_date=book_gutendex.get("publishedDate", ""),
                    description=book_gutendex.get("description", ""),
                    categories=book_gutendex.get("subjects", []),
                    authors=[j["name"] for j in book_gutendex.get("authors", [])],
                )
        return book
