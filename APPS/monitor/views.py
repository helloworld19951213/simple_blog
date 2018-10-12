import os
from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import render_to_response

from monitor.models import Memory, Network, Basic


def index(request):
    Datetime = []
    mem_total = 0
    for i in Memory.objects.all():
        Datetime.append(datetime.strftime(i.memory_time, "%Y-%m-%d %H:%M"))
        mem_total = i.memory_total
    return render_to_response('Memory_info.html', {'Datetime': Datetime, 'mem_total': mem_total})


def get_chart(request):
    part = os.popen('ls /').read().splitlines()
    part.remove('proc')
    cmdpart = 'du -s /' + ' /'.join(part)
    # cmdpart2 = "df | grep '/$' | awk '{print $4}'"
    part_used = os.popen(cmdpart).read().splitlines()
    used = []
    for i in part_used:
        if i.split('\t')[0] != '0':
            used.append(i)

    used_dict = {'data': [], 'categories': []}
    for i in used:
        list = {'value': int(i.split('\t')[0]), 'name': i.split('\t')[1]}

        used_dict['categories'].append(i.split('\t')[1])
        used_dict['data'].append(list)
    return JsonResponse(used_dict)


def get_mem(request):
    memory_list = {'Used': [], 'Free': [], 'Share': [],
                   'Buff_Cache': [], 'Available': [], 'Datetime': []}
    for i in Memory.objects.all():
        memory_list['Used'].append(i.memory_used)
        memory_list['Free'].append(i.memory_free)
        memory_list['Share'].append(i.memory_share)
        memory_list['Buff_Cache'].append(i.memory_bu_ca)
        memory_list['Available'].append(i.memory_available)
        memory_list['Datetime'].append(
            datetime.strftime(i.memory_time, "%Y-%m-%d %H:%M"))
    return JsonResponse(memory_list)


def get_mem_time(request):
    memory_list = {'Used': [], 'Free': [], 'Share': [],
                   'Buff_Cache': [], 'Available': [], 'Datetime': []}
    # if request.is_ajax:
    starttime = request.GET.get('starttime').encode('utf-8')
    endtime = request.GET.get('endtime').encode('utf-8')

    startdate = datetime.strptime(starttime.split(' ')[0], "%Y-%m-%d")
    enddate = datetime.strptime(endtime.split(' ')[0], "%Y-%m-%d")
    # 过滤在某时间段的数据
    for i in Memory.objects.filter(memory_time__range=(startdate, enddate)):
        memory_list['Used'].append(i.memory_used)
        memory_list['Free'].append(i.memory_free)
        memory_list['Share'].append(i.memory_share)
        memory_list['Buff_Cache'].append(i.memory_bu_ca)
        memory_list['Available'].append(i.memory_available)
        memory_list['Datetime'].append(
            datetime.strftime(i.memory_time, "%Y-%m-%d %H:%M"))
        memory_list['mem_total'] = i.memory_total
    return JsonResponse(memory_list)
