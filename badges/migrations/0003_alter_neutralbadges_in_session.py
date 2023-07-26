# Generated by Django 4.2.2 on 2023-07-26 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0014_rename_is_neutral_creditsession_is_neutral'),
        ('badges', '0002_neutralbadges_is_obtained'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neutralbadges',
            name='in_session',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='badges', to='profiles.creditsession'),
        ),
    ]
