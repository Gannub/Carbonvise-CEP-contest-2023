# Generated by Django 4.2.2 on 2023-07-02 11:11

import dealer.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dealer', '0002_dealer_deal_province'),
    ]

    operations = [
        migrations.AddField(
            model_name='dealer',
            name='shop_icon',
            field=models.ImageField(blank=True, null=True, upload_to=dealer.models.upload_path),
        ),
        migrations.AlterField(
            model_name='dealer',
            name='verify',
            field=models.FileField(max_length=254, upload_to=dealer.models.verify_upload_path),
        ),
    ]
