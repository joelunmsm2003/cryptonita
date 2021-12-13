# Generated by Django 2.2.5 on 2021-12-08 08:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '8036_auto_20211208_0845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cryptocurrency',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 12, 8, 8, 45, 49, 691755), null=True),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 12, 8, 8, 45, 49, 695802), null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 12, 8, 8, 45, 49, 693351), null=True),
        ),
    ]
