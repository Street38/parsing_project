# Generated by Django 4.1 on 2022-09-03 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parsing', '0007_alter_trackingmodel_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personalaccount',
            name='name',
        ),
    ]