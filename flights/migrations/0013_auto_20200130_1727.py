# Generated by Django 2.2.2 on 2020-01-30 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0012_remove_booking_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='past_bookings',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='tier',
        ),
    ]
