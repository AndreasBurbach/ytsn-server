# Generated by Django 3.2.9 on 2022-04-30 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='youtubevideostatement',
            name='vote',
            field=models.PositiveSmallIntegerField(choices=[(1, 'like'), (2, 'dislike')], default=1),
        ),
    ]
