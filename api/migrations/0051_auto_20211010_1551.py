# Generated by Django 2.2.5 on 2021-10-10 15:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0050_auto_20211008_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='criptomonedas',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 10, 15, 51, 28, 235655), null=True),
        ),
        migrations.AlterField(
            model_name='inversion',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 10, 15, 51, 28, 236834), null=True),
        ),
        migrations.AlterField(
            model_name='portofolio',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 10, 15, 51, 28, 238292), null=True),
        ),
    ]
