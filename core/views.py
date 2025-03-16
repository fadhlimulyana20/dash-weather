from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from core.forms import RegisterForm

def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard")  # Redirect to weather dashboard
        else:
            messages.error(request, "Invalid credentials")
    return render(request, "auth/login.html")

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after registration
            return redirect('dashboard')  # Redirect to the protected dashboard
    else:
        form = RegisterForm()
    
    return render(request, 'auth/register.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect("login")  # Redirect to login page after logout
