# Generated by Django 2.2.7 on 2019-11-17 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdminPanel', '0002_remove_vendor_fabrics_fabrics_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin_category',
            name='dress_code',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='admin_category',
            name='type_of_wear',
            field=models.CharField(default='', max_length=40),
        ),
    ]