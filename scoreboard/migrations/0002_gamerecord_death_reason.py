# Generated by Django 3.2.3 on 2021-08-04 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamerecord',
            name='death_reason',
            field=models.CharField(default='killed by a fox', max_length=1024),
            preserve_default=False,
        ),
    ]
