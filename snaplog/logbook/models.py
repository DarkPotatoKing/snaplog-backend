from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    student_number = models.PositiveIntegerField(default=0, unique=True)

    def __str__(self):
        return '{} {} ({})'.format(self.first_name, self.last_name, str(self.student_number))
