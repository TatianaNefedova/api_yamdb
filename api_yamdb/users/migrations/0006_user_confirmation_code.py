# Generated by Django 3.2 on 2023-08-11 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_merge_20230811_0321'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='confirmation_code',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]