# Generated by Django 4.1.2 on 2022-10-05 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyflixApp', '0022_remove_myflix_gener_myflix_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='myflix',
            name='publicada',
            field=models.BooleanField(default=False),
        ),
    ]