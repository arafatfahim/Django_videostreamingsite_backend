# Generated by Django 3.2 on 2021-04-28 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('playlists', '0005_playlist_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='playlists.playlist'),
        ),
    ]