from django.shortcuts import render
from django.views.generic import View
import requests
from bs4 import BeautifulSoup
import redis
import json
# from django_celery_beat.models import CrontabSchedule, PeriodicTask

# schedule, _ = CrontabSchedule.objects.get_or_create(minute='58', hour='23', day_of_week='*', day_of_month='*',
#                                                     month_of_year='*', timezone='Asia/Tehran'
#                                                     )
#
# PeriodicTask.objects.get_or_create(crontab=schedule, name='cpu-benchmark-task',
#                                    task='apps.benchmark.tasks.cpu_scrapy_tasks')
#
# PeriodicTask.objects.get_or_create(crontab=schedule, name='gpu-benchmark-task',
#                                    task='apps.benchmark.tasks.gpu_scrapy_tasks')
#
# PeriodicTask.objects.get_or_create(crontab=schedule, name='ram-benchmark-task',
#                                    task='apps.benchmark.tasks.ram_scrapy_tasks')
#
# PeriodicTask.objects.get_or_create(crontab=schedule, name='disk-benchmark-task',
#                                    task='apps.benchmark.tasks.disk_scrapy_tasks')
#
# PeriodicTask.objects.get_or_create(crontab=schedule, name='pc-benchmark-task',
#                                    task='apps.benchmark.tasks.pc_scrapy_tasks')


r = redis.Redis(host='localhost', port=6379, db=0)


class BenchmarkView(View):
    def get(self, request):
        return render(request, 'benchmark/benchmark.html')


class CpuBenchmarkView(View):
    def get(self, request, category, type):
        once = False

        if category in ['overclock', 'single-thread']:
            once = True

        if once:
            details = json.loads(r.get(f'benchmark:cpu:{category}:once'))

        else:
            details = json.loads(r.get(f'benchmark:cpu:{category}:{type}'))

        return render(request, 'benchmark/cpu-benchmark.html', {'details': details})


class CpuSingleBenchmarkView(View):
    def get(self, request, url):
        text = requests.get(f'https://www.cpubenchmark.net/cpu.php?{url}').text
        soup = BeautifulSoup(text, 'html.parser').find('div', class_='desc-body')
        details = []
        soup.find('div', class_='desc-body')
        for i in soup.find_all('p'):
            text = i.get_text().split(':')
            details.append({'name': text[0], 'amount': text[1:]})
        return render(request, 'benchmark/cpu-single-benchmark.html', {'details': details})


class GpuBenchmarkView(View):
    def get(self, request, category):
        details = json.loads(r.get(f'benchmark:gpu:{category}'))

        return render(request, 'benchmark/gpu-benchmark.html', {'details': details})


class GpuSingleBenchmarkView(View):
    def get(self, request, url):
        text = requests.get(f'https://www.videocardbenchmark.net/video_lookup.php?{url}').text
        soup = BeautifulSoup(text, 'html.parser').find('div', class_='desc-body')
        details = []
        soup.find('div', class_='desc-body')
        for i in soup.find_all('p'):
            text = i.get_text().split(':')
            details.append({'name': text[0], 'amount': text[1:]})
        return render(request, 'benchmark/gpu-single-benchmark.html', {'details': details})


class RamBenchmarkView(View):
    def get(self, request, category):
        details = json.loads(r.get(f'benchmark:ram:{category}'))
        return render(request, 'benchmark/ram-benchmark.html', {'details': details})


class RamSingleBenchmarkView(View):
    def get(self, request, url):
        text = requests.get(f'https://www.memorybenchmark.net/ram.php?{url}').text
        soup = BeautifulSoup(text, 'html.parser').find('div', class_='desc-body')
        details = []
        soup.find('div', class_='desc-body')
        for i in soup.find_all('p'):
            text = i.get_text().split(':')
            details.append({'name': text[0], 'amount': text[1:]})
        return render(request, 'benchmark/ram-single-benchmark.html', {'details': details})


class DiskBenchmarkView(View):
    def get(self, request, category):
        details = json.loads(r.get(f'benchmark:disk:{category}'))
        return render(request, 'benchmark/disk-benchmark.html', {'details': details})


class DiskSingleBenchmarkView(View):
    def get(self, request, url):
        text = requests.get(f'https://www.harddrivebenchmark.net/hdd_lookup.php?{url}').text
        soup = BeautifulSoup(text, 'html.parser').find('div', class_='desc-body')
        details = []
        soup.find('div', class_='desc-body')
        for i in soup.find_all('p'):
            text = i.get_text().split(':')
            details.append({'name': text[0], 'amount': text[1:]})
        return render(request, 'benchmark/disk-single-benchmark.html', {'details': details})


class PcBenchmarkView(View):
    def get(self, request, category):
        details = json.loads(r.get(f'benchmark:pc:{category}'))
        return render(request, 'benchmark/pc-benchmark.html', {'details': details})
