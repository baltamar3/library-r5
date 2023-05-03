from django.db import models
from django.contrib.postgres.fields import ArrayField


class Book(models.Model):
    title = models.CharField("title", max_length=128)
    subtitle = models.CharField("subtitle", max_length=128)
    authors = ArrayField(models.CharField(max_length=100), verbose_name="authors")
    categories = ArrayField(models.CharField(max_length=100), verbose_name="categories")
    publication_date = models.DateTimeField(auto_now_add=True)
    publisher = models.CharField("publisher", max_length=128)
    description = models.TextField(verbose_name="description")

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
        db_table = "book"

    def __str__(self):
        return self.title


Book.objects.create(
    title="Aventuras denjuaniro",
    authors=["Brayan Altamar"],
    categories=["horror", "romance"],
)
