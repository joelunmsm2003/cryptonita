# Generated by Django 2.2.5 on 2021-10-08 04:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0042_auto_20211008_0425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='criptomonedas',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 8, 4, 32, 40, 660021), null=True),
        ),
        migrations.AlterField(
            model_name='inversion',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 8, 4, 32, 40, 663789), null=True),
        ),
        migrations.AlterField(
            model_name='portofolio',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 8, 4, 32, 40, 666038), null=True),
        ),
    ]
