# Generated by Django 3.2 on 2022-04-16 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spa', '0002_auto_20220416_1807'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='booking_id',
        ),
    ]
