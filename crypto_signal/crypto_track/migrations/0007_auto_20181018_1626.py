# Generated by Django 2.1.2 on 2018-10-18 14:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('crypto_track', '0006_auto_20181018_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='pytrends',
            name='btc_usd',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='pytrends',
            name='buy_bitcoin',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='cryptocandle',
            name='update_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 18, 14, 26, 39, 109620, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='cryptocandlehistory',
            name='update_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 18, 14, 26, 39, 110564, tzinfo=utc)),
        ),
    ]