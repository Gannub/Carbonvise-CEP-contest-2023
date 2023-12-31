# Generated by Django 4.2.2 on 2023-06-19 17:52

from django.db import migrations, models
import market.models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0003_market_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='market',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=market.models.upload_path),
        ),
        migrations.AlterField(
            model_name='market',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
