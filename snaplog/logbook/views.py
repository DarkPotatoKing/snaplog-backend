from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render

from .models import Student


def index(request):
    context = {}
    return render(request, 'logbook/index.html', context)

def login(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    student_number = request.POST['student_number']
    r = '{} {} ({})'.format(first_name, last_name, student_number)
    return HttpResponse(r)
