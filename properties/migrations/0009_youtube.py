# Generated by Django 3.2.6 on 2021-11-13 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0008_auto_20211108_1006'),
    ]

    operations = [
        migrations.CreateModel(
            name='Youtube',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('youtube_link', models.URLField(verbose_name='Youtube Link')),
            ],
        ),
    ]
