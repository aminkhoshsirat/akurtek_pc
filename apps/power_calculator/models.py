from django.db import models


class CpuBrandsModel(models.Model):
    title = models.CharField(max_length=1000)

    def __str__(self):
        return self.title


class GpuBrandsModel(models.Model):
    title = models.CharField(max_length=1000)

    def __str__(self):
        return self.title


class CpuModel(models.Model):
    brand = models.ForeignKey(CpuBrandsModel, on_delete=models.DO_NOTHING, related_name='brand_cpus')
    title = models.CharField(max_length=1000)
    power_usage = models.PositiveIntegerField()


class MainBoardModel(models.Model):
    form_factor = models.CharField(max_length=500)
    power = models.IntegerField()


class GpuModel(models.Model):
    brand = models.ForeignKey(GpuBrandsModel, on_delete=models.DO_NOTHING, related_name='brand_gpus')
    title = models.CharField(max_length=1000)
    power_usage = models.PositiveIntegerField()


class SSDModel(models.Model):
    type = models.CharField(max_length=500)
    power = models.IntegerField()


class HardModel(models.Model):
    type = models.CharField(max_length=500)
    power = models.IntegerField()


class MouseModel(models.Model):
    type = models.CharField(max_length=500)
    power = models.IntegerField()


class KeyBoardModel(models.Model):
    type = models.CharField(max_length=500)
    power = models.IntegerField()


class RamModel(models.Model):
    type = models.CharField(max_length=500)
    power = models.IntegerField()
    storage = models.IntegerField()


class DriveModel(models.Model):
    type = models.CharField(max_length=1000)
    power = models.IntegerField()


class FanModel(models.Model):
    size = models.CharField(max_length=500)
    power = models.IntegerField()


class LiquidFanModel(models.Model):
    type = models.CharField(max_length=500)
    power = models.IntegerField()


class PortModel(models.Model):
    type = models.CharField(max_length=500)
    power = models.IntegerField()


class OtherPartsModel(models.Model):
    type = models.CharField(max_length=500)
    power = models.IntegerField()
