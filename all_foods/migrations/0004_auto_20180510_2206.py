# Generated by Django 2.0.3 on 2018-05-10 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('all_foods', '0003_auto_20180505_0001'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='offer_price',
            field=models.IntegerField(default=0, verbose_name='offer_name'),
        ),
        migrations.AddField(
            model_name='food',
            name='price',
            field=models.IntegerField(default=0, verbose_name='current_price'),
        ),
    ]
