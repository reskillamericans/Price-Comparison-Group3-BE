# Generated by Django 3.2.4 on 2021-07-14 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_comments'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='uodated_at',
            new_name='updated_at',
        ),
    ]