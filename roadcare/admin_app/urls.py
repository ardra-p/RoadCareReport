from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.admin_login,name='login'),
    path('dashboard/',views.admin_dashboard,name='admin_dashboard'),
]

