from django.db import models

class Employee(models.Model):
    fullname12 = models.CharField(max_length=500)
    emp_code = models.CharField(max_length=300)
    mobile = models.CharField(max_length=300)

class Example(models.Model):
    fullname123 = models.CharField(max_length=500)
    emp_code = models.CharField(max_length=300)


#commiit