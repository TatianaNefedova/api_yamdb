# Generated by Django 3.2 on 2023-08-08 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('slug', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('slug', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='titles',
            name='genre',
        ),
        migrations.AlterField(
            model_name='titles',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category', to='reviews.category'),
        ),
        migrations.AddField(
            model_name='titles',
            name='genre',
            field=models.ManyToManyField(blank=True, null=True, related_name='genre', to='reviews.Genre'),
        ),
    ]