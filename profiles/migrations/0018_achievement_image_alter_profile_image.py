# Generated by Django 4.2.2 on 2023-07-29 08:18

from django.db import migrations, models
import profiles.models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0017_achievement_alter_creditsession_session_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='achievement',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=profiles.models.upload_path),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=profiles.models.upload_path),
        ),
    ]