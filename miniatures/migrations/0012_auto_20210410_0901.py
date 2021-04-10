# Generated by Django 3.1.7 on 2021-04-10 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miniatures', '0011_auto_20210409_1544'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='miniature',
            name='faction',
        ),
        migrations.AddField(
            model_name='miniature',
            name='has_factions',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
