from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='user',
            name='username_not_me',
        ),
    ]
