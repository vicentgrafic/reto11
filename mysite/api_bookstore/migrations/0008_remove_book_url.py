# Generated by Django 3.2.5 on 2021-07-27 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_bookstore', '0007_book_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='url',
        ),
    ]
