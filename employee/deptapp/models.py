from django.db import models
from django.shortcuts import reverse
# Create your models here.

class Department(models.Model):
    deptname = models.CharField(max_length=50, unique=True, blank=False)
    dept_logo = models.FileField(upload_to='documents/', blank=True)
    def __str__(self):
        return self.deptname

    def get_absolute_url(self):
        return reverse('deptapp:detail_dept', kwargs={'pk': self.pk})

class Employee(models.Model):
    dept = models.ForeignKey(Department, on_delete = models.CASCADE)
    empname=models.CharField(max_length=50, blank=False)
    emplastname= models.CharField(max_length=50)
    empsal = models.IntegerField()

    def __str__(self):
        return self.empname

