# Generated by Django 4.1.2 on 2022-10-15 17:56

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('MyflixApp', '0031_alter_myflix_sinospse_alter_myflix_uuid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myflix',
            name='banner',
        ),
        migrations.AddField(
            model_name='myflix',
            name='classificacao',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='myflix',
            name='lancamento',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='myflix',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('d1d3ee97-f855-4f9d-999e-365ec800b629')),
        ),
    ]