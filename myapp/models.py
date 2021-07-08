import django
from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models import Sum
from django.utils import timezone
from django.db import models


# Create your models here.
class Topic(models.Model):
     name = models.CharField(max_length=200)
     length = models.IntegerField(blank=False, default=12)

     def __str__(self):
          return self.name


class Course(models.Model):
     title = models.CharField(max_length=200)
     topic = models.ForeignKey(Topic, related_name='courses',
on_delete=models.CASCADE)
     price = models.DecimalField(max_digits=10, decimal_places=2)
     for_everyone = models.BooleanField(default=True)
     description = models.TextField(blank=True)
     def __str__(self):
          return self.title

class Student(User):
     LVL_CHOICES = [
     ('HS', 'High School'),
     ('UG', 'Undergraduate'),
     ('PG', 'Postgraduate'),
     ('ND', 'No Degree'),
     ]
     level = models.CharField(choices=LVL_CHOICES, max_length=2, default='HS')
     address = models.CharField(max_length=300, blank=True)
     province=models.CharField(max_length=2, default="ON")
     registered_courses = models.ManyToManyField(Course, blank=True)
     interested_in = models.ManyToManyField(Topic)

     def __str__(self):
          return self.username

class Order(models.Model):
     choices = [
          (0, 'Cancelled'),
          (1, 'Confirmed'),
          (2, 'On Hold'),
     ]
     courses = models.ManyToManyField(Course, blank=True)
     student = models.ForeignKey(Student, related_name='courses', on_delete=models.CASCADE)
     order_status =  models.IntegerField(choices=choices, default=1)
     order_date = models.DateField(default=django.utils.timezone.now)
     def __str__(self):
          return self.student.username

     def total_cost(self):
          return self.courses.objects.aggregate(total_cost=Sum('price'))