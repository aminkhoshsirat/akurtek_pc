# Generated by Django 5.0.6 on 2024-07-15 22:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bucket', '0002_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='buketmodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_buckets', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bucketproductsmodel',
            name='bucket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_bucket_products', to='bucket.buketmodel'),
        ),
        migrations.AddField(
            model_name='walletmodel',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_wallet', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='wallettransactionmodel',
            name='wallet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wallet_transactions', to='bucket.walletmodel'),
        ),
    ]
