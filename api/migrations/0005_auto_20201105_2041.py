# Generated by Django 2.2.5 on 2020-11-05 20:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200901_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medidas',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 11, 5, 20, 41, 4, 763081), null=True),
        ),
    ]
