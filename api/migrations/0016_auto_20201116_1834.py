# Generated by Django 2.2.5 on 2020-11-16 18:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_auto_20201116_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategoria',
            name='foto',
            field=models.FileField(blank=True, null=True, upload_to='static'),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 11, 16, 18, 34, 53, 297673), null=True),
        ),
        migrations.AlterField(
            model_name='cercademi',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 11, 16, 18, 34, 53, 299932), null=True),
        ),
        migrations.AlterField(
            model_name='favoritos',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 11, 16, 18, 34, 53, 299471), null=True),
        ),
        migrations.AlterField(
            model_name='local',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 11, 16, 18, 34, 53, 298559), null=True),
        ),
        migrations.AlterField(
            model_name='medidas',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 11, 16, 18, 34, 53, 297090), null=True),
        ),
        migrations.AlterField(
            model_name='promocion',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 11, 16, 18, 34, 53, 298991), null=True),
        ),
        migrations.AlterField(
            model_name='subcategoria',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 11, 16, 18, 34, 53, 298102), null=True),
        ),
    ]
