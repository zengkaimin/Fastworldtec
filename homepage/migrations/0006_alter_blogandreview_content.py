# Generated by Django 5.0.7 on 2024-12-03 03:53

import mdeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_blogandreview_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogandreview',
            name='content',
            field=mdeditor.fields.MDTextField(blank=True),
        ),
    ]