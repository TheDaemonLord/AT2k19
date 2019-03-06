# Generated by Django 2.1.5 on 2019-03-05 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_price', '0003_auto_20190209_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='current_price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='company',
            name='day_high',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='company',
            name='day_low',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='company',
            name='opening_price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='company',
            name='percentage_change',
            field=models.FloatField(default=0),
        ),
    ]
