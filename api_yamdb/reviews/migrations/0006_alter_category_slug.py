# Generated by Django 3.2 on 2023-08-10 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_alter_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.CharField(max_length=50),
        ),
    ]
