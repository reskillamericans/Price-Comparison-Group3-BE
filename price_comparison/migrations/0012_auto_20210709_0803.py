# Generated by Django 3.2.4 on 2021-07-09 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_remove_product_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='comment_slug',
            field=models.CharField(default=1, max_length=3000),
        ),
        migrations.AddField(
            model_name='product',
            name='product_slug',
            field=models.CharField(default=1, max_length=3000),
        ),
    ]