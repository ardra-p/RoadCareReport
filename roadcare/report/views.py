from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request,'home/home.html')

def admin_login(request):
    return render(request,'home/admin_login.html')