# Generated by Django 2.2.5 on 2020-09-01 15:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200828_1540'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medidas',
            old_name='parametro',
            new_name='label',
        ),
        migrations.RenameField(
            model_name='medidas',
            old_name='valor',
            new_name='medida',
        ),
        migrations.AlterField(
            model_name='medidas',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 9, 1, 15, 21, 38, 86568), null=True),
        ),
    ]
