# Generated by Django 5.0.7 on 2024-12-05 03:42

import mdeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DailyEssentials', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyessentials',
            name='description',
            field=mdeditor.fields.MDTextField(blank=True),
        ),
    ]
