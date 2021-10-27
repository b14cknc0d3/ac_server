# Generated by Django 3.2.6 on 2021-10-23 04:45

from django.db import migrations, models
import phonenumber_field.modelfields
import properties.models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Properties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Phone No.')),
                ('image', models.ImageField(upload_to=properties.models.get_file_path)),
                ('video_links', models.URLField(verbose_name='Video Link')),
                ('description', models.CharField(max_length=225)),
                ('owner_or_broker', models.CharField(choices=[('O', 'OWNER'), ('B', 'BROKER')], max_length=1)),
                ('category', models.CharField(choices=[('2kh', '2_KANAL_HOUSE'), ('1kh', '1_KANAL_HOUSE'), ('4mh', '14_MARLAR_HOUSE'), ('5mh', '5_MARLAR_HOUSE'), ('2kp', '2_KANAL_PLOT'), ('1kp', '1_KANAL_PLOT'), ('4kp', '4_KANAL_PLOT'), ('5mp', '5_MARLAR_PLOT'), ('5ep', '5_MARLA_EXTENSION_PLOT'), ('5kf', '5_KANAL_FARM')], max_length=3, verbose_name='Properties Type')),
                ('bidder_list', models.ManyToManyField(related_name='bidder_list', to='properties.Bid')),
            ],
        ),
        migrations.DeleteModel(
            name='NaiHouse',
        ),
    ]
