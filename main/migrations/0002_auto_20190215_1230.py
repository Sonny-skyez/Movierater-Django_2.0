# Generated by Django 2.0 on 2019-02-15 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrainfo',
            name='rodzaj',
            field=models.IntegerField(choices=[(0, 'Nieznany'), (3, 'Sci-Fi'), (2, 'Komedia'), (1, 'Horror'), (4, 'Dramat')], default=0),
        ),
    ]
