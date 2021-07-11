# Generated by Django 3.2.4 on 2021-07-10 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_auto_20210710_1145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_slug',
        ),
        migrations.AlterField(
            model_name='comments',
            name='comment_slug',
            field=models.SlugField(default=1, max_length=3000),
        ),
        migrations.AlterField(
            model_name='comments',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Comments', to='products.product', unique=True),
        ),
    ]