# Generated by Django 3.0.3 on 2020-09-25 08:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20200925_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 25, 8, 10, 44, 270327, tzinfo=utc)),
        ),
    ]
