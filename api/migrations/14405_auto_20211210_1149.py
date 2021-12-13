# Generated by Django 2.2.5 on 2021-12-10 11:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '14404_auto_20211210_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cryptocurrency',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 12, 10, 11, 48, 44, 129277), null=True),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 12, 10, 11, 48, 44, 132311), null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 12, 10, 11, 48, 44, 130797), null=True),
        ),
    ]
