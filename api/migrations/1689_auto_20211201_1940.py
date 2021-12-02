# Generated by Django 2.2.5 on 2021-12-01 19:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '1688_auto_20211201_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cryptocurrency',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 12, 1, 19, 40, 2, 811145), null=True),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 12, 1, 19, 40, 2, 814229), null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 12, 1, 19, 40, 2, 812604), null=True),
        ),
    ]
