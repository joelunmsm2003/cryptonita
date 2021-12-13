# Generated by Django 2.2.5 on 2021-12-05 03:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '2093_auto_20211205_0358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cryptocurrency',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 12, 5, 3, 59, 36, 479803), null=True),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 12, 5, 3, 59, 36, 483176), null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 12, 5, 3, 59, 36, 481480), null=True),
        ),
    ]
