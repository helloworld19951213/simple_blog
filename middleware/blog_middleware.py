import sys

from django.conf import settings
from django.http import JsonResponse
from django.views.debug import technical_500_response


class UserBasedExceptionMiddleware(object):
    def process_exception(self, request, exception):
        if request.user.is_superuser or request.META.get('REMOTE_ADDR') in settings.ALLOWED_HOSTS:
            return technical_500_response(request, *sys.exc_info())


class ResponseDataMiddleware(object):
    def process_response(self, request, response):
        if request.META['PATH_INFO'] == '/monitor/memory/':
            return JsonResponse(response)
        else:
            return response
