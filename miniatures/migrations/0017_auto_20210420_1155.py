# Generated by Django 3.1.7 on 2021-04-20 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('miniatures', '0016_auto_20210411_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='miniature',
            name='gamesys',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='miniatures.gamingsystem'),
        ),
    ]