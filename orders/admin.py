from django.contrib import admin
from .models import Order, Device, EmployeeOrder

admin.site.register(Order)
admin.site.register(Device)
admin.site.register(EmployeeOrder)