# Generated by Django 4.0.1 on 2022-02-01 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ffmpeg', '0010_alter_mediafile_fingerprint'),
    ]

    operations = [
        migrations.AddField(
            model_name='mediafile',
            name='video_height',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mediafile',
            name='video_width',
            field=models.IntegerField(default=0),
        ),
    ]
