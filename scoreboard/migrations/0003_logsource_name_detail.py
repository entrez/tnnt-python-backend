# Generated by Django 3.1.6 on 2021-03-02 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0002_auto_20210302_2158'),
    ]

    operations = [
        migrations.AddField(
            model_name='logsource',
            name='name_detail',
            field=models.CharField(default='xlog source description', max_length=200),
        ),
    ]
