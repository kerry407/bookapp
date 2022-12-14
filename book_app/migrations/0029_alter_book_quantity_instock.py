# Generated by Django 4.0.3 on 2022-07-24 20:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0028_alter_book_minquantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='quantity_instock',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
