from django.shortcuts import render
from .forms import SignupForm, EmailAuthenticationForm
from django import forms
from django.contrib.auth import authenticate, login
# Create your views here.


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SignupForm()
    return render(request, 'users/signup.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        form = EmailAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'files/dashboard.html')
            
    else:          
        form = EmailAuthenticationForm()
    return render(request, 'users/login.html', {'form': form})
            