from django.db import models
from home.models import UserModel

class Order(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date_of_creation = models.DateTimeField(auto_now=False, auto_now_add=True)
    price = models.IntegerField(null=True)
    is_in_process = models.BooleanField(default=False)
    is_finished = models.BooleanField(default=False)
    client = models.ForeignKey(UserModel, on_delete=models.CASCADE)
