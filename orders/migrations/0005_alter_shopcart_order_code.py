# Generated by Django 4.1 on 2022-08-10 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_payment_payment_platform_alter_shopcart_book_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopcart',
            name='order_code',
            field=models.CharField(max_length=100),
        ),
    ]