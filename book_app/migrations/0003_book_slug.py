# Generated by Django 4.0.3 on 2022-04-10 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0002_book_author_book_is_bestselling_alter_book_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
