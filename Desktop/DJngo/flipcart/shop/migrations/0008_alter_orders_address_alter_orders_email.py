# Generated by Django 4.0.4 on 2022-07-09 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_orders_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='address',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='orders',
            name='email',
            field=models.CharField(max_length=500),
        ),
    ]
