from django.shortcuts import render
from .forms import *
from .models import *
from django.contrib import *
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
def landing(request):
    return render(request, 'user_functions/landing.html', {})

@login_required
def hub(request):
    return render(request, 'user_functions/hub.html', {})

@login_required
def logout_view(request):
    logout(request)
    return render(request, 'user_functions/landing.html', {})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user:
            if user.username == user.email:
                return HttpResponseRedirect(reverse('user_functions:register'))
            else:
                login(request, user)
                return HttpResponseRedirect(reverse('user_functions:hub'))
        else:
            return HttpResponse("Invalid Login")
    else:
        return render(request, 'user_functions/login.html', {})
    
def register(request):
    
    user_form = CreateUserForm(request.POST or None)
    people_form = CreatePersonForm(request.POST or None)
    
    if user_form.is_valid() and people_form.is_valid():
        
        print(user_form.cleaned_data)
        
        try:
            user = User.objects.get(username = request.POST.get('email'))
        except:
            return HttpResponse("A User with that email already exists")
        user_content = user_form.save(commit=False)
        user.username = user_content.username
        
        if user_form.cleaned_data['password'] == user_form.cleaned_data['passwordConfirm']:
            user.set_password(user_content.password)
        else:
            return HttpResponse("Passwords do not match.")
        user.date = datetime.now()
        
        person = people_form.save(commit=False)        
        
        user.person = person
        person.email = user.email
        
        user_profile = UserProfile(User=user, Level="Authorized", Status="Unlocked", Person=person)     
        
        person.save()
        user.save()
        user_profile.save()
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('user_functions:hub'))
        else:
            return HttpResponse("Login after registration failed.")
    else:
        return render(request, 'user_functions/register.html', {'user_form':user_form, 'people_form':people_form})    