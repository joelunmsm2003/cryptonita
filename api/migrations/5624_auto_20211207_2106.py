# Generated by Django 2.2.5 on 2021-12-07 21:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '5623_auto_20211207_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cryptocurrency',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 12, 7, 21, 6, 32, 233767), null=True),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 12, 7, 21, 6, 32, 236886), null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 12, 7, 21, 6, 32, 235257), null=True),
        ),
    ]
