# Generated by Django 4.1.1 on 2022-09-23 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyflixApp', '0013_alter_genero_genero_filme'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myflix',
            name='genero_filme',
        ),
    ]
