from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    student_number = models.PositiveIntegerField(default=0)
