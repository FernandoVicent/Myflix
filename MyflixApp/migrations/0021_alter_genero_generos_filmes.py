# Generated by Django 4.1.1 on 2022-09-26 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyflixApp', '0020_genero_remove_myflix_generos_filmes_myflix_gener'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genero',
            name='generos_filmes',
            field=models.CharField(max_length=10, null=True),
        ),
    ]