__author__ = 'dc'
import json

from django.http import HttpResponse


def demo(request):
    ret = {1: "hello", 2: "demo"}
    return HttpResponse(json.dumps(ret))