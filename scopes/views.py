from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *

# Create your views here.

@login_required
def hub(request):
    
    context_dict = {}
    
    all_species = SpeciesCommunity.objects.all()
    context_dict['SpeciesCommunity'] = all_species
    
    all_locations = Location.objects.all()
    context_dict['Location'] = all_locations
    
    all_measures = ConservationMeasure.objects.all()
    context_dict['ConservationMeasure'] = all_measures
    
    all_goals = Goal.objects.all()
    context_dict['Goal'] = all_goals
    
    return render(request, 'scopes/scope_hub.html', context_dict)

@login_required
def speCom(request, speCom_ID):
    
    if speCom_ID == "0":
        spe_com_form = SpeComForm(request.POST, request.FILES)
    
    else:
        SpeCom = SpeciesCommunity.objects.get(pk=speCom_ID)
        
        initial_dict = {
            'TargetType':SpeCom.TargetType,
            'Acronym':SpeCom.Acronym,
            'CommonName':SpeCom.CommonName,
            'ScientificName':SpeCom.ScientificName,
            'ITISTSN':SpeCom.ITISTSN,
            'CommunityName':SpeCom.CommunityName,
            'Synonyms':SpeCom.Synonyms,
            'Comments':SpeCom.Comments,
            'Picture':SpeCom.Picture,
        }
        
        spe_com_form = SpeComForm(request.POST or None, request.FILES or None, initial=initial_dict, instance=SpeCom,)
     
    if spe_com_form.is_valid(): 

        spe_com = spe_com_form.save(commit=False)
        spe_com.save()
        return redirect('/scopes/')
    
    else:
        return render(request, 'scopes/SpeCom.html', {'spe_com_form':spe_com_form, 'speCom_ID':speCom_ID})

@login_required
def location(request, loc_ID):
        
    if loc_ID == "0":
        location_form = LocationForm(request.POST)
    
    else:
        Location_Obj = Location.objects.get(pk=loc_ID)
        
        initial_dict = {
            'LocationCode':Location_Obj.LocationCode,
            'LocationName':Location_Obj.LocationName,
            'Description':Location_Obj.Description,
            'SpatialLayer':Location_Obj.SpatialLayer,
            'SpatialID':Location_Obj.SpatialID,
        }
        
        location_form = LocationForm(request.POST or None, request.FILES or None, initial=initial_dict, instance=Location,)
  
    if location_form.is_valid(): 

        location = location_form.save(commit=False)
        location.save()
        return redirect('/scopes/')
    
    else:
        return render(request, 'scopes/Location.html', {'location_form':location_form, 'loc_ID':loc_ID})

@login_required
def conMeasure(request, conMea_ID):
        
    if conMea_ID == "0":
        con_measure_form = ConMeasureForm(request.POST)
    
    else:
        ConMeas = ConservationMeasure.objects.get(pk=conMea_ID)
        
        initial_dict = {
            'CMCode':ConMeas.CMCode,
            'CMDescription':ConMeas.CMDescription,
            'SppHab':ConMeas.SppHab,
            'CMType':ConMeas.CMType,
            'CMSummary':ConMeas.CMSummary,
            'Status':ConMeas.Status,
        }
        
        con_measure_form = ConMeasureForm(request.POST or None, request.FILES or None, initial=initial_dict, instance=ConMeas,)
  
    
    if con_measure_form.is_valid(): 

        con_measure = con_measure_form.save(commit=False)
        con_measure.save()
        return redirect('/scopes/')
    
    else:
        return render(request, 'scopes/ConMeasure.html', {'con_measure_form':con_measure_form, 'conMea_ID': conMea_ID})

@login_required
def goal(request, goal_ID):
        
    if goal_ID == "0":
        goal_form = GoalForm(request.POST or None)
    
    else:
        goal_Obj = Goal.objects.get(pk=goal_ID)
        
        initial_dict = {
            'GoalName':goal_Obj.GoalName,
            'GoalType':goal_Obj.GoalType,
            'GoalDescription':goal_Obj.GoalDescription,
        }
        
        goal_form = GoalForm(request.POST or None, request.FILES or None, initial=initial_dict, instance=goal_Obj,)
    
    print(goal_form.errors.values())
    print(goal_form.data) 
    print(request.POST)
    
    if goal_form.is_valid(): 
        print("Valid!!!") 
        goal = goal_form.save(commit=False)
        goal.save()
        return redirect('/scopes/')
    
    else:
        print("Invalid")
        return render(request, 'scopes/Goal.html', {'goal_form':goal_form, 'goal_ID':goal_ID})