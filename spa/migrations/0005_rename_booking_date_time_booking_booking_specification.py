# Generated by Django 3.2 on 2022-04-16 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spa', '0004_auto_20220416_1820'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='booking_date_time',
            new_name='booking_specification',
        ),
    ]
