# Generated by Django 3.1.4 on 2020-12-16 23:10

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20201216_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='palestra',
            name='data',
            field=models.DateTimeField(verbose_name=datetime.datetime(2020, 12, 16, 23, 10, 54, 555686)),
        ),
        migrations.AlterField(
            model_name='palestra',
            name='nome',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='palestras', to='core.palestrante'),
        ),
    ]
