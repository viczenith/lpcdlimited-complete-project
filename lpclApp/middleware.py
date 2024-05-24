from django.conf import settings
from django.http import HttpResponseNotFound
from django.shortcuts import render

class Handle404Middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if response.status_code == 404:
            if settings.DEBUG:
                original_debug = settings.DEBUG
                settings.DEBUG = False

                response = render(request, '404.html')

                settings.DEBUG = original_debug

        return response
