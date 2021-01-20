# Generated by Django 2.2.5 on 2021-01-14 17:49

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0032_auto_20210114_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 14, 17, 49, 43, 543894), null=True),
        ),
        migrations.AlterField(
            model_name='cercademi',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 14, 17, 49, 43, 546151), null=True),
        ),
        migrations.AlterField(
            model_name='criptomonedas',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 14, 17, 49, 43, 540910), null=True),
        ),
        migrations.AlterField(
            model_name='favoritos',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 14, 17, 49, 43, 545644), null=True),
        ),
        migrations.AlterField(
            model_name='inversion',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 14, 17, 49, 43, 541426), null=True),
        ),
        migrations.AlterField(
            model_name='local',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 14, 17, 49, 43, 544749), null=True),
        ),
        migrations.AlterField(
            model_name='medidas',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 14, 17, 49, 43, 543458), null=True),
        ),
        migrations.AlterField(
            model_name='promocion',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 14, 17, 49, 43, 545241), null=True),
        ),
        migrations.AlterField(
            model_name='subcategoria',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 1, 14, 17, 49, 43, 544318), null=True),
        ),
        migrations.CreateModel(
            name='HistorialUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ganancia', models.FloatField(blank=True, max_length=100, null=True)),
                ('price', models.FloatField(blank=True, max_length=100, null=True)),
                ('fecha', models.DateTimeField(blank=True, null=True)),
                ('criptomoneda', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Criptomonedas')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'HistorialUser',
            },
        ),
    ]
