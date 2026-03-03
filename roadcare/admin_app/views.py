from django.shortcuts import render

# Create your views here.
def admin_login(request):
    return render(request,'admin_page/admin_login.html')


def admin_dashboard(request):
    return render(request,'admin_page/admin_dashboard.html')
