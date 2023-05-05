from book import BookSource
from book.models import Book

from django import forms
from django.contrib.postgres.forms import SimpleArrayField


class BookForm(forms.Form):
    id = forms.CharField(required=False)
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
        self.cleaned_data.pop("id")
        self.cleaned_data.pop("source")

        book = Book.objects.create(**self.cleaned_data)
        return book
