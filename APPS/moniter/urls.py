from django.conf.urls import url
from moniter.views import index, get_chart, get_mem, get_mem_time

urlpatterns = [
    url(r'^chart', get_chart, name='get_chart'),
    url(r'^memory', get_mem),
    url(r'^memory_time', get_mem_time),
    url(r'^index', index)
]
