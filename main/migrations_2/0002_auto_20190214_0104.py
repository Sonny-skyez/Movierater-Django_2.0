# Generated by Django 2.0 on 2019-02-14 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrainfo',
            name='rodzaj',
            field=models.IntegerField(choices=[(0, 'Nieznany'), (1, 'Horror'), (3, 'Sci-Fi'), (4, 'Dramat'), (2, 'Komedia')], default=0),
        ),
    ]