# Generated by Django 3.2 on 2022-04-16 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spa', '0003_remove_booking_booking_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='booking_date',
            new_name='booking_date_time',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='booking_time',
        ),
    ]