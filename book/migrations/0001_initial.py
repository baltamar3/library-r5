# Generated by Django 3.2 on 2023-05-03 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='title')),
                ('subtitle', models.CharField(max_length=128, verbose_name='subtitle')),
                ('publication_date', models.DateTimeField(auto_now_add=True)),
                ('publisher', models.CharField(max_length=128, verbose_name='subtitle')),
                ('description', models.TextField(verbose_name='description')),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
                'db_table': 'book',
            },
        ),
    ]
