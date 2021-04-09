# Generated by Django 3.1.7 on 2021-04-09 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('miniatures', '0010_auto_20210409_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='miniature',
            name='gaming_system',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='miniatures.gamingsystem'),
        ),
        migrations.AlterField(
            model_name='miniature',
            name='manufacturer',
            field=models.CharField(default='Manufacturer', max_length=254),
            preserve_default=False,
        ),
    ]