from django.shortcuts import render
from django.views.generic import View
from .models import *


class PowerView(View):
    def get(self, request):
        cpu_brand = self.request.GET.get('cpu_brand')
        gpu_brand = self.request.GET.get('gpu_brand')

        cpu_brands = CpuBrandsModel.objects.all()
        gpu_brands = GpuBrandsModel.objects.all()
        main_boards = MainBoardModel.objects.all()

        rams = RamModel.objects.all()

        context = {
            'cpu_brands': cpu_brands,
            'gpu_brands': gpu_brands,
            'main_boards': main_boards,

            'rams': rams,
        }

        if cpu_brand:
            cpus = CpuModel.objects.filter(brand=cpu_brand)
            context['cpus'] = cpus

        if gpu_brand:
            gpus = GpuModel.objects.filter(brand=gpu_brand)
            context['gpus'] = gpus

        return render(request, 'power/power-caculator.html', context)