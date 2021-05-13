"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home.views import home_view, register_view, login_view, logout_view, profile_view, redact_view
from orders.views import order_creation_view, order_list_view, examples_view, order_detail_view
from employee.views import employee_panel_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home-page'),
    path('register/', register_view, name='register-page'),
    path('login/', login_view, name='login-page'),
    path('logout/', logout_view, name='logout-page'),
    path('profile/', profile_view, name='profile-page'),
    path('profile/create/', order_creation_view, name='creation-page'),
    path('profile/order_list/', order_list_view, name='order_list-page'),
    path('profile/order_list/<int:order_id>/', order_detail_view, name='order_detail-page'),
    path('profile/employee_panel/', employee_panel_view, name='employee_panel-page'),
    path('profile/redact/', redact_view, name='redact-page'),
    path('examples/', examples_view, name='examples-page')

]
