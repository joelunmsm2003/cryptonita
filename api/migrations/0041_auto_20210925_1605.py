# Generated by Django 2.2.5 on 2021-09-25 16:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0040_auto_20210909_2021'),
    ]

    operations = [
        migrations.AddField(
            model_name='criptomonedas',
            name='recomendacion',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 9, 25, 16, 5, 37, 784794), null=True),
        ),
        migrations.AlterField(
            model_name='cercademi',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 9, 25, 16, 5, 37, 787037), null=True),
        ),
        migrations.AlterField(
            model_name='criptomonedas',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 9, 25, 16, 5, 37, 779783), null=True),
        ),
        migrations.AlterField(
            model_name='favoritos',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 9, 25, 16, 5, 37, 786634), null=True),
        ),
        migrations.AlterField(
            model_name='inversion',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 9, 25, 16, 5, 37, 781320), null=True),
        ),
        migrations.AlterField(
            model_name='local',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 9, 25, 16, 5, 37, 785743), null=True),
        ),
        migrations.AlterField(
            model_name='medidas',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 9, 25, 16, 5, 37, 784297), null=True),
        ),
        migrations.AlterField(
            model_name='portofolio',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 9, 25, 16, 5, 37, 787503), null=True),
        ),
        migrations.AlterField(
            model_name='promocion',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 9, 25, 16, 5, 37, 786213), null=True),
        ),
        migrations.AlterField(
            model_name='subcategoria',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 9, 25, 16, 5, 37, 785297), null=True),
        ),
    ]
