from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from phone_field import PhoneFormField, PhoneWidget
from .models import UserModel

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Email адрес'}))
    full_name = forms.CharField(max_length=200, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Полное имя'}))
    phone = PhoneFormField(widget=PhoneWidget(
        attrs={'class': 'form-control', 'placeholder': 'Номер телефона'}))
    company = forms.CharField(required=False, max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Название компании'}))
    address = forms.CharField(required=False, max_length=200, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Адрес'}))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Подтверждение пароля'}))

    class Meta:
        model = UserModel
        fields = ('email', 'full_name', 'phone', 'company', 'address', 'password1', 'password2')


class ProfileForm(forms.ModelForm):
    full_name = forms.CharField(max_length=200, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    phone = PhoneFormField(widget=PhoneWidget(
        attrs={'class': 'form-control'}))
    company = forms.CharField(required=False, max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    address = forms.CharField(required=False, max_length=200, widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = UserModel
        fields = ('full_name', 'phone', 'company', 'address')


class LoginForm(forms.ModelForm):
    password = forms.CharField( widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'id': 'inputEmail'}))
    email = forms.CharField( widget=forms.EmailInput(
        attrs={'class': 'form-control', 'id': 'inputPassword'}))

    class Meta:
        model = UserModel
        fields = ('email', 'password')

    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        if not authenticate(email=email, password=password):
            raise forms.ValidationError('Неверный Email или пароль')