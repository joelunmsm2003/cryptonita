# Generated by Django 2.2.5 on 2021-12-02 04:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '1929_merge_20211202_0450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cryptocurrency',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 12, 2, 4, 50, 51, 144916), null=True),
        ),
        migrations.AlterField(
            model_name='generic',
            name='column',
            field=models.CharField(choices=[('id', 'id'), ('price', 'price'), ('symbol', 'symbol'), ('icono', 'icono'), ('sigla', 'sigla'), ('name', 'name'), ('trend', 'trend'), ('recommendation', 'recommendation'), ('activ', 'activ'), ('date', 'date'), ('user', 'user'), ('market_cap', 'market_cap'), ('fully_diluted_market_cap', 'fully_diluted_market_cap'), ('volume_24h', 'volume_24h'), ('volume_24h_market_cap', 'volume_24h_market_cap'), ('circulating_supply', 'circulating_supply'), ('max_supply', 'max_supply'), ('total_supply', 'total_supply')], max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 12, 2, 4, 50, 51, 148461), null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 12, 2, 4, 50, 51, 146777), null=True),
        ),
    ]
