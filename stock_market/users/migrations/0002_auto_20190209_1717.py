# Generated by Django 2.1.5 on 2019-02-09 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='stock_possesed_1',
            field=models.IntegerField(default=0),
        ),
    ]
