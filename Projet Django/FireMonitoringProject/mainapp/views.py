from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

from .models import FireMonitoringData

def home(request):
    # Fetch some example fire monitoring data for demonstration
    monitoring_data = FireMonitoringData.objects.all()[:5]  # Get the latest 5 entries
    return render(request, 'home.html', {'project_name': 'Fire Monitoring', 'monitoring_data': monitoring_data})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})


# views.py
from django.shortcuts import render

def about_us_view(request):
    project_name = "Fire Monitoring"  # Replace with your actual project name
    return render(request, 'about_us.html', {'project_name': project_name})
