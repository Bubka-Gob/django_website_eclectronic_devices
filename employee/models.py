from django.db import models
from phone_field import PhoneField

class EmployeeModel(models.Model):
    full_name = models.CharField(max_length=200)
    age = models.IntegerField()
    phone = PhoneField()
    passport = models.CharField(max_length=40, null=True, blank=True)
    address = models.CharField(max_length=200)
    specialization = models.CharField(max_length=80)
    experience = models.IntegerField()
    date_of_employment = models.DateField()
    date_of_last_vacation = models.DateField()
    is_on_vacation = models.BooleanField()
    salary = models.IntegerField()


