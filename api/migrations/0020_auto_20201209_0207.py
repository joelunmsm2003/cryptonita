# Generated by Django 2.2.5 on 2020-12-09 02:07

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_auto_20201209_0156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 9, 2, 7, 47, 469138), null=True),
        ),
        migrations.AlterField(
            model_name='cercademi',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 9, 2, 7, 47, 471388), null=True),
        ),
        migrations.AlterField(
            model_name='criptomonedas',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 9, 2, 7, 47, 466350), null=True),
        ),
        migrations.AlterField(
            model_name='favoritos',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 9, 2, 7, 47, 470994), null=True),
        ),
        migrations.AlterField(
            model_name='local',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 9, 2, 7, 47, 470047), null=True),
        ),
        migrations.AlterField(
            model_name='medidas',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 9, 2, 7, 47, 468657), null=True),
        ),
        migrations.AlterField(
            model_name='promocion',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 9, 2, 7, 47, 470550), null=True),
        ),
        migrations.AlterField(
            model_name='subcategoria',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 9, 2, 7, 47, 469574), null=True),
        ),
        migrations.CreateModel(
            name='Inversion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_comprada', models.FloatField(max_length=100, null=True)),
                ('precio_usd', models.FloatField(max_length=100, null=True)),
                ('comprada_usd', models.FloatField(max_length=100, null=True)),
                ('fecha', models.DateTimeField(blank=True, default=datetime.datetime(2020, 12, 9, 2, 7, 47, 467667), null=True)),
                ('criptomoneda', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Criptomonedas')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Criptomonedas',
            },
        ),
    ]
