# Generated by Django 3.0.3 on 2020-09-24 07:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200924_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 24, 7, 23, 51, 64915, tzinfo=utc)),
        ),
    ]
