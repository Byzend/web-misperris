# Generated by Django 2.0.2 on 2018-10-29 15:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mascota', '0003_mascota_raza'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascota',
            name='Estado',
            field=models.CharField(default=datetime.datetime(2018, 10, 29, 15, 38, 51, 424917, tzinfo=utc), max_length=50, verbose_name='Estado'),
            preserve_default=False,
        ),
    ]
