# Generated by Django 2.2.2 on 2020-01-30 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0010_auto_20200130_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='total',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
