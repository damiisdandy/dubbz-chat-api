# Generated by Django 4.1.5 on 2023-01-20 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("message", "0002_apikey"),
    ]

    operations = [
        migrations.DeleteModel(name="APiKey",),
    ]
