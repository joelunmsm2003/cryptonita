# Generated by Django 2.2.5 on 2020-12-09 01:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_auto_20201116_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 9, 1, 41, 2, 833979), null=True),
        ),
        migrations.AlterField(
            model_name='cercademi',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 9, 1, 41, 2, 840800), null=True),
        ),
        migrations.AlterField(
            model_name='favoritos',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 9, 1, 41, 2, 839568), null=True),
        ),
        migrations.AlterField(
            model_name='local',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 9, 1, 41, 2, 837299), null=True),
        ),
        migrations.AlterField(
            model_name='medidas',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 9, 1, 41, 2, 831736), null=True),
        ),
        migrations.AlterField(
            model_name='promocion',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 9, 1, 41, 2, 838547), null=True),
        ),
        migrations.AlterField(
            model_name='subcategoria',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 9, 1, 41, 2, 835421), null=True),
        ),
    ]
