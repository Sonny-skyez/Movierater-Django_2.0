# Generated by Django 2.0 on 2019-06-15 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20190615_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='photo',
            field=models.ImageField(blank=True, default='blank.jpg', null=True, upload_to='plakaty'),
        ),
    ]
