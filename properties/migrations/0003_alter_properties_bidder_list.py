# Generated by Django 3.2.6 on 2021-10-23 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0002_auto_20211023_0445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='properties',
            name='bidder_list',
            field=models.ManyToManyField(blank=True, related_name='bidder_list', to='properties.Bid'),
        ),
    ]
