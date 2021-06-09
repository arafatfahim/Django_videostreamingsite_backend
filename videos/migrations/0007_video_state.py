# Generated by Django 3.2 on 2021-04-26 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0006_auto_20210426_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='state',
            field=models.CharField(choices=[('PU', 'Publish'), ('DR', 'Draft')], default='DR', max_length=2),
        ),
    ]
