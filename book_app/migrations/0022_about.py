# Generated by Django 4.0.3 on 2022-07-17 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0021_alter_category_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_text', models.TextField(null=True)),
            ],
            options={
                'verbose_name_plural': 'About',
            },
        ),
    ]
