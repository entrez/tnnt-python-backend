# Generated by Django 3.2.3 on 2021-08-05 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0012_rename_description_achievement_descr'),
    ]

    operations = [
        migrations.RenameField(
            model_name='achievement',
            old_name='descr',
            new_name='description',
        ),
    ]
