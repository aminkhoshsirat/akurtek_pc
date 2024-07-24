# Generated by Django 5.0.6 on 2024-07-16 14:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_alter_assembledcasemodel_optical_drive'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assembledcasemodel',
            name='case',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.casemodel', verbose_name='کیس'),
        ),
        migrations.AlterField(
            model_name='assembledcasemodel',
            name='cpu',
            field=models.ManyToManyField(to='product.cpumodel', verbose_name='پردازنده'),
        ),
        migrations.AlterField(
            model_name='assembledcasemodel',
            name='fan_cpu',
            field=models.ManyToManyField(to='product.fancpumodel', verbose_name='فن پردازنده'),
        ),
        migrations.AlterField(
            model_name='assembledcasemodel',
            name='gpu',
            field=models.ManyToManyField(blank=True, to='product.gpumodel', verbose_name='کارت گرافیک'),
        ),
        migrations.AlterField(
            model_name='assembledcasemodel',
            name='hard',
            field=models.ManyToManyField(blank=True, to='product.hardmodel', verbose_name='هارد'),
        ),
        migrations.AlterField(
            model_name='assembledcasemodel',
            name='main_board',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.mainboardmodel', verbose_name='مادربرد'),
        ),
        migrations.AlterField(
            model_name='assembledcasemodel',
            name='optical_drive',
            field=models.ManyToManyField(blank=True, to='product.opticaldrivemodel', verbose_name='درایو نوری'),
        ),
        migrations.AlterField(
            model_name='assembledcasemodel',
            name='power',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.powermodel', verbose_name='پاور'),
        ),
        migrations.AlterField(
            model_name='assembledcasemodel',
            name='ram',
            field=models.ManyToManyField(to='product.rammodel', verbose_name='رم'),
        ),
        migrations.AlterField(
            model_name='assembledcasemodel',
            name='ssd',
            field=models.ManyToManyField(blank=True, to='product.ssdmodel', verbose_name=''),
        ),
    ]
