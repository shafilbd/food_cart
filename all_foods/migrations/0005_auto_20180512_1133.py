# Generated by Django 2.0.3 on 2018-05-12 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('all_foods', '0004_auto_20180510_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='type',
            field=models.CharField(choices=[('Fast Food', 'Fast Food'), ('Dinner Foods', 'Dinner Foods'), ('Lunch Food', 'Lunch Food'), ('Rices Foods', 'Rices Foods'), ('soup', 'soup'), ('Fried Chicken', 'Fried Chicken'), ('Grilled', 'Grilled'), ('other', 'Other')], max_length=30, verbose_name='foods type :'),
        ),
    ]