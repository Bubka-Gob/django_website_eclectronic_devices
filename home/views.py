from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .forms import RegistrationForm, LoginForm
from.models import UserModel

def home_view(request):
    return render(request, 'home/home.html')

def register_view(request):
    if request.method == 'GET':
        form = RegistrationForm()
    else:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            messages.success(request, f'Аккаунт создан для пользователя {email}')
            return redirect('login-page')
    return render(request, 'home/register.html', {'form': form})

def login_view(request):
    user = request.user
    if user.is_authenticated:
        return redirect('home-page')

    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                messages.success(request, 'Вход выполнен')
                return redirect('home-page')
    return render(request, 'home/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return render(request, 'home/logout.html')

def profile_view(request):
    return render(request, 'home/profile.html')

def redact_view(request):
    if request.method == 'GET':
        return render(request, 'home/redact.html')
    else:
        user_row = UserModel.objects.get(email=request.user.email)
        user_row.first_name = request.POST['first_name']
        user_row.last_name = request.POST['last_name']
        user_row.phone = request.POST['phone']
        user_row.city = request.POST['city']
        user_row.save()

        return redirect('profile-page')