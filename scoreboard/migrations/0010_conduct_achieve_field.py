# Generated by Django 3.2.3 on 2021-08-05 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0009_auto_20210804_2231'),
    ]

    operations = [
        migrations.AddField(
            model_name='conduct',
            name='achieve_field',
            field=models.BooleanField(default=False),
        ),
    ]
