# Generated by Django 3.2.4 on 2021-07-10 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0021_auto_20210710_1301'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['product_name']},
        ),
    ]
