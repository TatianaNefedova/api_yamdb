# Generated by Django 3.2 on 2023-08-12 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0009_alter_genre_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(max_length=256, unique=True),
        ),
    ]