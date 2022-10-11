# Generated by Django 4.1.1 on 2022-09-26 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyflixApp', '0017_remove_myflix_genero_filme'),
    ]

    operations = [
        migrations.CreateModel(
            name='Filme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('file_video', models.FileField(upload_to='filme')),
            ],
        ),
        migrations.RemoveField(
            model_name='myflix',
            name='filme',
        ),
        migrations.AddField(
            model_name='myflix',
            name='filme',
            field=models.ManyToManyField(to='MyflixApp.filme'),
        ),
    ]