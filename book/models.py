from django.db import models
from django.contrib.postgres.fields import ArrayField


class Book(models.Model):
    title = models.CharField("title", max_length=350)
    subtitle = models.CharField("subtitle", max_length=350)
    authors = ArrayField(models.CharField(max_length=350), verbose_name="authors")
    categories = ArrayField(models.CharField(max_length=350), verbose_name="categories")
    publication_date = models.CharField(max_length=350)
    publisher = models.CharField("publisher", max_length=350)
    description = models.TextField(verbose_name="description")
    image = models.ImageField(upload_to="books", blank=True, null=True)

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
        db_table = "book"

    def __str__(self):
        return self.title
