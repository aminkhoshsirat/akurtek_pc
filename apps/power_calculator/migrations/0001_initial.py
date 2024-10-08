# Generated by Django 5.0.6 on 2024-07-15 22:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CpuBrandsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='DriveModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=1000)),
                ('power', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FanModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=500)),
                ('power', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='GpuBrandsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='HardModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=500)),
                ('power', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='KeyBoardModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=500)),
                ('power', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='LiquidFanModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=500)),
                ('power', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MainBoardModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form_factor', models.CharField(max_length=500)),
                ('power', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MouseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=500)),
                ('power', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OtherPartsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=500)),
                ('power', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PortModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=500)),
                ('power', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RamModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=500)),
                ('power', models.IntegerField()),
                ('storage', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SSDModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=500)),
                ('power', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CpuModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('power_usage', models.PositiveIntegerField()),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='brand_cpus', to='power_calculator.cpubrandsmodel')),
            ],
        ),
        migrations.CreateModel(
            name='GpuModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('power_usage', models.PositiveIntegerField()),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='brand_gpus', to='power_calculator.gpubrandsmodel')),
            ],
        ),
    ]
