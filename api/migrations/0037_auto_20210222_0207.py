# Generated by Django 2.2.5 on 2021-02-22 02:07

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0036_auto_20210222_0203'),
    ]

    operations = [
        migrations.AddField(
            model_name='inversion',
            name='cuenta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Cuentas'),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 22, 2, 7, 42, 418831), null=True),
        ),
        migrations.AlterField(
            model_name='cercademi',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 22, 2, 7, 42, 420878), null=True),
        ),
        migrations.AlterField(
            model_name='criptomonedas',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 22, 2, 7, 42, 415456), null=True),
        ),
        migrations.AlterField(
            model_name='favoritos',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 22, 2, 7, 42, 420489), null=True),
        ),
        migrations.AlterField(
            model_name='inversion',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 22, 2, 7, 42, 416375), null=True),
        ),
        migrations.AlterField(
            model_name='local',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 22, 2, 7, 42, 419693), null=True),
        ),
        migrations.AlterField(
            model_name='medidas',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 22, 2, 7, 42, 418407), null=True),
        ),
        migrations.AlterField(
            model_name='promocion',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 22, 2, 7, 42, 420093), null=True),
        ),
        migrations.AlterField(
            model_name='subcategoria',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 22, 2, 7, 42, 419203), null=True),
        ),
    ]
