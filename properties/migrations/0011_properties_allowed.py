# Generated by Django 3.2.6 on 2021-11-16 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0010_alter_bid_property_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='properties',
            name='allowed',
            field=models.BooleanField(default=False),
        ),
    ]
