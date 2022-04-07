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
    
@login_required
def settings(request, user_id):
    
    user = User.objects.get(pk = user_id)
    user_profile = UserProfile.objects.get(User = user.id)
    person = user_profile.Person
    
    initial_dict = {
        'LastName':person.LastName,
        'FirstName':person.FirstName,
        'Affiliation':person.Affiliation,
        'Address':person.Address,
        'Email':person.Email,
        'Phone':person.Phone,
    }
    
    password_form = PasswordForm(request.POST or None)
    person_settings_form = PersonSettingsForm(request.POST or None, initial=initial_dict, instance=person,)    
    
    context_dict = {
        'user':user,
        'user_profile':user_profile,
        'person':person,
        'password_form':password_form,
        'person_settings_form':person_settings_form,
    }  
    
    if password_form.is_valid():
        password = password_form.save(commit=False)
        auth = authenticate(username=user.username, password=password_form.cleaned_data['Password'])
        if auth:
            if password_form.cleaned_data['NewPassword'] == password_form.cleaned_data['NewPasswordConfirm']:
                user.set_password(password_form.cleaned_data['NewPassword'])
                user.save()
                logout(request)
                return render(request, 'user_functions/landing.html', {})
            else:
                return HttpResponse("Passwords do not match.")
        else:
            return HttpResponse("Wrong password.")
        return render(request, 'user_functions/settings.html', context_dict)
    
    elif person_settings_form.is_valid():
        settings = person_settings_form.save(commit=False)
        settings.save()
        return render(request, 'user_functions/settings.html', context_dict)
    
    else:
        return render(request, 'user_functions/settings.html', context_dict)