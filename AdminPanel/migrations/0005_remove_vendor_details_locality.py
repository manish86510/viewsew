# Generated by Django 2.2.7 on 2019-11-21 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AdminPanel', '0004_vendor_details_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor_details',
            name='locality',
        ),
    ]
