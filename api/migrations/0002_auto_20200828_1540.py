# Generated by Django 2.2.5 on 2020-08-28 15:40

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='myuser',
            options={},
        ),
        migrations.AlterModelManagers(
            name='myuser',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='anexo',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='username',
        ),
        migrations.AddField(
            model_name='myuser',
            name='date_of_birth',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='myuser',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='medidas',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 8, 28, 15, 40, 40, 343855), null=True),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='email',
            field=models.EmailField(max_length=255, unique=True, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
