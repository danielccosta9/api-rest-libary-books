# Generated by Django 4.0.5 on 2022-06-28 23:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_books_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='image',
        ),
    ]