from django.db import models
from home.models import UserModel
from employee.models import EmployeeModel


class Device(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    start_price = models.IntegerField(null=True)
    is_street = models.BooleanField(default=False)
    is_room = models.BooleanField(default=False)
    max_temp = models.IntegerField()
    min_temp = models.IntegerField()
    is_220 = models.BooleanField(default=True)
    requirements = models.TextField()
    is_private = models.BooleanField(default=False)
    is_example = models.BooleanField(default=False)
    image = models.ImageField(upload_to='orders/images/', null=True)


class Order(models.Model):
    date_of_creation = models.DateTimeField(auto_now=False, auto_now_add=True)
    price = models.IntegerField(null=True)
    address = models.CharField(max_length=200)
    is_in_process = models.BooleanField(default=False)
    is_finished = models.BooleanField(default=False)
    spec_document = models.FileField(upload_to='orders/specs/', null=True)
    review = models.TextField(null=True)
    client = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.DO_NOTHING)


class EmployeeOrder(models.Model):
    employee = models.ForeignKey(EmployeeModel, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    is_operator = models.BooleanField(default=False)


class Contract(models.Model):
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    document = models.FileField(upload_to='orders/contract/', null=True)
