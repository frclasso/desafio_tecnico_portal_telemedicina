# Generated by Django 3.1.4 on 2020-12-16 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20201216_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='palestrante',
            name='nome',
            field=models.CharField(max_length=255),
        ),
    ]
