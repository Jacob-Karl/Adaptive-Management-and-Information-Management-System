from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
import reversion

# Create your views here.

@login_required
def hub(request):
    
    context_dict = {}
    
    all_species = SpeciesCommunity.objects.all()
    species_selected_field = request.GET.get('species_fields')
    if species_selected_field == 'TargetType':
        context_dict['SpeciesCommunity'] = all_species.filter(TargetType__icontains=request.GET.get('species_search'))
    elif species_selected_field == 'Acronym':
        context_dict['SpeciesCommunity'] = all_species.filter(Acronym__icontains=request.GET.get('species_search'))
    elif species_selected_field == 'CommonName':
        context_dict['SpeciesCommunity'] = all_species.filter(CommonName__icontains=request.GET.get('species_search'))
    elif species_selected_field == 'ScientificName':
        context_dict['SpeciesCommunity'] = all_species.filter(ScientificName__icontains=request.GET.get('species_search'))
    elif species_selected_field == 'ITISTSN':
        context_dict['SpeciesCommunity'] = all_species.filter(ITISTSN__icontains=request.GET.get('species_search'))
    elif species_selected_field == 'CommunityName':
        context_dict['SpeciesCommunity'] = all_species.filter(CommunityName__icontains=request.GET.get('species_search'))
    elif species_selected_field == 'Synonyms':
        context_dict['SpeciesCommunity'] = all_species.filter(Synonyms__icontains=request.GET.get('species_search'))
    elif species_selected_field == 'Comments':
        context_dict['SpeciesCommunity'] = all_species.filter(Comments__icontains=request.GET.get('species_search'))
    else: 
        context_dict['SpeciesCommunity'] = all_species 
        
    all_locations = Location.objects.all()
    location_selected_field = request.GET.get('location_fields')
    if location_selected_field == 'LocationCode':
        context_dict['Location'] = all_locations.filter(LocationCode__icontains=request.GET.get('location_search'))
    elif location_selected_field == 'LocationName':
        context_dict['Location'] = all_locations.filter(LocationName__icontains=request.GET.get('location_search'))
    elif location_selected_field == 'Description':
        context_dict['Location'] = all_locations.filter(Description__icontains=request.GET.get('location_search'))
    elif location_selected_field == 'SpatialLayer':
        context_dict['Location'] = all_locations.filter(SpatialLayer__icontains=request.GET.get('location_search'))
    elif location_selected_field == 'SpatialID':
        context_dict['Location'] = all_locations.filter(SpatialID__icontains=request.GET.get('location_search'))
    else: 
        context_dict['Location'] = all_locations
    
    all_measures = ConservationMeasure.objects.all()
    measure_selected_field = request.GET.get('conMeas_fields')
    if measure_selected_field == 'CMCode':
        context_dict['ConservationMeasure'] = all_measures.filter(CMCode__icontains=request.GET.get('conMeas_search'))
    elif measure_selected_field == 'CMDescription':
        context_dict['ConservationMeasure'] = all_measures.filter(CMDescription__icontains=request.GET.get('conMeas_search'))
    elif measure_selected_field == 'SppHab':
        context_dict['ConservationMeasure'] = all_measures.filter(SppHab__icontains=request.GET.get('conMeas_search'))
    elif measure_selected_field == 'CMType':
        context_dict['ConservationMeasure'] = all_measures.filter(CMType__icontains=request.GET.get('conMeas_search'))
    elif measure_selected_field == 'CMSummary':
        context_dict['ConservationMeasure'] = all_measures.filter(CMSummary__icontains=request.GET.get('conMeas_search'))
    elif measure_selected_field == 'Status':
        context_dict['ConservationMeasure'] = all_measures.filter(Status__icontains=request.GET.get('conMeas_search'))
    else: 
        context_dict['ConservationMeasure'] = all_measures
    
    all_goals = Goal.objects.all()
    goal_selected_field = request.GET.get('goal_fields')
    if goal_selected_field == 'GoalName':
        context_dict['ConservationMeasure'] = all_goals.filter(GoalName__icontains=request.GET.get('goal_search'))
    elif goal_selected_field == 'GoalType':
        context_dict['ConservationMeasure'] = all_goals.filter(GoalType__icontains=request.GET.get('goal_search'))
    elif goal_selected_field == 'GoalDescription':
        context_dict['ConservationMeasure'] = all_goals.filter(GoalDescription__icontains=request.GET.get('goal_search'))
    else: 
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

        with reversion.create_revision():
            spe_com = spe_com_form.save(commit=False)
            spe_com.save()
            reversion.set_user(request.user)
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

        with reversion.create_revision():
            location = location_form.save(commit=False)
            location.save()
            reversion.set_user(request.user)
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
    
        with reversion.create_revision():
            con_measure = con_measure_form.save(commit=False)
            con_measure.save()
            reversion.set_user(request.user)
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
    
    if goal_form.is_valid(): 
        with reversion.create_revision():
            goal = goal_form.save(commit=False)
            goal.save()
            reversion.set_user(request.user)
            return redirect('/scopes/')
    
    else:
        return render(request, 'scopes/Goal.html', {'goal_form':goal_form, 'goal_ID':goal_ID})