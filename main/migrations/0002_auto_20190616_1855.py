# Generated by Django 2.0 on 2019-06-16 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='photo',
            field=models.ImageField(blank=True, default='blank.jpg', null=True, upload_to=''),
        ),
    ]
