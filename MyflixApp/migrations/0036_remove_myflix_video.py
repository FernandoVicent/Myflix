# Generated by Django 4.1.2 on 2022-10-16 02:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyflixApp', '0035_remove_myflix_video_url_myflix_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myflix',
            name='video',
        ),
    ]
