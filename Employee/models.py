from django.db import models


class Employee(models.Model):
    fullname12 = models.CharField(max_length=500)
    mobile = models.CharField(max_length=300)
    emp_code = models.CharField(max_length=300)


class Example(models.Model):
    emp_code = models.CharField(max_length=300)
    fullname123 = models.CharField(max_length=500)
