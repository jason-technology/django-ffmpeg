# Generated by Django 4.0.1 on 2022-02-01 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ffmpeg', '0011_mediafile_video_height_mediafile_video_width'),
    ]

    operations = [
        migrations.AddField(
            model_name='mediafile',
            name='kbpm',
            field=models.IntegerField(default=0),
        ),
    ]