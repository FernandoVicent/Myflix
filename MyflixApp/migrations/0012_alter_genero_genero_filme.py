# Generated by Django 4.1.1 on 2022-09-23 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyflixApp', '0011_remove_myflix_genero_filme_myflix_genero_filme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genero',
            name='genero_filme',
            field=models.CharField(choices=[('Terror', 'Terror'), ('Ação', 'Ação'), ('Suspense', 'Suspense'), ('Ficcao', 'Ficcao'), ('Policial', 'Policial')], max_length=20, null=True),
        ),
    ]