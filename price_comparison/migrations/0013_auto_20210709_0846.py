# Generated by Django 3.2.4 on 2021-07-09 12:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0012_auto_20210709_0803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='product',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='Comments'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='User', to=settings.AUTH_USER_MODEL),
        ),
    ]