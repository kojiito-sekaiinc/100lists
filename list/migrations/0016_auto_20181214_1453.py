# Generated by Django 2.1.4 on 2018-12-14 05:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0015_auto_20181214_1021'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 14, 14, 53, 25, 601037)),
        ),
        migrations.AlterField(
            model_name='list',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 14, 14, 53, 25, 599650)),
        ),
    ]
