from django.shortcuts import render
from .forms import *
from .models import *
from reversion.models import *
from django.contrib import *
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import random
import string


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
        
        try:
            user = User.objects.get(username = request.POST.get('email'))
        except:
            return HttpResponse("Please use the email you recieved your invitation from. If this is the case, A User with that email already exists")
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
 
@login_required   
def invite(request, password):
    invitation_form = InvitationForm(request.POST or None)
    
    context_dict = {
        'invitation_form':invitation_form,
    }
    
    if invitation_form.is_valid():
        if password == 'nopassword':
            tmp_password = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(15))
            context_dict['password'] = tmp_password
            email = invitation_form.cleaned_data['email']
            user = User.objects.create_user(email, email)
            user.set_password(tmp_password)
            user.save()            
        else:
            context_dict['password'] = 'nopassword'

        return render(request, 'user_functions/invitation.html', context_dict)
    else:
        context_dict['password'] = 'nopassword'
        return render(request, 'user_functions/invitation.html', context_dict)

@login_required    
def user_hub(request):
    # check if user profile is locked or unlocked to determine the specific function that
    # needs to be activated.
    # when the activate/deactivate button is pressed POST the change and reload the page
    #print(User.groups.all())
    user_profiles = UserProfile.objects.all()
    user_objects = User.objects.filter(groups__name__in = ['Contributor', 'Admin'])
    users = UserProfile.objects.filter(User__in = user_objects)
    revisions = Revision.objects.all()
    
    context_dict = {
        'users':users,
    }
    
    user_id = request.POST.get("submit")
    
    print(users)
    

    
    try:
        user = User.objects.get(username = user_id)
        if user.is_active == True:
            user.is_active = False
            user.save()
            print("User Deactivated")
        else:
            user.is_active = True
            user.save()
            print("User Activated")
            
    except:
        pass
    
    return render(request, 'user_functions/user_hub.html', context_dict)

@login_required
def user_changelog(request, user_id):
    
    user_changes = []
    
    change_user = UserProfile.objects.get(pk = user_id)
    user_revisions = Revision.objects.all().filter(user = change_user.User)
    print(user_revisions)
    for version in user_revisions:
        user_change = Version.objects.get(revision = version.id)
        
        change = [] 
        change_object = user_change.object_repr
        change_revision = Revision.objects.get(pk = user_change.revision.id)
        change_date = change_revision.date_created
        change.append(change_revision)
        change.append(change_date)
        
        '''change_data = user_change[0].serialized_data 
        print(version)
        change_elements = change_data.split("','")
        change_contents = change_elements[0].split('", "')
        
        change_location = change_contents[-1][12:-4]
        change_location = change_location.split(' - ')
        change_location = change_location[0]
        
        change_model = change_contents[0].split("','")
        change_id = change_contents[1].split("','")
        change_id = change_id[0].split(',')[0][5:]
        change_fields = change_contents[2].split("','")
        
        change_date = change_elements[0].split('"Date": "')
        try:
            change_date = change_date[1][:23]
        except:
            change_date = version.date_created
        
        change_field_contents = change_fields[0].split("\', \' ")
        print("_____________")
        print(change_location)        
        for element in change_field_contents:
            element = element.lstrip()
            #print(element)
            if element[:2] == '**':
                element = element[2:]
                change.append(change_location)
                change.append(element)
                change.append(change_date)'''
        
        
        if change != []:
            user_changes.append(change)
        
    #print(user_changes)
    #Get relavent data out of the JSON field and the date field, combine 
    #into a nested list, and pass the super list to the changelog page
    
    context_dict = {
        'user_id':change_user,
        'user_changes':user_changes,
    }
        
    return render(request, 'user_functions/user_changelog.html', context_dict)