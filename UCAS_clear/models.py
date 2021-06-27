from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

# Create your models here.

class User(AbstractUser):
    pass

class University(models.Model):
    university_name = models.CharField(max_length=255, default=None)

    def __str__(self):
        return self.university_name

class Course(models.Model):
    university_id = models.IntegerField(default=None)
    university_name = models.CharField(max_length=255, default=None)
    course_name = models.CharField(max_length=255, default=None)
    ucas_points = models.IntegerField(default=None)
    course_spaces = models.IntegerField(default=None)
    filled_spaces = models.IntegerField(default=None)
    availability_status = models.CharField(max_length=255, default='Available')
    closing_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.course_name