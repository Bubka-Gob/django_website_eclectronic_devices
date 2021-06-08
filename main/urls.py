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
from django.conf import settings
from django.conf.urls.static import static
from home.views import home_view, register_view, login_view, logout_view, profile_view, redact_view
from orders.views import (device_creation_view,
                          order_list_view,
                          examples_view,
                          order_detail_view,
                          order_creation_view,
                          device_from_example_view)
from employee.views import (orders_panel_view,
                            employee_order_view,
                            order_accept_view,
                            order_finish_view,
                            device_redact_view,
                            employee_managing_view,
                            employee_adding_view,
                            employee_removing_view)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home-page'),
    path('register/', register_view, name='register-page'),
    path('login/', login_view, name='login-page'),
    path('logout/', logout_view, name='logout-page'),
    path('profile/', profile_view, name='profile-page'),
    path('profile/create_order/<int:device_id>/', order_creation_view, name='order_creation-page'),
    path('profile/create/', device_creation_view, name='creation-page'),
    path('profile/order_list/', order_list_view, name='order_list-page'),
    path('profile/order_list/<int:order_id>/', order_detail_view, name='order_detail-page'),
    path('profile/orders_panel/', orders_panel_view, name='orders_panel-page'),
    path('profile/employee_order/<int:order_id>/', employee_order_view, name='employee_order-page'),
    path('profile/employee_order/<int:order_id>/redact/', device_redact_view, name='device_redact-page'),
    path('profile/employee_order/<int:order_id>/accept/', order_accept_view, name='order_accept-page'),
    path('profile/employee_order/<int:order_id>/finish/', order_finish_view, name='order_finish-page'),
    path('profile/employee_order/<int:order_id>/manage_employees/', employee_managing_view, name='employee_managing-page'),
    path('profile/employee_order/<int:order_id>/add/<int:employee_id>', employee_adding_view, name='employee_adding-page'),
    path('profile/employee_order/<int:order_id>/remove/<int:employee_id>', employee_removing_view, name='employee_removing-page'),
    path('profile/redact/', redact_view, name='redact-page'),
    path('examples/', examples_view, name='examples-page'),
    path('examples/redact/<int:device_id>', device_from_example_view, name='device_from_example-page')
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
