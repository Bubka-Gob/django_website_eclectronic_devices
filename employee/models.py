from django.db import models

class EmployeeModel(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.IntegerField()
    address = models.CharField(max_length=200)
    specialization = models.CharField(max_length=80)
    experience = models.IntegerField()
    date_of_employment = models.DateField()
    date_of_last_vacation = models.DateField()
    is_on_vacation = models.BooleanField()
    salary = models.IntegerField()
