# Generated by Django 5.0.6 on 2024-07-16 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_assembledcasemodel_case_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assembledcasemodel',
            name='optical_drive',
            field=models.ManyToManyField(blank=True, to='product.opticaldrivemodel'),
        ),
    ]
