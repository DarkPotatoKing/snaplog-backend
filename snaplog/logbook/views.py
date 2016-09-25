from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render

from .models import Student


def index(request):
    context = {}
    return render(request, 'logbook/index.html', context)

def login(request):
    return HttpResponse('Login response')
