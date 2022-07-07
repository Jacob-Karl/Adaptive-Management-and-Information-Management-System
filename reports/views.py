import django
import os
import datetime
from django.shortcuts import *
from reports.forms import *
from django.contrib import *
from django.contrib.auth.decorators import login_required
from projects.models import *
from scopes.models import *
import time

# Create your views here.
@login_required
def hub(request):
    context_dict = {}
    
    all_projects = Project.objects.all()
    context_dict = {
        'All_Projects' : all_projects,
    }
    
    return render(request, 'reports/report_hub.html', context_dict)

@login_required
def prepare_report(request, project_ID):
    print(django.get_version())
    report_selector_form = reportSelectorForm(request.POST)
    
    context_dict = {
        'project_ID':project_ID,
        'report_selector_form':report_selector_form,
    }
    
    if report_selector_form.is_valid():
        print("------------------------")
        print(report_selector_form)
        print(request.POST)
        template_file = open("C:/Users/Jacobs Laptop PC/Documents/AMATRA/AMATRA/AIMS/static/AIMS output template v2.txt", "r")
        template = template_file.read()
        template_file.close()
        report_selector_form = reportSelectorForm(request.POST)
    
        projectObj = Project.objects.get(id=project_ID)
        context_dict = {report_selector_form,}
    
        all_projects = Project.objects.all()
        context_dict= {
            'All_Projects': all_projects,
        }
    
        chunks = template.split("//chunk//")
    
        templateTree = "N/A"
        projectTemplate = "N/A"
        projectTriggerTemplate = "N/A"
        triggerStatusTemplate = "N/A"
        projectObjectiveTemplate = "N/A"
        objectiveMilestoneTemplate = "N/A"
        objectiveStepTemplate = "N/A"
        stepMethodTemplate = "N/A"
        methodProtocolTemplate = "N/A"
    
        for item in chunks:
            name = item[2:item.find("/>")]
            if name == "template":
                templateTree = item[item.find("/>")+2:]
            if name == "project":
                projectTemplate = item[item.find("/>")+2:]
            elif name == "project_trigger":
                projectTriggerTemplate = item[item.find("/>")+2:]
            elif name == "trigger_status":
                triggerStatusTemplate = item[item.find("/>")+2:]
            elif name == "project_objective":
                projectObjectiveTemplate = item[item.find("/>")+2:]
            elif name == "objective_milestone":
                objectiveMilestoneTemplate = item[item.find("/>")+2:]
            elif name == "objective_step":
                objectiveStepTemplate = item[item.find("/>")+2:]
            elif name == "step_method":
                stepMethodTemplate = item[item.find("/>")+2:]
            elif name == "method_protocol":
                methodProtocolTemplate = item[item.find("/>")+2:]
    
    #From the template get each individual object layout
    #Use template to build a population tree
    #Use Object to fill out the tree with all the appropriate and named objects
    #navigate the tree and fill out each template stub with object info
    #Print the tree contents into the output file
    
    #The report page will have a series of interdependant tik boxes, based on which boxes
    #are untiked the reporting function will break before filling out the report 
    
    #Specify file output path
    
        all_obj_acryonyms = ""
        all_conMeas_codes = ""
        all_loc_codes = ""
        all_goal_names = ""
    
        for obj in projectObj.SpeComs.all():
            all_obj_acryonyms = all_obj_acryonyms + obj.Acronym
    
        for con in projectObj.ConMeas.all():
            all_conMeas_codes = all_conMeas_codes + con.CMCode
        
        for loc in projectObj.Locations.all():
            all_loc_codes = all_loc_codes + loc.LocationCode
        
        for goal in projectObj.Goals.all():
            all_goal_names = all_goal_names + goal.GoalName
    
        report = projectTemplate.format(project_id = projectObj.WorktaskID, project_name = projectObj.ProjectName, time_now = time.asctime( time.localtime(time.time()) ), project_lead = projectObj.ProjectLead, project_status = projectObj.ProjectStatus, project_type = projectObj.ProjectType, project_startDate = projectObj.ProjectStart, project_endDate = projectObj.ProjectEnd, project_summary = projectObj.ProjectSummary, project_background = projectObj.ProjectBackground, project_speComs = all_obj_acryonyms, project_conMeas = all_conMeas_codes, project_locations = all_loc_codes, project_goals = all_goal_names)                                    
               
        projectTriggers = Trigger.objects.filter(ProjectID = project_ID)
               
        for trigger in projectTriggers:
            report = report + projectTriggerTemplate.format(trigger_name = trigger.TriggerName, trigger_description = trigger.TriggerDescription, trigger_indicators = trigger.TriggerIndicators, trigger_response = trigger.ProposedResponse)
        
            triggerStatuses = TriggerStatus.objects.filter(TriggerID = trigger.id)
        
            for status in triggerStatuses:
                report = report + triggerStatusTemplate.format(status_trend = status.StatusTrend, status_date = status.ReportingDate, status_interpretation = status.MgmtInterp, status_response = status.MgmtResponse)
     
        projectObjectives = Objective.objects.filter(ProjectID = project_ID)
            
        for objective in projectObjectives:
            report = report + projectObjectiveTemplate.format(objective_code = objective.ObjCode, objective_name = objective.ObjName, objective_description = objective.ObjDescription, objective_startDate = objective.ObjStartDate, objective_endDate = objective.ObjEndDate, objective_flowDiagram = objective.ObjFlowDiagram)
        
            objectiveMilestones = Milestone.objects.filter(ObjectiveID = objective.id)
        
            for milestone in objectiveMilestones:
                milestoneProgress = MilestoneProgress.objects.filter(MilestoneID = milestone.id)
                report = report + objectiveMilestoneTemplate.format(milestone_description = milestone.Description, milestone_progress = milestoneProgress.Description)
            
            objectiveSteps = Step.objects.filter(ObjectiveID = objective.id)
        
            for step in objectiveSteps:
                report = report + objectiveStepTemplate.format(step_code = step.StepCode, step_name = step.StepName, step_type = step.StepType, step_summary = step.StepSummary, step_startDate = step.StepStartDate, step_endDate = step.StepEndDate, step_dependancies = step.StepDependencies)
            
                stepMethods = Method.objects.filter(StepID = step.id)
            
                for method in stepMethods:
                    report = report + stepMethodTemplate.format(method_code = method.MethodCode, method_title = method.MethodTitle, method_type = method.MethodType, method_date = method.MethodDate, method_version = method.MethodVersion, method_description = method.MethodDescription, method_contact = method.MethodContact)
                
                    methodProtocols = Protocol.objects.filter(MethodID = method.id)
                
                    for protocol in methodProtocols:
                        report = report + methodProtocolTemplate.format(protocol_tile = protocol.ProtocolTitle, protocol_version = protocol.ProtocolVerision, protocol_date = protocol.ProtocolDate, protocol_author = protocol.ProtocolAuthor, protocol_description = protocol.ProtocolDescription, protocol_link = protocol.ProtocolLink)
                       
        #print(report)
    
        report_file = open("C:/Users/Jacobs Laptop PC/Documents/AMATRA/AMATRA/AIMS/static/"+ projectObj.WorktaskID + "_report.txt", "w")
        report_file.write(report)
        report_file.close()
    
        return render(request, 'reports/report_hub.html', context_dict)    
    return render(request, 'reports/report.html', context_dict)

#generate report need to be reworked to take the output of the report prepare via the URL
#It then needs to take the input and break when appropriate

@login_required
def generate_report(request, project_ID):
    print("////////////////////////")
    print(request.POST)    
    template_file = open("C:/Users/Jacobs Laptop PC/Documents/AMATRA/AMATRA/AIMS/static/AIMS output template v2.txt", "r")
    template = template_file.read()
    template_file.close()
    
    report_selector_form = reportSelectorForm(request.POST)
    
    projectObj = Project.objects.get(id=project_ID)
    context_dict = {report_selector_form,}
    
    all_projects = Project.objects.all()
    context_dict= {
        'All_Projects': all_projects,
    }
    
    chunks = template.split("//chunk//")
    
    templateTree = "N/A"
    projectTemplate = "N/A"
    projectTriggerTemplate = "N/A"
    triggerStatusTemplate = "N/A"
    projectObjectiveTemplate = "N/A"
    objectiveMilestoneTemplate = "N/A"
    objectiveStepTemplate = "N/A"
    stepMethodTemplate = "N/A"
    methodProtocolTemplate = "N/A"
    
    for item in chunks:
        name = item[2:item.find("/>")]
        if name == "template":
            templateTree = item[item.find("/>")+2:]
        if name == "project":
            projectTemplate = item[item.find("/>")+2:]
        elif name == "project_trigger":
            projectTriggerTemplate = item[item.find("/>")+2:]
        elif name == "trigger_status":
            triggerStatusTemplate = item[item.find("/>")+2:]
        elif name == "project_objective":
            projectObjectiveTemplate = item[item.find("/>")+2:]
        elif name == "objective_milestone":
            objectiveMilestoneTemplate = item[item.find("/>")+2:]
        elif name == "objective_step":
            objectiveStepTemplate = item[item.find("/>")+2:]
        elif name == "step_method":
            stepMethodTemplate = item[item.find("/>")+2:]
        elif name == "method_protocol":
            methodProtocolTemplate = item[item.find("/>")+2:]
    
    #From the template get each individual object layout
    #Use template to build a population tree
    #Use Object to fill out the tree with all the appropriate and named objects
    #navigate the tree and fill out each template stub with object info
    #Print the tree contents into the output file
    
    #The report page will have a series of interdependant tik boxes, based on which boxes
    #are untiked the reporting function will break before filling out the report 
    
    #Specify file output path
    
    all_obj_acryonyms = ""
    all_conMeas_codes = ""
    all_loc_codes = ""
    all_goal_names = ""
    
    for obj in projectObj.SpeComs.all():
        all_obj_acryonyms = all_obj_acryonyms + obj.Acronym
    
    for con in projectObj.ConMeas.all():
        all_conMeas_codes = all_conMeas_codes + con.CMCode
        
    for loc in projectObj.Locations.all():
        all_loc_codes = all_loc_codes + loc.LocationCode
        
    for goal in projectObj.Goals.all():
        all_goal_names = all_goal_names + goal.GoalName
    
    report = projectTemplate.format(project_id = projectObj.WorktaskID, project_name = projectObj.ProjectName, time_now = time.asctime( time.localtime(time.time()) ), project_lead = projectObj.ProjectLead, project_status = projectObj.ProjectStatus, project_type = projectObj.ProjectType, project_startDate = projectObj.ProjectStart, project_endDate = projectObj.ProjectEnd, project_summary = projectObj.ProjectSummary, project_background = projectObj.ProjectBackground, project_speComs = all_obj_acryonyms, project_conMeas = all_conMeas_codes, project_locations = all_loc_codes, project_goals = all_goal_names)                                    
               
    projectTriggers = Trigger.objects.filter(ProjectID = project_ID)
               
    for trigger in projectTriggers:
        if request.POST.get('triggerToggle','') != 'on':
            break
        report = report + projectTriggerTemplate.format(trigger_name = trigger.TriggerName, trigger_description = trigger.TriggerDescription, trigger_indicators = trigger.TriggerIndicators, trigger_response = trigger.ProposedResponse)
        
        triggerStatuses = TriggerStatus.objects.filter(TriggerID = trigger.id)
        
        for status in triggerStatuses:
            if request.POST.get('triggerStatusToggle','') != 'on':
                break
            report = report + triggerStatusTemplate.format(status_trend = status.StatusTrend, status_date = status.ReportingDate, status_interpretation = status.MgmtInterp, status_response = status.MgmtResponse)
     
    projectObjectives = Objective.objects.filter(ProjectID = project_ID)
            
    for objective in projectObjectives:
        if request.POST.get('objectiveToggle','') != 'on':
            break        
        report = report + projectObjectiveTemplate.format(objective_code = objective.ObjCode, objective_name = objective.ObjName, objective_description = objective.ObjDescription, objective_startDate = objective.ObjStartDate, objective_endDate = objective.ObjEndDate, objective_flowDiagram = objective.ObjFlowDiagram)
        
        objectiveMilestones = Milestone.objects.filter(ObjectiveID = objective.id)
        
        for milestone in objectiveMilestones:
            if request.POST.get('milestoneToggle','') != 'on':
                break            
            milestoneProgress = MilestoneProgress.objects.filter(MilestoneID = milestone.id)
            report = report + objectiveMilestoneTemplate.format(milestone_description = milestone.Description, milestone_progress = milestoneProgress.Description)
            
        objectiveSteps = Step.objects.filter(ObjectiveID = objective.id)
        
        for step in objectiveSteps:
            if request.POST.get('stepToggle','') != 'on':
                break            
            report = report + objectiveStepTemplate.format(step_code = step.StepCode, step_name = step.StepName, step_type = step.StepType, step_summary = step.StepSummary, step_startDate = step.StepStartDate, step_endDate = step.StepEndDate, step_dependancies = step.StepDependencies)
            
            stepMethods = Method.objects.filter(StepID = step.id)
            
            for method in stepMethods:
                if request.POST.get('methodToggle','') != 'on':
                    break                
                report = report + stepMethodTemplate.format(method_code = method.MethodCode, method_title = method.MethodTitle, method_type = method.MethodType, method_date = method.MethodDate, method_version = method.MethodVersion, method_description = method.MethodDescription, method_contact = method.MethodContact)
                
                methodProtocols = Protocol.objects.filter(MethodID = method.id)
                
                for protocol in methodProtocols:
                    if request.POST.get('outputToggle','') != 'on':
                        break                    
                    report = report + methodProtocolTemplate.format(protocol_tile = protocol.ProtocolTitle, protocol_version = protocol.ProtocolVerision, protocol_date = protocol.ProtocolDate, protocol_author = protocol.ProtocolAuthor, protocol_description = protocol.ProtocolDescription, protocol_link = protocol.ProtocolLink)
                       
    print(report)
    print(os.path.expanduser('~user'))
    print(request.POST.get('outputPath',''))
    #Save to Downloads folder with date/time/version number -X-
    #Work on new budget/workplan due next Friday -X-
    #Backup on Github
    #report_file = open("C:/Users/Jacobs Laptop PC/Documents/AMATRA/AMATRA/AIMS/static/"+ projectObj.WorktaskID + "_report.txt", "w")
    report_file = open(os.path.expanduser('~') + '\\Downloads\\' + projectObj.WorktaskID + "_report" + str(datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")) + ".txt", "w")
    report_file.write(report)
    report_file.close()
    
    return render(request, 'reports/report_hub.html', context_dict)