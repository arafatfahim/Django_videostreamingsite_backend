# Generated by Django 3.2 on 2021-04-26 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0008_video_publish_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
