# Generated by Django 4.0.3 on 2022-08-02 15:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0034_alter_book_author'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0003_remove_payment_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='payment_platform',
            field=models.CharField(choices=[('Paystack', 'Paystack'), ('Paypal', 'Paypal')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='shopcart',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='book_app.book'),
        ),
        migrations.AlterField(
            model_name='shopcart',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
