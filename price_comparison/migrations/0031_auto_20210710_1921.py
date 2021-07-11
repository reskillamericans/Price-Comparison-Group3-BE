# Generated by Django 3.2.4 on 2021-07-10 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0030_auto_20210710_1702'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='product',
        ),
        migrations.AddField(
            model_name='comments',
            name='product_id',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='products.product'),
        ),
    ]