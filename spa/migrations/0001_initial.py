# Generated by Django 3.2 on 2022-04-15 19:16

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('featured_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('category', models.CharField(max_length=15)),
                ('title', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField()),
                ('time', models.DateTimeField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.IntegerField()),
                ('client_name', models.CharField(max_length=50)),
                ('client_email', models.EmailField(max_length=254, unique=True)),
                ('client_phone', models.IntegerField()),
                ('treatment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_treatments', to='spa.treatment')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.DateTimeField(unique=True)),
                ('booking_time', models.DurationField()),
                ('booked_status', models.IntegerField(choices=[(0, 'Unconfirmed'), (1, 'Booked')], default=0)),
                ('booking_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_treatments', to='spa.client')),
            ],
        ),
    ]
