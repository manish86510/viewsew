# Generated by Django 2.2.7 on 2019-11-16 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('admin_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=10)),
                ('is_active', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Admin_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dress_code', models.CharField(max_length=20, unique=True)),
                ('type_of_wear', models.CharField(max_length=40, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('adm_cat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminPanel.Admin')),
            ],
        ),
        migrations.CreateModel(
            name='Admin_Fabric_Type',
            fields=[
                ('fabric_id', models.AutoField(primary_key=True, serialize=False)),
                ('fabric_name', models.CharField(default='', max_length=50)),
                ('fabric_description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Vendor_Details',
            fields=[
                ('vendor_id', models.AutoField(primary_key=True, serialize=False)),
                ('dob', models.CharField(max_length=30)),
                ('mobile', models.BigIntegerField()),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('post_office', models.CharField(max_length=30, null=True)),
                ('boutique_address', models.CharField(max_length=255)),
                ('locality', models.CharField(max_length=150, null=True)),
                ('landmark', models.CharField(max_length=80, null=True)),
                ('pincode', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Vendor_fabrics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fabrics_type', models.ImageField(upload_to='images/')),
                ('fabrics_description', models.CharField(max_length=100)),
                ('fabrics_quantity', models.IntegerField()),
                ('fabrics_price', models.FloatField(default=0.0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('fabrics_category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='AdminPanel.Admin_Fabric_Type')),
                ('ven_fab_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminPanel.Vendor_Details')),
            ],
        ),
        migrations.CreateModel(
            name='Vendor_Design',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('design', models.ImageField(upload_to='images/')),
                ('design_description', models.TextField()),
                ('design_price', models.FloatField(default=0.0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('design_code', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='AdminPanel.Admin_Category')),
                ('ven_des_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminPanel.Vendor_Details')),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=10)),
                ('is_active', models.IntegerField(default=0)),
                ('edit_content', models.BooleanField(default=False)),
                ('offer', models.IntegerField(default=1)),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
                ('vendor_key', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='AdminPanel.Vendor_Details')),
            ],
        ),
        migrations.CreateModel(
            name='Admin_fabrics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fabrics_type', models.ImageField(upload_to='images/')),
                ('fabrics_description', models.CharField(max_length=100)),
                ('fabrics_price', models.FloatField(default=0.0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('adm_fab_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminPanel.Admin')),
                ('fabrics_category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='AdminPanel.Admin_Fabric_Type')),
            ],
        ),
        migrations.CreateModel(
            name='Admin_Design',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('design', models.ImageField(upload_to='images/')),
                ('design_description', models.TextField()),
                ('design_price', models.FloatField(default=0.0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('adm_des_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminPanel.Admin')),
                ('design_code', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='AdminPanel.Admin_Category')),
            ],
        ),
    ]
