# Generated by Django 3.2.6 on 2021-11-13 07:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0009_youtube'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='property_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bidders', to='properties.properties'),
        ),
    ]
