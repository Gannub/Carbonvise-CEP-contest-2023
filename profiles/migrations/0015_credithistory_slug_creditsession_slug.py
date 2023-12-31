# Generated by Django 4.2.2 on 2023-07-26 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0014_rename_is_neutral_creditsession_is_neutral'),
    ]

    operations = [
        migrations.AddField(
            model_name='credithistory',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='creditsession',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
