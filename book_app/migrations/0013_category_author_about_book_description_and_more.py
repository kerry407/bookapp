# Generated by Django 4.0.3 on 2022-07-15 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0012_review_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.AddField(
            model_name='author',
            name='about',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='editors_note',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='length',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='read_time',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='release_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='book_app.category'),
        ),
    ]
