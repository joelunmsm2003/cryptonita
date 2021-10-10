# Generated by Django 2.2.5 on 2021-10-10 19:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0053_auto_20211010_1856'),
    ]

    operations = [
        migrations.RenameField(
            model_name='criptomonedas',
            old_name='simbolo',
            new_name='symbol',
        ),
        migrations.AlterField(
            model_name='criptomonedas',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 10, 19, 0, 2, 92065), null=True),
        ),
        migrations.AlterField(
            model_name='inversion',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 10, 19, 0, 2, 93331), null=True),
        ),
        migrations.AlterField(
            model_name='portofolio',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 10, 19, 0, 2, 94808), null=True),
        ),
    ]
