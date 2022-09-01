#AIMS Full project importing
from datetime import datetime
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AIMS.settings")
import django
django.setup()
from projects.models import *
from scopes.models import *

f = open("..\LCR MSCP D08 Adaptive Management Plan DRAFT 2021-11-15.txt","rb")
f_text = str(f.readlines())

f_text = f_text.replace('\\r', '')
f_text = f_text.replace("', b'", '')

WorktaskIDstart = f_text.find("Project (Work Task) ID")
NameStart = f_text.find("Project (Work Task) Name")
VersionDateStart = f_text.find("Project Plan Version Date")
LeadStart = f_text.find("Project Lead")
ContributorStart = f_text.find("Project Plan Contributors")
StatusStart = f_text.find("Project Status")
TypeStart = f_text.find("Project Type")
StartDateStart = f_text.find("Project Start Date")
EndDateStart = f_text.find("Project End Date")
SummaryStart = f_text.find("Project Summary")
BackgroundStart = f_text.find("Project Background")
SpeComStart = f_text.find("Associated Species and Cover Type Targets")
ConMeasStart = f_text.find("Associated Conservation Measures")
LocationStart = f_text.find("Associated Locations")
GoalStart = f_text.find("Associated Ecological Goals")
TriggerStart = f_text.find("Project Decision Triggers")
OtherConMeasStart = f_text.find("Other Affected Conservation Measures")
OtherSpeComStart = f_text.find("Other Affected Covered and Evaluation Species")
RelatedProjectStart = f_text.find("Related Projects")
ObjectiveStart = f_text.find("Project Objectives")
ProductStart = f_text.find("Project Outputs")
DecisionTriggerStart = f_text.find("DECISION TRIGGER:")

#Problem: A number of objects share the 2nd level on the project and can't be easily seperated
#Solution: Nested Split statements? 

DecisionTriggers = f_text.split("DECISION TRIGGER")
Objectives = DecisionTriggers[-1].split("OBJECTIVE")
DecisionTriggers[-1] = Objectives[0]
ImplementationSteps = Objectives[-1].split("IMPLEMENTATION STEP")
Objectives[-1] = ImplementationSteps[0]

#DecisionTriggers.pop()
Objectives.pop(0)
#ImplementationSteps.pop()

Citations = ImplementationSteps[-1].split("LITERATURE CITED")
Citations = Citations[-1]
ImplementationSteps[-1] = Citations[0]

'''
print("Decision Triggers")
for item in DecisionTriggers:
    print(item+"\n\n")

print("Objectives")
for item in Objectives:
    print(item+"\n\n")

print("Implementation Steps")
for item in ImplementationSteps:
    print(item+"\n\n")
'''

WorktaskID_text = f_text[WorktaskIDstart+24:NameStart-2]
Name_text = f_text[NameStart+26:VersionDateStart-2]
VersionDate_text = f_text[VersionDateStart+18:LeadStart-2]
Lead_text = f_text[LeadStart+14:ContributorStart-2]
Contributor_text = f_text[ContributorStart+16:StatusStart-2]
Status_text = f_text[StatusStart+12:TypeStart-2]
Type_text = f_text[TypeStart+12:StartDateStart-2]
StartDate_text = f_text[StartDateStart+20:EndDateStart-2]
EndDate_text = f_text[EndDateStart+18:SummaryStart-2]
Summary_text = f_text[SummaryStart+25:BackgroundStart-2]
Background_text = f_text[BackgroundStart+20:SpeComStart-2]
SpeCom_text = f_text[SpeComStart+43:ConMeasStart-2]
ConMeas_text = f_text[ConMeasStart+34:LocationStart-2]
Location_text = f_text[LocationStart+22:GoalStart-2]
Goal_text = f_text[GoalStart+29:TriggerStart-2]
Trigger_text = f_text[TriggerStart+50:OtherConMeasStart-2]
OtherConMeas_text = f_text[OtherConMeasStart+38:OtherSpeComStart-2]
OtherSpeCom_text = f_text[OtherSpeComStart+47:RelatedProjectStart-2]
RelatedProject_text = f_text[RelatedProjectStart+63:ObjectiveStart-2]
Objective_text = f_text[ObjectiveStart+50:ProductStart-2]
Product_text = f_text[ProductStart+43:DecisionTriggerStart-4]

#print(WorktaskID_text+"\n"+Name_text+"\n"+VersionDate_text+"\n"+Lead_text+"\n"+Contributor_text+"\n"+Status_text+"\n"+Type_text+"\n"+StartDate_text+"\n"+EndDate_text+"\n"+Summary_text+"\n"+Background_text+"\n"+SpeCom_text+"\n"+ConMeas_text+"\n"+Location_text+"\n"+Goal_text+"\n"+Trigger_text+"\n"+OtherConMeas_text+"\n"+OtherSpeCom_text+"\n"+RelatedProject_text+"\n"+Objective_text+"\n"+Product_text)

StartDate_date = datetime.strptime("01/01/"+StartDate_text, '%M/%d/%Y')
EndDate_date = datetime.strptime("01/01/"+EndDate_text, '%M/%d/%Y')

SpeCom_list = SpeCom_text.split("; ")
ConMeas_list = ConMeas_text.split("; ")
Location_list = Location_text.split("; ")
Goal_list = Goal_text.split("; ")

Trigger_list = Trigger_text.split("\\n")
RelatedProject_list = RelatedProject_text.split("\\n")
Objective_list = Objective_text.split("\\n")
Product_list = Product_text.split("\\n")

project = Project(WorktaskID = WorktaskID_text, ProjectName = Name_text, ProjectLead = Lead_text, ProjectStatus = Status_text, ProjectStart = StartDate_date, ProjectEnd = EndDate_date, ProjectSummary = Summary_text, ProjectBackground = Background_text, OtherConsMeas = OtherConMeas_text, OtherSpecies = OtherSpeCom_text, Reference = Citations, ProjectContributors = Contributor_text)
project.save()

for spe_com in SpeCom_list:
    if spe_com == "n/a":
        break
    try:
        scope = SpeciesCommunity.objects.get(Acronym = spe_com)
    except:
        scope = SpeciesCommunity.objects.create(Acronym = spe_com)
    project.SpeComs.add(scope)
    project.save()
                
for con_meas in ConMeas_list:
    if con_meas == "n/a":
        break    
    try:
        conservation = ConservationMeasure.objects.get(CMCode = con_meas)
    except:
        conservation = ConservationMeasure.objects.create(CMCode = con_meas)
    project.ConMeas.add(conservation)
    project.save()    
                        
for local in Location_list:
    if local == "n/a":
        break    
    try:
        location = Location.objects.get(LocationCode = local)
    except:
        location = Location.objects.create(LocationCode = local)
    project.Locations.add(location)
    project.save() 
    
for goal in Goal_list:
    if goal == "n/a":
        break    
    try:
        goal = Goal.objects.get(GoalName = goal)
    except:
        goal = Goal.objects.create(GoalName = goal)
    project.Goals.add(goal)
    project.save()

for trigger in Trigger_list:
    new_trigger = Trigger.objects.create(ProjectID = project, TriggerName = trigger)
    new_trigger.save()   
    project.Triggers.add(new_trigger)

for related in RelatedProject_list:
    related_list = related.split("\\t")
    new_related_project = RelatedProject.objects.create(Project = project, WorktaskID = related_list[0], RelationshipType = related_list[1])
    new_related_project.save()   
    project.RelatedProjects.add(new_related_project)
    

for objective in Objective_list:
    obj_list = objective.split("\\t")
    new_objective = Objective.objects.create(ProjectID = project, ObjCode = obj_list[0], ObjName = obj_list[1])
    new_objective.save()
    project.Objectives.add(new_objective)

for product in Product_list:
    prod_list = product.split("\\t")
    new_product = Output.objects.create(ProjectID = project, OutputTitle = prod_list[0], OutputURI = prod_list[1])
    new_product.save()
    project.Outputs.add(new_product)



for decTri in DecisionTriggers:
    nameStart = decTri.find("Trigger Name")
    descriptionStart = decTri.find("Trigger Description")
    indicatorStart = decTri.find("Trigger Indicator/Value Statement")
    proResponseStart = decTri.find("Proposed Response")
    statusStart = decTri.find("Trigger Indicator Status/Trend")
    interpretationStart = decTri.find("Management Interpretation")
    mgmResponseStart = decTri.find("Management Response")
    
    Name_text = decTri[nameStart+14:descriptionStart-2]
    Description_text = decTri[descriptionStart+21:indicatorStart-2]
    Indicator_text = decTri[indicatorStart+35:proResponseStart-2]
    ProResponse_text = decTri[proResponseStart+26:statusStart-2]
    Status_text = decTri[statusStart+26:interpretationStart-2]
    Interpretation_text = decTri[interpretationStart+26:mgmResponseStart-2]
    MgmResponse_text = decTri[mgmResponseStart+26:-2]
        
    try:
        trigID = Trigger.objects.filter(ProjectID = project).get(TriggerName = Name_text)
        status = TriggerStatus.objects.create(TriggerID = trigID, StatusTrend = Status_text, MgmtInterp = Interpretation_text, MgmtResponse = MgmResponse_text)
        status.save()
        trigID.TriggerStatus.add(status)
        trigID.save()
        trigID = Trigger.objects.filter(ProjectID = project).filter(TriggerName = Name_text).update(TriggerDescription = Description_text, TriggerIndicators = Indicator_text, ProposedResponse = ProResponse_text)
    except:
        pass
    
for obj in Objectives:
    IDStart = obj.find("Objective ID")
    objNameStart = obj.find("Objective Name")
    objDescriptionStart = obj.find("Objective Description")
    startDateStart = obj.find("Objective Start Date")
    endDateStart = obj.find("Objective End Date")
    diagramStart = obj.find("Objective Work-Flow Diagram")
    milestoneStart = obj.find("Objective Milestones and Status")
    stepStart = obj.find("Implementation Steps")
    objEnd = obj.find("IMPLEMENTATION STEP")
    
    ID_text = obj[IDStart+12:objNameStart-2]
    Name_text = obj[objNameStart+16:objDescriptionStart-2]
    Description_text = obj[objDescriptionStart+23:startDateStart-2]
    StartDate_text = obj[startDateStart+21:endDateStart-2]
    EndDate_text = obj[endDateStart+20:diagramStart-2]
    Diagram_text = obj[diagramStart+29:milestoneStart-2]
    Milestone_text = obj[milestoneStart+33:stepStart-2]
    Step_text = obj[stepStart+22:objEnd-2]
    
    Milestone_list = Milestone_text.split('\\n')
    Milestone_list.pop(0)
    Step_list = Step_text.split('\\n')
    Step_list.pop(0)


    objID = Objective.objects.filter(ProjectID = project).filter(ObjName = Name_text).update(ObjDescription=Description_text, ObjFlowDiagram=Diagram_text)
    
    objActual = Objective.objects.filter(ProjectID = project).get(ObjName = Name_text)
    for mile in Milestone_list:
        mileAndProgress = mile.split('\\t')
        progressData = mileAndProgress[1].split(', ')
        mile_object = Milestone.objects.create(ObjectiveID = objActual, Description = mileAndProgress[0])
        progress_object = MilestoneProgress.objects.create(MilestoneID = mile_object, ReportingDate = datetime.strptime("01/01/"+progressData[1], '%M/%d/%Y'), Status = progressData[0])
        progress_object.save()
        mile_object.MilestoneProgress.add(progress_object)
        mile_object.save()
        objActual.Milestones.add(mile_object)

    for step in Step_list:
        stepParts = step.split('\\t')
        step_object = Step.objects.create(ObjectiveID = objActual, StepName = stepParts[1], StepCode = stepParts[0])
        step_object.save()
        objActual.Steps.add(step_object)
        
for impStep in ImplementationSteps:
    IDStart = impStep.find("Step ID")
    NameStart = impStep.find("Step Name")
    TypeStart = impStep.find("Step Type")
    SummaryStart = impStep.find("Step Summary")
    StartDateStart = impStep.find("Step Start Date")
    EndDateStart = impStep.find("Step End Date")
    MetricStart = impStep.find("Step Tracking Metrics")
    DependanciesStart = impStep.find("Step Dependencies")
    MethodStart = impStep.find("Step Methods")
    
    ID_text = impStep[IDStart+9:NameStart-2]
    Name_text = impStep[NameStart+11:TypeStart-2]
    Type_text = impStep[TypeStart+11:SummaryStart-2]
    Summary_text = impStep[SummaryStart+14:StartDateStart-2]
    StartDate_text = impStep[StartDateStart+17:EndDateStart-2]
    EndDate_text = impStep[EndDateStart+15:MetricStart-2]
    Dependencies_text = impStep[DependanciesStart+19:MethodStart-2]
    Method_text = impStep[MethodStart+14:-2]
    
    try:
        impStep_StartDate_date = datetime.strptime("01/01/"+StartDate_text, '%M/%d/%Y')
    except:
        if StartDate_text == "Same as for parent objective":
            impStep_StartDate_date = StartDate_date
        else:
            impStep_StartDate_date = '1900-01-01'
    try:
        impStep_EndDate_date = datetime.strptime("01/01/"+EndDate_text, '%M/%d/%Y')
    except:
        if EndDate_text == "Same as for parent objective":
            impStep_EndDate_date = EndDate_date
        else:
            impStep_EndDate_date = '1900-01-01'        
    
    print(ID_text+'\n'+Name_text+'\n'+Type_text)
    
    stepID = Step.objects.filter(StepName = Name_text).filter(StepCode = ID_text).update(StepType = Type_text, StepSummary = Summary_text, StepStartDate = impStep_StartDate_date, StepEndDate = impStep_EndDate_date, StepDependencies = Dependencies_text)
    
    
