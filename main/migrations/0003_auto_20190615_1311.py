# Generated by Django 2.0 on 2019-06-15 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190615_1158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='imdb_rating',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='released',
        ),
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
    ]
