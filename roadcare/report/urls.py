from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name='home'),
    path('login',views.admin_login,name='login'),

]
