# Generated by Django 4.2.2 on 2023-07-30 08:48

from django.db import migrations, models
import profiles.models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0024_achievement_des1_achievement_des2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=profiles.models.upload_path),
        ),
    ]
