from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404

from .models import Student

def compare(a, b):
    return a.strip().upper() == b.strip().upper()


def index(request):
    context = {}
    return render(request, 'logbook/index.html', context)

def login(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    student_number = request.POST['student_number']
    try:
        student = get_object_or_404(Student, student_number=student_number)

        if compare(first_name, student.first_name) and compare(last_name, student.last_name) and int(student_number) == student.student_number:
            return HttpResponse('Welcome {}.'.format(str(student)))
        else:
            raise StandardError
    except:
        return HttpResponse('Your credentials do not match any record in the database.')
