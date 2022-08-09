# Generated by Django 4.0.3 on 2022-08-02 15:04

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_userprofile_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.CharField(max_length=200, null=True, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='city',
            field=models.CharField(max_length=20, null=True, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='country',
            field=django_countries.fields.CountryField(max_length=2, null=True, verbose_name='Country'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email Address'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone1',
            field=models.CharField(max_length=20, null=True, verbose_name='Mobile number'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone2',
            field=models.CharField(max_length=20, null=True, verbose_name='Secondary phone number'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='zip_code',
            field=models.CharField(max_length=10, null=True, verbose_name='Postal code'),
        ),
    ]
