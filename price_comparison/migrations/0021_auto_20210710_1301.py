# Generated by Django 3.2.4 on 2021-07-10 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_auto_20210710_1154'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='slug',
            field=models.SlugField(default=1, unique=True),
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=1, unique=True),
        ),
    ]
