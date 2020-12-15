# Generated by Django 3.1.4 on 2020-12-15 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_palestrante'),
    ]

    operations = [
        migrations.AlterField(
            model_name='palestrante',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Palestra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('descricao', models.CharField(blank=True, max_length=255, null=True)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('palestrante', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.palestrante')),
            ],
        ),
    ]