# Generated by Django 3.1.7 on 2021-04-08 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miniatures', '0008_auto_20210408_1250'),
    ]

    operations = [
        migrations.RenameField(
            model_name='miniature',
            old_name='category',
            new_name='manufacturer',
        ),
    ]
