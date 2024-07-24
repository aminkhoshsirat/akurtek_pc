# Generated by Django 5.0.6 on 2024-07-15 22:30

import django_jalali.db.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdvertisingBannerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('url', models.SlugField(allow_unicode=True, unique=True)),
                ('image', models.ImageField(upload_to='panel/banners')),
                ('order', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=1000)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='AmazingOfferModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expired_date', django_jalali.db.models.jDateTimeField()),
                ('order', models.PositiveIntegerField(unique=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='AsemblePanelModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_board_image', models.ImageField(upload_to='panel/asemble_images')),
                ('cpu_image', models.ImageField(upload_to='panel/asemble_images')),
                ('fan_cpu_image', models.ImageField(upload_to='panel/asemble_images')),
                ('ram_image', models.ImageField(upload_to='panel/asemble_images')),
                ('hard_image', models.ImageField(upload_to='panel/asemble_images')),
                ('ssd_image', models.ImageField(upload_to='panel/asemble_images')),
                ('gpu_image', models.ImageField(upload_to='panel/asemble_images')),
                ('optical_drive_image', models.ImageField(upload_to='panel/asemble_images')),
                ('power_image', models.ImageField(upload_to='panel/asemble_images')),
                ('case_image', models.ImageField(upload_to='panel/asemble_images')),
                ('keyboard_image', models.ImageField(upload_to='panel/asemble_images')),
                ('mouse_image', models.ImageField(upload_to='panel/asemble_images')),
                ('speaker_image', models.ImageField(upload_to='panel/asemble_images')),
                ('monitor_image', models.ImageField(upload_to='panel/asemble_images')),
            ],
        ),
        migrations.CreateModel(
            name='DailyWorksModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10000)),
                ('descriptions', models.TextField(blank=True, null=True)),
                ('date', django_jalali.db.models.jDateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='FinancialStatementModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_company', models.CharField(max_length=10000)),
                ('receiver_company', models.CharField(max_length=10000)),
                ('sender_address', models.TextField()),
                ('receiver_address', models.TextField()),
                ('sender_post_code', models.CharField(blank=True, max_length=10, null=True)),
                ('receiver_post_code', models.CharField(blank=True, max_length=10, null=True)),
                ('sender_state', models.CharField(blank=True, max_length=10000, null=True)),
                ('receiver_state', models.CharField(blank=True, max_length=10000, null=True)),
                ('sender_city', models.CharField(blank=True, max_length=10000, null=True)),
                ('receiver_city', models.CharField(blank=True, max_length=10000, null=True)),
                ('sender_phone', models.CharField(max_length=11)),
                ('receiver_phone', models.CharField(max_length=11)),
                ('date', models.DateTimeField()),
                ('title', models.CharField(max_length=10000)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FinancialStatementObjectsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('product_code', models.CharField(blank=True, max_length=10, null=True)),
                ('price', models.PositiveIntegerField()),
                ('off', models.PositiveIntegerField()),
                ('price_after_off', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='InstantOfferModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expired_date', django_jalali.db.models.jDateTimeField()),
                ('order', models.PositiveIntegerField(unique=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='SiteDetailModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10000)),
                ('logo', models.ImageField(upload_to='site/logo')),
                ('phone', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('empty_cart_image', models.ImageField(upload_to='site/detail')),
                ('footer_title', models.CharField(max_length=1000)),
                ('footer_text', models.TextField()),
                ('limit_of_address_can_add', models.IntegerField()),
                ('suggested_products_image', models.ImageField(blank=True, null=True, upload_to='site/detail')),
                ('amazing_products_image', models.ImageField(blank=True, null=True, upload_to='site/detail')),
                ('instagram', models.URLField(blank=True, null=True)),
                ('facebook', models.URLField(blank=True, null=True)),
                ('whatsapp', models.URLField(blank=True, null=True)),
                ('youtube', models.URLField(blank=True, null=True)),
                ('telegram', models.URLField(blank=True, null=True)),
                ('twitter', models.URLField(blank=True, null=True)),
                ('linkedin', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SuggestedProductsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(unique=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]