# Generated by Django 4.1 on 2022-08-10 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_alter_shopcart_order_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='order_code',
            field=models.CharField(editable=False, max_length=100),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_code',
            field=models.CharField(editable=False, max_length=100),
        ),
    ]
