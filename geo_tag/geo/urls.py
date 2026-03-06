from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_complaint, name='add_complaint'),
    path('success/<int:id>/', views.success, name='success'),
    path('map/', views.map_view, name='map'),
]