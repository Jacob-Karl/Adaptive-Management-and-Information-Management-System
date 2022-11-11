from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from scopes.models import *
from user_functions.models import *
from .forms import *
from .models import *
import reversion

# Create your views here.
@login_required
def hub(request):
    context_dict = {}
    
    all_projects = Project.objects.all()
    context_dict['All_Projects'] = all_projects
    
    return render(request, 'projects/project_hub.html', context_dict)

@login_required
def project(request, project_ID):
    
    initial_dict = {
        }
    
    if project_ID == "0":
        project_form = ProjectForm(request.POST or None)
    
    else:
        project_Obj = Project.objects.get(pk=project_ID)       
        
        initial_dict = {
            'WorktaskID':project_Obj.WorktaskID,
            'ProjectName':project_Obj.ProjectName,
            'ProjectLead':project_Obj.ProjectLead,
            'ProjectStatus':project_Obj.ProjectStatus,
            'ProjectType':project_Obj.ProjectType,
            'ProjectStart':project_Obj.ProjectStart,
            'ProjectEnd':project_Obj.ProjectEnd,
            'ProjectSummary':project_Obj.ProjectSummary,
            'ProjectBackground':project_Obj.ProjectBackground,
            'OtherConsMeas':project_Obj.OtherConsMeas,
            'OtherSpecies':project_Obj.OtherSpecies,
            'Triggers':project_Obj.Triggers.all(),
            'Outputs':project_Obj.Outputs.all(),
            'Objectives':project_Obj.Objectives.all(),
            'SpeComs':project_Obj.SpeComs.all(),
            'ConMeas':project_Obj.ConMeas.all(),
            'Locations':project_Obj.Locations.all(),
            'Goals':project_Obj.Goals.all(),
            'RelatedProjects':project_Obj.RelatedProjects.all(),
        }
        
        project_form = ProjectForm(request.POST or None, initial=initial_dict, instance=project_Obj,)
        
    trigger_helper_form = TriggerHelperForm()
    output_helper_form = OutputHelperForm()
    objective_helper_form = ObjectiveHelperForm()
    
    context_dict = {
        'project_form':project_form,
        'project_ID':project_ID
    }    
    
    if 'add_Trigger' in request.GET:
        new_trigger = Trigger(ProjectID = project_Obj)
        new_trigger.save()
        project_Obj.save()
        project_Obj.Triggers.add(new_trigger)
        context_dict.update(initial_dict)
        print(project_form.is_valid())
        #if project_form.is_valid():
        project = project_form.save(commit=False)
        project.save()        
        return render(request, 'projects/Project.html', context_dict)
    
    elif 'add_Output' in request.GET:
        new_output = Output(ProjectID = project_Obj)
        new_output.save()
        project_Obj.save()
        project_Obj.Outputs.add(new_output)
        context_dict.update(initial_dict)
        return render(request, 'projects/Project.html', context_dict)
    
    elif 'add_Objective' in request.GET:
        new_objective = Objective(ProjectID = project_Obj)
        new_objective.save()
        project_Obj.save()
        project_Obj.Objectives.add(new_objective)
        context_dict.update(initial_dict)
        return render(request, 'projects/Project.html', context_dict)    
    
    elif 'add_Related_Projects' in request.GET:
        new_related_project = RelatedProject(Project = project_Obj)
        new_related_project.save()
        project_Obj.save()
        project_Obj.RelatedProjects.add(new_related_project)
        context_dict.update(initial_dict)
        return render(request, 'projects/Project.html', context_dict)        
    
    elif 'project_Submit' in request.POST:
        if project_form.is_valid():
            with reversion.create_revision():
                project = project_form.save(commit=False)
                try:
                    logged_in_profile = UserProfile.objects.get(User = request.user.id)
                    logged_in_person = logged_in_profile.Person
                    #try:
                    project_contributor = Contributor(PeopleID = logged_in_person)
                    project_contributor.save()
                    #except:
                    #    project_contributor = Contributor.objects.get(PeopleID = logged_in_person.id)
                    project.ProjectContributors.add(project_contributor)  
                except:
                    pass
                project.save()
                reversion.set_user(request.user)
                reversion.set_comment("revision test")                
                return redirect('/projects/')
        else:
            print("Form invalid")
            return render(request, 'projects/Project.html', context_dict)
    
    else:
        context_dict.update(initial_dict)        
        return render(request, 'projects/Project.html', context_dict)
 
@login_required
def speComAdder(request, project_ID):
    
    speCom_adder_form = SpeComAdderForm(request.POST)
    project_Obj = Project.objects.get(pk=project_ID)
    context_dict = {
        'speCom_adder_form':speCom_adder_form,
        'project_ID':project_ID,
    }
    
    if speCom_adder_form.is_valid():
        
        for item in request.POST.getlist('SpeComs'):
            speCom_Obj = SpeciesCommunity.objects.get(pk = item)
            project_Obj.SpeComs.add(speCom_Obj)
                                  
        return redirect('/projects/Project/'+project_ID+'/')
    else:
        return render(request, 'projects/SpeCom Adder.html', context_dict) 
    
@login_required
def conMeasAdder(request, project_ID):
    
    conMeas_adder_form = ConMeasAdderForm(request.POST)
    project_Obj = Project.objects.get(pk=project_ID)
    context_dict = {
        'conMeas_adder_form':conMeas_adder_form,
        'project_ID':project_ID,
    }
    
    if conMeas_adder_form.is_valid():
        
        for item in request.POST.getlist('ConMeas'):
            conMeas_Obj = ConservationMeasure.objects.get(pk = item)
            project_Obj.ConMeas.add(conMeas_Obj)
                                  
        return redirect('/projects/Project/'+project_ID+'/')
    else:
        return render(request, 'projects/ConMeas Adder.html', context_dict) 
    
@login_required
def locationAdder(request, project_ID):
    
    location_adder_form = LocationAdderForm(request.POST)
    project_Obj = Project.objects.get(pk=project_ID)
    context_dict = {
        'location_adder_form':location_adder_form,
        'project_ID':project_ID,
    }
    
    if location_adder_form.is_valid():
        for item in request.POST.getlist('Locations'):
            location_Obj = Location.objects.get(pk = item)
            project_Obj.Locations.add(location_Obj)
                                  
        return redirect('/projects/Project/'+project_ID+'/')
    else:
        return render(request, 'projects/Location Adder.html', context_dict)
   
@login_required
def goalAdder(request, project_ID):
    
    goal_adder_form = GoalAdderForm(request.POST)
    project_Obj = Project.objects.get(pk=project_ID)
    context_dict = {
        'goal_adder_form':goal_adder_form,
        'project_ID':project_ID,
    }
    

    if goal_adder_form.is_valid():
        for item in request.POST.getlist('Goals'):
            goal_Obj = Goal.objects.get(pk = item)
            project_Obj.Goals.add(goal_Obj)
                                
            return redirect('/projects/Project/'+project_ID+'/')
    else:
        return render(request, 'projects/Goal Adder.html', context_dict)
        

@login_required
def relatedProject(request, related_project_ID):
    if related_project_ID == "0":
        related_project_form = RelatedProject(request.POST or None)
    
    else:
        related_project_Obj = RelatedProject.objects.get(pk=related_project_ID)
        
        initial_dict = {
            'WorktaskID':related_project_Obj.WorktaskID,
            'RelationshipType':related_project_Obj.RelationshipType,          
        }
        
        related_project_form = RelatedProjectForm(request.POST or None, request.FILES or None, initial=initial_dict, instance=related_project_Obj,)
    
    #related_project_helper_form = RelatedProjectHelperForm()
    
    context_dict = {
        'related_project_form':related_project_form,
        'project_ID':related_project_Obj.Project.id,
        'related_project_ID':related_project_ID,
    }     
      
    if related_project_form.is_valid():
        with reversion.create_revision():
            related_project = related_project_form.save(commit=False)
            related_project.save()
            reversion.set_user(request.user)
            project = related_project_Obj.Project.id
            return redirect('/projects/Project/'+str(project)+'/')
    else:
        context_dict.update(initial_dict)
        return render(request, 'projects/RelatedProject.html', context_dict)

@login_required
def trigger(request, trigger_ID):
            
    if trigger_ID == "0":
        trigger_form = TriggerForm(request.POST or None)
    
    else:
        trigger_Obj = Trigger.objects.get(pk=trigger_ID)
        
        initial_dict = {
            'TriggerName':trigger_Obj.TriggerName,
            'TriggerDescription':trigger_Obj.TriggerDescription,
            'TriggerIndicators':trigger_Obj.TriggerIndicators,
            'ProposedResponse':trigger_Obj.ProposedResponse,
            'TriggerStatuses':trigger_Obj.TriggerStatus.all(),
        }
        
        trigger_form = TriggerForm(request.POST or None, initial=initial_dict, instance=trigger_Obj,)
        
    trigger_status_helper_form = TriggerStatusHelperForm()
    context_dict = {
        'trigger_form':trigger_form,
        'trigger_ID':trigger_ID,
        'project_ID':trigger_Obj.ProjectID.id,
    }     
    
    if 'add_Trigger_Status' in request.GET:
        new_trigger_status = TriggerStatus(TriggerID = trigger_Obj)
        new_trigger_status.save()
        trigger_Obj.save()
        trigger_Obj.TriggerStatus.add(new_trigger_status)
        context_dict.update(initial_dict)
        return render(request, 'projects/Trigger.html', context_dict)        
    else:    
        if trigger_form.is_valid():
            with reversion.create_revision():
                trigger = trigger_form.save(commit=False)
                trigger.save()
                reversion.set_user(request.user)
                project = trigger_Obj.ProjectID.id
                return redirect('/projects/Project/'+str(project)+'/')
    
        else:
            context_dict.update(initial_dict)  
            return render(request, 'projects/Trigger.html', context_dict)

@login_required
def triggerStatus(request, trigger_status_ID):
            
    if trigger_status_ID == "0":
        trigger_status_form = TriggerStatusForm(request.POST or None)
    
    else:
        trigger_status_Obj = TriggerStatus.objects.get(pk=trigger_status_ID)
        
        initial_dict = {
            'ReportingDate':trigger_status_Obj.ReportingDate,
            'StatusTrend':trigger_status_Obj.StatusTrend,
            'MgmtInterp':trigger_status_Obj.MgmtInterp,
            'MgmtResponse':trigger_status_Obj.MgmtResponse,
        }
        
        trigger_status_form = TriggerStatusForm(request.POST or None, request.FILES or None, initial=initial_dict, instance=trigger_status_Obj,)
    
    context_dict = {
        'trigger_status_form':trigger_status_form,
        'trigger_status_ID':trigger_status_ID
    }
    
    if trigger_status_form.is_valid(): 
        with reversion.create_revision():
            trigger_status = trigger_status_form.save(commit=False)
            trigger_status.save()
            reversion.set_user(request.user)
            trigger = trigger_status_Obj.TriggerID.id
            return redirect('/projects/Trigger/'+str(trigger)+'/')
    
    else:
        context_dict.update(initial_dict)
        return render(request, 'projects/TriggerStatus.html', context_dict)

@login_required
def output(request, output_ID):
    if output_ID == "0":
        output_form = OutputForm(request.POST or None)
    
    else:
        output_Obj = Output.objects.get(pk=output_ID)
        
        initial_dict = {
            'OutputType':output_Obj.OutputType,
            'OutputAuthors':output_Obj.OutputAuthors,
            'OutputDate':output_Obj.OutputDate,
            'OutputTitle':output_Obj.OutputTitle,
            'OutputVersion':output_Obj.OutputVersion,
            'OutputDescription':output_Obj.OutputDescription,
            'OutputDOI':output_Obj.OutputDOI,
            'OutputCitation':output_Obj.OutputCitation,
            'OutputURI':output_Obj.OutputURI,
            'OutputConstraints':output_Obj.OutputConstraints,        
        }
        
        output_form = OutputForm(request.POST or None, request.FILES or None, initial=initial_dict, instance=output_Obj,)
    
    context_dict = {
        'output_form':output_form,
        'output_ID':output_ID,
        'project_ID':output_Obj.ProjectID.id,
    }   
    
    if output_form.is_valid():
        with reversion.create_revision():
            output = output_form.save(commit=False)
            output.save()
            reversion.set_user(request.user)
            project = output_Obj.ProjectID.id
            return redirect('/projects/Project/'+str(project)+'/')
    
    else:
        context_dict.update(initial_dict)
        return render(request, 'projects/Output.html', context_dict)

@login_required
def objective(request, objective_ID):
    if objective_ID == "0":
        objective_form = ObjectiveForm(request.POST or None)
    
    else:
        objective_Obj = Objective.objects.get(pk=objective_ID)
        
        initial_dict = {
            'ObjCode':objective_Obj.ObjCode,
            'ObjName':objective_Obj.ObjName,
            'ObjDescription':objective_Obj.ObjDescription,
            'ObjStartDate':objective_Obj.ObjStartDate,
            'ObjEndDate':objective_Obj.ObjEndDate,
            'ObjFlowDiagram':objective_Obj.ObjFlowDiagram,
            'Milestones':objective_Obj.Milestones.all(),
            'Steps':objective_Obj.Steps.all()
        }
        
        objective_form = ObjectiveForm(request.POST or None, request.FILES or None, initial=initial_dict, instance=objective_Obj,)
    
    milestone_helper_form = MilestoneHelperForm()
    step_helper_form = StepHelperForm()
    context_dict = {
        'objective_form':objective_form,
        'objective_ID':objective_ID,
        'project_ID':objective_Obj.ProjectID.id,
    }     
    
    if 'add_Milestone' in request.GET:
        new_milestone = Milestone(ObjectiveID = objective_Obj)
        new_milestone.save()
        objective_Obj.save()
        objective_Obj.Milestones.add(new_milestone)
        context_dict.update(initial_dict)
        return render(request, 'projects/Objective.html', context_dict)
    elif 'add_Step' in request.GET:
        new_step = Step(ObjectiveID = objective_Obj)
        new_step.save()
        objective_Obj.save()
        objective_Obj.Steps.add(new_step)
        context_dict.update(initial_dict)
        return render(request, 'projects/Objective.html', context_dict)     
    else:    
        if objective_form.is_valid():
            with reversion.create_revision():
                objective = objective_form.save(commit=False)
                objective.save()
                reversion.set_user(request.user)
                project = objective_Obj.ProjectID.id
                return redirect('/projects/Project/'+str(project)+'/')
        else:
            context_dict.update(initial_dict)  
            return render(request, 'projects/Objective.html', context_dict)


@login_required
def milestone(request, milestone_ID):
    if milestone_ID == "0":
        milestone_form = MilestoneForm(request.POST or None)
    
    else:
        milestone_Obj = Milestone.objects.get(pk=milestone_ID)
        
        initial_dict = {
            'Description':milestone_Obj.Description,
            'MilestoneProgress':milestone_Obj.MilestoneProgress.all(),
        }
        
        milestone_form = MilestoneForm(request.POST or None, request.FILES or None, initial=initial_dict, instance=milestone_Obj,)
    
    milestone_progress_helper_form = MilestoneProgressHelperForm()
    context_dict = {
        'milestone_form':milestone_form,
        'objective_ID':milestone_Obj.ObjectiveID.id,
        'milestone_ID':milestone_ID,
    }     
    
    if 'add_Milestone_Progress' in request.GET:
        new_milestone_progress = MilestoneProgress(MilestoneID = milestone_Obj)
        new_milestone_progress.save()
        milestone_Obj.save()
        milestone_Obj.MilestoneProgress.add(new_milestone_progress)
        context_dict.update(initial_dict)
        return render(request, 'projects/Milestone.html', context_dict)        
    else:    
        if milestone_form.is_valid():
            with reversion.create_revision():
                milestone = milestone_form.save(commit=False)
                milestone.save()
                reversion.set_user(request.user)
                objective = milestone_Obj.ObjectiveID.id
                return redirect('/projects/Objective/'+str(objective)+'/')
        else:
            context_dict.update(initial_dict)
            return render(request, 'projects/Milestone.html', context_dict)

@login_required
def milestoneProgress(request, milestone_progress_ID):
    if milestone_progress_ID == "0":
        milestone_progress_form = MilestoneProgressForm(request.POST or None)
    
    else:
        milestone_progress_Obj = MilestoneProgress.objects.get(pk=milestone_progress_ID)
        
        initial_dict = {
            'ReportingDate':milestone_progress_Obj.ReportingDate,
            'Status':milestone_progress_Obj.Status,
            'Description':milestone_progress_Obj.Description,
        }
        
        milestone_progress_form = MilestoneProgressForm(request.POST or None, request.FILES or None, initial=initial_dict, instance=milestone_progress_Obj,)
    
    context_dict = {
        'milestone_progress_form':milestone_progress_form,
        'milestone_ID':milestone_progress_Obj.MilestoneID.id,
        'milestone_progress_ID':milestone_progress_ID,
    }     
      
    if milestone_progress_form.is_valid():
        with reversion.create_revision():
            milestone_progress = milestone_progress_form.save(commit=False)
            milestone_progress.save()
            reversion.set_user(request.user)
            milestone = milestone_progress_Obj.MilestoneID.id
            return redirect('/projects/Milestone/'+str(milestone)+'/')
    else:
        context_dict.update(initial_dict)
        return render(request, 'projects/MilestoneProgress.html', context_dict)

@login_required
def step(request, step_ID):
    if step_ID == "0":
        step_form = StepForm(request.POST or None)
    
    else:
        step_Obj = Step.objects.get(pk=step_ID)
        
        initial_dict = {
            'StepName':step_Obj.StepName,
            'StepCode':step_Obj.StepCode,
            'StepType':step_Obj.StepType,
            'StepSummary':step_Obj.StepSummary,
            'StepStartDate':step_Obj.StepStartDate,
            'StepEndDate':step_Obj.StepEndDate,
            'StepDependencies':step_Obj.StepDependencies,
            'Methods':step_Obj.Methods.all(),
        }
        
        step_form = StepForm(request.POST or None, request.FILES or None, initial=initial_dict, instance=step_Obj,)
    
    method_helper_form = MethodHelperForm()
    context_dict = {
        'step_form':step_form,
        'objective_ID':step_Obj.ObjectiveID.id,
        'step_ID':step_ID,
    }     
    
    if 'add_Method' in request.GET:
        new_method = Method(StepID = step_Obj)
        new_method.save()
        step_Obj.save()
        step_Obj.Methods.add(new_method)
        context_dict.update(initial_dict)
        return render(request, 'projects/Step.html', context_dict)        
    else:    
        if step_form.is_valid():
            with reversion.create_revision():
                step = step_form.save(commit=False)
                step.save()
                reversion.set_user(request.user)
                objective = step_Obj.ObjectiveID.id
                return redirect('/projects/Objective/'+str(objective)+'/')
        else:
            context_dict.update(initial_dict)
            return render(request, 'projects/Step.html', context_dict)


@login_required
def method(request, method_ID):
    if method_ID == "0":
        method_form = MethodForm(request.POST or None)
    
    else:
        method_Obj = Method.objects.get(pk=method_ID)
        
        initial_dict = {
            'MethodTitle':method_Obj.MethodTitle,
            'MethodCode':method_Obj.MethodCode,
            'MethodType':method_Obj.MethodType,
            'MethodDate':method_Obj.MethodDate,
            'MethodVersion':method_Obj.MethodVersion,
            'MethodDescription':method_Obj.MethodDescription,
            'MethodContact':method_Obj.MethodContact,
            'Protocols':method_Obj.Protocols.all(),
        }
        
        method_form = MethodForm(request.POST or None, request.FILES or None, initial=initial_dict, instance=method_Obj,)
    
    protocol_helper_form = ProtocolHelperForm()
    context_dict = {
        'method_form':method_form,
        'step_ID':method_Obj.StepID.id,
        'method_ID':method_ID,
    }     
    
    if 'add_Protocol' in request.GET:
        new_protocol = Protocol(MethodID = method_Obj)
        new_protocol.save()
        method_Obj.save()
        method_Obj.Protocols.add(new_protocol)
        context_dict.update(initial_dict)
        return render(request, 'projects/Method.html', context_dict)        
    else:    
        if method_form.is_valid():
            with reversion.create_revision():
                method = method_form.save(commit=False)
                method.save()
                reversion.set_user(request.user)
                step = method_Obj.StepID.id
                return redirect('/projects/Step/'+str(step)+'/')
        else:
            context_dict.update(initial_dict)
            return render(request, 'projects/Method.html', context_dict)

@login_required
def protocol(request, protocol_ID):
    if protocol_ID == "0":
        protocol_form = Protocol(request.POST or None)
    
    else:
        protocol_Obj = Protocol.objects.get(pk=protocol_ID)
        
        initial_dict = {
            'ProtocolTitle':protocol_Obj.ProtocolTitle,
            'ProtocolVerision':protocol_Obj.ProtocolVerision,
            'ProtocolDate':protocol_Obj.ProtocolDate,
            'ProtocolAuthor':protocol_Obj.ProtocolAuthor,
            'ProtocolDescription':protocol_Obj.ProtocolDescription,
            'ProtocolLink':protocol_Obj.ProtocolLink,            
        }
        
        protocol_form = ProtocolForm(request.POST or None, request.FILES or None, initial=initial_dict, instance=protocol_Obj,)
    
    context_dict = {
        'protocol_form':protocol_form,
        'method_ID':protocol_Obj.MethodID.id,
        'protocol_ID':protocol_ID,
    }     
      
    if protocol_form.is_valid():
        with reversion.create_revision():
            protocol = protocol_form.save(commit=False)
            protocol.save()
            reversion.set_user(request.user)
            method = protocol_Obj.MethodID.id
            return redirect('/projects/Milestone/'+str(method)+'/')
    else:
        context_dict.update(initial_dict)
        return render(request, 'projects/Protocol.html', context_dict)
