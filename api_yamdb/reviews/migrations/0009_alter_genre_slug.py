# Generated by Django 3.2 on 2023-08-12 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0008_auto_20230811_0540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]