# Generated by Django 4.2.2 on 2023-07-29 15:45

from django.db import migrations, models
import profiles.models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0022_alter_creditsession_achievements_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=profiles.models.upload_path),
        ),
    ]
