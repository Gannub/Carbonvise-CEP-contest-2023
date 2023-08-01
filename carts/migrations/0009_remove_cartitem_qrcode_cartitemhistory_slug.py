# Generated by Django 4.2.2 on 2023-07-23 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0008_remove_cart_qrcode_cartitem_qrcode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='qrcode',
        ),
        migrations.AddField(
            model_name='cartitemhistory',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]