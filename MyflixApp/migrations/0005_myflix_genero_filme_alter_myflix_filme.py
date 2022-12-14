# Generated by Django 4.1.1 on 2022-09-22 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyflixApp', '0004_alter_myflix_filme'),
    ]

    operations = [
        migrations.AddField(
            model_name='myflix',
            name='genero_filme',
            field=models.CharField(choices=[('Terror', 'Terror'), ('Ação', 'Ação'), ('Suspense', 'Suspense'), ('Ficção', 'Ficção'), ('Policial', 'Policial')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='myflix',
            name='filme',
            field=models.FileField(upload_to='filme'),
        ),
    ]
