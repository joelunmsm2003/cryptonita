# Generated by Django 2.2.5 on 2021-11-21 17:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0067_auto_20211121_1637'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='email',
            options={'ordering': ['email']},
        ),
        migrations.RenameField(
            model_name='email',
            old_name='name',
            new_name='email',
        ),
        migrations.AlterField(
            model_name='cryptocurrency',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 11, 21, 17, 7, 56, 514001), null=True),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 11, 21, 17, 7, 56, 518583), null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 11, 21, 17, 7, 56, 515567), null=True),
        ),
    ]
