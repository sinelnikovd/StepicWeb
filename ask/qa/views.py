from django.shortcuts import render
from django.http import HttpResponse

def myviews(request, *args, **kwargs):
    return HttpResponse('OK')
