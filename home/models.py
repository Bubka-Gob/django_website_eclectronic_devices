from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from phone_field import PhoneField
from employee.models import EmployeeModel


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email: raise ValueError('Отсутсвует Email адрес')

        user=self.model(email = self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email=self.normalize_email(email), password=password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class UserModel(AbstractBaseUser): # ToDo Fix phone field
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    full_name = models.CharField(max_length=200, null=False, blank=False)
    phone = PhoneField(null=False, blank=False)
    #passport = models.CharField(max_length=40, null=True, blank=True)
    company = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    employee = models.ForeignKey(EmployeeModel, on_delete=models.DO_NOTHING, null=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'phone', 'city', 'address']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True