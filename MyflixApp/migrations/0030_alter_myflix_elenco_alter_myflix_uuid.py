# Generated by Django 4.1.2 on 2022-10-14 21:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('MyflixApp', '0029_alter_myflix_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myflix',
            name='elenco',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='myflix',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('41701f31-8bd4-4e4c-ae97-a8b7ac94d18f')),
        ),
    ]
