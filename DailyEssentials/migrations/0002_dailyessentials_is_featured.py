# Generated by Django 5.0.7 on 2024-11-26 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DailyEssentials', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailyessentials',
            name='is_featured',
            field=models.BooleanField(default=False, verbose_name='Featured Item (精选商品)'),
        ),
    ]
