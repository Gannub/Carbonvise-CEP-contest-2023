# Generated by Django 4.2.2 on 2023-06-25 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_profile_image'),
        ('carts', '0002_alter_cart_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='customer',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='profiles.profile'),
        ),
    ]
