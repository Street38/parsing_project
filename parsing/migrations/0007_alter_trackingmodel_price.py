# Generated by Django 4.1 on 2022-09-01 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parsing', '0006_personalaccount_telegram_chat_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trackingmodel',
            name='price',
            field=models.IntegerField(),
        ),
    ]
