#AIMS Full project importing
# -*- coding: utf-8 -*-
from datetime import datetime
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AIMS.settings")
import django
django.setup()
from projects.models import *
from scopes.models import *
import re

f = open("Full_Import\LCR MSCP F10 Adaptive Management Plan DRAFT 2022-07-28.txt","rb")
f_text = str(f.readlines())

f_text = f_text.replace('\\r', '')
f_text = f_text.replace("', b'", '')
f_text = f_text.replace('\\x92','\'')
f_text = f_text.replace('\\x93','"')
f_text = f_text.replace('\\x94','"')
f_text = f_text.replace('\\x96','-')
f_text = f_text.replace('\\x97','-')
f_text = f_text.replace('\\xc4','Ä')
f_text = f_text.replace('\\xcb','Ë')
f_text = f_text.replace('\\xcf','Ï')
f_text = f_text.replace('\\xd6','Ö')
f_text = f_text.replace('\\xdc','Ü')
f_text = f_text.replace('\\xe4','ä')
f_text = f_text.replace('\\xeb','ë')
f_text = f_text.replace('\\xef','ï')
f_text = f_text.replace('\\xf6','ö')
f_text = f_text.replace('\\xfc','ü')
f_text = f_text.replace('\\xc1','Á')
f_text = f_text.replace('\\xc9','É')
f_text = f_text.replace('\\xcd','Í')
f_text = f_text.replace('\\xd3','Ó')
f_text = f_text.replace('\\xda','Ú')
f_text = f_text.replace('\\xe1','á')
f_text = f_text.replace('\\xe9','é')
f_text = f_text.replace('\\xed','í')
f_text = f_text.replace('\\xf3','ó')
f_text = f_text.replace('\\xfa','ú')
#f_text = f_text.replace('','')

#f_text = re.sub(r'[^\x00-\xff]',r'', f_text) 
#f_text = f_text.encode('ascii', errors='ignore')

#print(f_text)

WorktaskIDstart = f_text.find("Work Task ID")
NameStart = f_text.find("Project (Work Task) Name")
VersionDateStart = f_text.find("Project Plan Version Date")
LeadStart = f_text.find("Project Lead")
StatusStart = f_text.find("Project Status")
TypeStart = f_text.find("Project Type")
StartDateStart = f_text.find("Project Start Date")
EndDateStart = f_text.find("Project End Date")
SummaryStart = f_text.find("Project Summary")
BackgroundStart = f_text.find("Project Background")
ContributorStart = f_text.find("Project Plan Contributors")
SpeComStart = f_text.find("Associated Species/Communities")
ConMeasStart = f_text.find("Associated Conservation Measures")
LocationStart = f_text.find("Associated Locations")
GoalStart = f_text.find("Associated Ecological Goals")
OtherConMeasStart = f_text.find("Other Affected Conservation Measures")
OtherSpeComStart = f_text.find("Other Affected Covered and Evaluation Species")
RelatedProjectStart = f_text.find("Related Projects")
TriggerStart = f_text.find("Decision Triggers")
ObjectiveStart = f_text.find("Objectives")
ProductStart = f_text.find("Outputs")
DecisionTriggerStart = f_text.find("DECISION TRIGGER:")

#Problem: A number of objects share the 2nd level on the project and can't be easily seperated
#Solution: Nested Split statements? 

DecisionTriggers = f_text.split("DECISION TRIGGER")
Objectives = DecisionTriggers[-1].split("OBJECTIVE")
DecisionTriggers[-1] = Objectives[0]
Milestones = Objectives[-1].split("MILESTONE")
Objectives[-1] = Milestones[0]
ImplementationSteps = Milestones[-1].split("IMPLEMENTATION STEP")
Milestones[-1] = ImplementationSteps[0]
Methods = ImplementationSteps[-1].split("METHOD")
ImplementationSteps[-1] = Methods[0]
Protocols = Methods[-1].split("PROTOCOL")
Methods[-1] = Protocols[0]
Outputs = Protocols[-1].split("OUTPUT")
Protocols[-1] = Outputs[0]

DecisionTriggers.pop(0)
Objectives.pop(0)
Milestones.pop(0)
ImplementationSteps.pop(0)
Methods.pop(0)
Protocols.pop(0)
Outputs.pop(0)

try:
    Citations = Outputs[-1].split("LITERATURE CITED")
except:
    Citations = ImplementationSteps[-1].split("LITERATURE CITED")
Citations = Citations[-1]
Citations = Citations[2:-2]
Citations = Citations.replace('\\n','\n')
#Outputs[-1] = Citations[0]

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
    
print("Methods")
for item in Methods:
    print(item+"\n\n")

print("Protocols")
for item in Protocols:
    print(item+"\n\n")

print("Outputs")
for item in Outputs:
    print(item+"\n\n")
'''

WorktaskID_text = f_text[WorktaskIDstart+14:NameStart-2]
Name_text = f_text[NameStart+26:VersionDateStart-2]
VersionDate_text = f_text[VersionDateStart+18:LeadStart-2]
Lead_text = f_text[LeadStart+14:StatusStart-2]
Status_text = f_text[StatusStart+12:TypeStart-2]
Type_text = f_text[TypeStart+12:StartDateStart-2]
StartDate_text = f_text[StartDateStart+20:EndDateStart-2]
EndDate_text = f_text[EndDateStart+18:SummaryStart-2]
Summary_text = f_text[SummaryStart+25:BackgroundStart-2]
Background_text = f_text[BackgroundStart+20:ContributorStart-2]
Contributor_text = f_text[ContributorStart+16:SpeComStart-2]
SpeCom_text = f_text[SpeComStart+43:ConMeasStart-2]
ConMeas_text = f_text[ConMeasStart+34:LocationStart-2]
Location_text = f_text[LocationStart+22:GoalStart-2]
Goal_text = f_text[GoalStart+29:OtherConMeasStart-2]
OtherConMeas_text = f_text[OtherConMeasStart+38:OtherSpeComStart-2]
OtherSpeCom_text = f_text[OtherSpeComStart+47:RelatedProjectStart-2]
RelatedProject_text = f_text[RelatedProjectStart+59:TriggerStart-2] #changed
Trigger_text = f_text[TriggerStart+51:ObjectiveStart-2]
Objective_text = f_text[ObjectiveStart+44:ProductStart-2]
Product_text = f_text[ProductStart+48:DecisionTriggerStart-4]

Summary_text = Summary_text.replace('\\n','\n')
Background_text = Background_text.replace('\\n','\n')

#print(SpeCom_text+'\n\n'+ConMeas_text+'\n\n'+Location_text+'\n\n'+Goal_text+'\n\n'+Trigger_text+'\n\n'+OtherConMeas_text+'\n\n'+OtherSpeCom_text+"\n"+RelatedProject_text+"\n"+Objective_text+"\n"+Product_text)

#print(WorktaskID_text+"\n"+Name_text+"\n"+VersionDate_text+"\n"+Lead_text+"\n"+Contributor_text+"\n"+Status_text+"\n"+Type_text+"\n"+StartDate_text+"\n"+EndDate_text+"\n"+Summary_text+"\n"+Background_text+"\n"+SpeCom_text+"\n"+ConMeas_text+"\n"+Location_text+"\n"+Goal_text+"\n"+Trigger_text+"\n"+OtherConMeas_text+"\n"+OtherSpeCom_text+"\n"+RelatedProject_text+"\n"+Objective_text+"\n"+Product_text)
try:
    StartDate_date = datetime.strptime("01/01/"+StartDate_text, '%M/%d/%Y')
except:
    StartDate_date = '1900-01-01'
    
try:
    EndDate_date = datetime.strptime("01/01/"+EndDate_text, '%M/%d/%Y')
except:
    EndDate_date = '1901-01-01'
    
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
  
#print(Location_list)

for local in Location_list:
    if local == "n/a":
        break    
    try:
        location = Location.objects.get(LocationCode = local)
    except:
        location = Location.objects.create(LocationCode = local)
    project.Locations.add(location)
    project.save() 
  
#print(Goal_list)
 
for goal in Goal_list:
    if goal == "n/a":
        break    
    try:
        goal = Goal.objects.get(GoalName = goal)
    except:
        goal = Goal.objects.create(GoalName = goal)
    project.Goals.add(goal)
    project.save()

#print(Trigger_list)

for trigger in Trigger_list:
    if trigger == "n/a" or trigger == "\\t":
        break      
    trig_list = trigger.split("\\t")
    new_trigger = Trigger.objects.create(ProjectID = project, TriggerName = trigger)
    new_trigger.save()   
    project.Triggers.add(new_trigger)

#print(RelatedProject_list)

for related in RelatedProject_list:
    if related == "n/a":
        break      
    related_list = related.split("\\t")
    new_related_project = RelatedProject.objects.create(Project = project, WorktaskID = related_list[0], RelationshipType = related_list[1])
    new_related_project.save()   
    project.RelatedProjects.add(new_related_project)
    
#print(Objective_list)
    
for objective in Objective_list:
    if objective == "n/a":
        break      
    obj_list = objective.split("\\t")
    new_objective = Objective.objects.create(ProjectID = project, ObjCode = obj_list[0], ObjName = obj_list[1])
    new_objective.save()
    project.Objectives.add(new_objective)

#print(Product_list)

for product in Product_list:
    if product == "n/a":
        break        
    prod_list = product.split("\\t")
    print(prod_list)
    new_product = Output.objects.create(ProjectID = project, OutputTitle = prod_list[1], OutputURI = prod_list[2])
    new_product.save()
    project.Outputs.add(new_product)



for decTri in DecisionTriggers:
    nameStart = decTri.find("Trigger Name")
    descriptionStart = decTri.find("Trigger Description")
    indicatorStart = decTri.find("Trigger Indicator(s)")
    proResponseStart = decTri.find("Proposed Response")
    repDate = decTri.find("Trigger Status Reporting Date")#NEW
    statusStart = decTri.find("Trigger Indicator Status/Trend")
    interpretationStart = decTri.find("Management Interpretation")
    mgmResponseStart = decTri.find("Management Response")
    
    Name_text = decTri[nameStart+14:descriptionStart-2]
    Description_text = decTri[descriptionStart+21:indicatorStart-2]
    Indicator_text = decTri[indicatorStart+20:proResponseStart-2] #changed
    ProResponse_text = decTri[proResponseStart+19:statusStart-2] #changed
    Status_text = decTri[statusStart+30:interpretationStart-2]
    Interpretation_text = decTri[interpretationStart+27:mgmResponseStart-2]
    MgmResponse_text = decTri[mgmResponseStart+26:-2]
    
    Description_text = Description_text.replace('\\n','\n')
    Indicator_text = Indicator_text.replace('\\n','\n')
    Indicator_text = Indicator_text.replace('\\n','\n')
    Status_text = Status_text.replace('\\n','\n')
    Interpretation_text = Interpretation_text.replace('\\n','\n')
    MgmResponse_text = MgmResponse_text.replace('\\n','\n')
    
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
    IDStart = obj.find("Objective Code")
    objNameStart = obj.find("Objective Name")
    objDescriptionStart = obj.find("Objective Description")
    startDateStart = obj.find("Objective Start Date")
    endDateStart = obj.find("Objective End Date")
    diagramStart = obj.find("Objective Work-Flow Diagram")
    milestoneStart = obj.find("Milestones")
    stepStart = obj.find("Implementation Steps")
    objEnd = obj.find("IMPLEMENTATION STEP")
    
    ID_text = obj[IDStart+12:objNameStart-2]
    Name_text = obj[objNameStart+16:objDescriptionStart-2]
    Description_text = obj[objDescriptionStart+23:startDateStart-2]
    StartDate_text = obj[startDateStart:endDateStart-2]             #changed
    EndDate_text = obj[endDateStart:diagramStart-2]                 #changed
    Diagram_text = obj[diagramStart+29:milestoneStart-2]
    Milestone_text = obj[milestoneStart+33:stepStart-2]
    Step_text = obj[stepStart+22:objEnd-3]
    
    Milestone_list = Milestone_text.split('\\n')
    Milestone_list.pop(0)
    Step_list = Step_text.split('\\n')
    Step_list.pop(0)

    Description_text = Description_text.replace('\\n','\n')

    try:
        objID = Objective.objects.filter(ProjectID = project).filter(ObjName = Name_text).update(ObjDescription=Description_text, ObjFlowDiagram=Diagram_text)
        objActual = Objective.objects.filter(ProjectID = project).get(ObjName = Name_text)
    except:
        pass
    
    for mile in Milestone_list:
        try:
            mileAndProgress = mile.split('\\t')
            progressData = mileAndProgress[1].split(', ')
            mile_object = Milestone.objects.create(ObjectiveID = objActual, MilestoneID = mileAndProgress[0], MilestoneName = mileAndProgress[1])
            '''progress_object = MilestoneProgress.objects.create(MilestoneID = mile_object, ReportingDate = datetime.strptime("01/01/"+progressData[1], '%M/%d/%Y'), Status = progressData[0])
            progress_object.save()
            mile_object.MilestoneProgress.add(progress_object)'''
            mile_object.save()
            objActual.Milestones.add(mile_object)
        except:
            pass

    for step in Step_list:
        try:
            stepParts = step.split('\\t')
            step_object = Step.objects.create(ObjectiveID = objActual, StepName = stepParts[1], StepCode = stepParts[0])
            step_object.save()
            objActual.Steps.add(step_object)
        except:
            pass

for mile in Milestones:
    IDstart = mile.find("Milestone ID")
    NameStart = mile.find("Milestone Name")
    DescriptionStart = mile.find("Milestone Description")
    ProgressReportingDateStart = mile.find("Milestone Progress Reporting Date")
    ProgressStatusStart = mile.find("Milestone Progress Status")
    ProgressDescriptionStart = mile.find("Milestone Progress Description")

    ID_text = mile[IDstart+14:NameStart-2]
    Name_text = mile[NameStart+14:DescriptionStart-2]
    Description_text = mile[DescriptionStart+21:ProgressReportingDateStart-2]
    ProgressReportingDate_text = mile[ProgressReportingDateStart+33:ProgressStatusStart-2]
    ProgressStatus_text = mile[ProgressStatusStart+27:ProgressDescriptionStart-2] #changed
    ProgressDescription_text = mile[ProgressDescriptionStart+30:-2]
    
    Description_text = Description_text.replace('\\n','\n')
    ProgressDescription_text = ProgressDescription_text.replace('\\n','\n')
    
    try:
        progressDate = datetime.strptime("01/01/"+ProgressReportingDate_text, '%M/%d/%Y')
    except:
        progressDate = '1900-01-01'
  
    try:
        mileID = Milestone.objects.filter(MilestoneID = ID_text).update(Description=Description_text)
        mileActual = Milestone.objects.get(MilestoneID = ID_text)
        progress_object = MilestoneProgress.objects.create(MilestoneID = mileActual, ReportingDate = progressDate, Status = ProgressStatus_text, Description = ProgressDescription_text)
        progress_object.save()
        mileActual.MilestoneProgress.add(progress_object)
    except:
        pass
    
for impStep in ImplementationSteps:
    IDStart = impStep.find("Step Code")
    NameStart = impStep.find("Step Name")
    SummaryStart = impStep.find("Step Summary")
    TypeStart = impStep.find("Step Type")
    StartDateStart = impStep.find("Step Start Date")
    EndDateStart = impStep.find("Step End Date")
    #MetricStart = impStep.find("Step Tracking Metrics")
    DependanciesStart = impStep.find("Step Dependencies")
    MethodStart = impStep.find("Step Methods")
    
    ID_text = impStep[IDStart+11:NameStart-2]
    Name_text = impStep[NameStart+11:SummaryStart-2]
    Summary_text = impStep[SummaryStart+14:TypeStart-2]
    Type_text = impStep[TypeStart+11:StartDateStart-2]
    StartDate_text = impStep[StartDateStart+17:EndDateStart-2]
    EndDate_text = impStep[EndDateStart+15:DependanciesStart-2]
    Dependencies_text = impStep[DependanciesStart+19:MethodStart-2]
    Method_text = impStep[MethodStart+14:-2]
    
    Summary_text = Summary_text.replace('\\n','\n')
    Dependencies_text = Dependencies_text.replace('\\n','\n')
    
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
    

    Method_list = Method_text.split('\\n')
    Method_list.pop(0)
    
    try:
        stepID = Step.objects.filter(StepName = Name_text).filter(StepCode = ID_text).update(StepType = Type_text, StepSummary = Summary_text, StepStartDate = impStep_StartDate_date, StepEndDate = impStep_EndDate_date, StepDependencies = Dependencies_text)
        stepActual = Step.objects.get(StepCode = ID_text)
    except:
        pass
    
    try:
        for method in Method_list:
            method_parts = method.split('\\t')
            method_object = Method.objects.create(StepID = stepActual, MethodTitle = method_parts[1], MethodCode = method_parts[0])
            method_object.save()
            stepActual.Methods.add(method_object)
    except:
        pass
    
for method in Methods:
    MethodCodeStart = method.find("Method Code")
    MethodTitleStart = method.find("Method Title")
    MethodTypeStart = method.find("Method Type")
    MethodDateStart = method.find("Method Date")
    MethodVersionStart = method.find("Method Version")
    MethodDescriptionStart = method.find("Method Description")
    MethodProtocolsStart = method.find("Method Protocols")
    MethodContactStart = method.find("Method Contact")
    
    MethodCode_text = method[MethodCodeStart+13:MethodTitleStart-2]
    MethodTitle_text = method[MethodTitleStart+14:MethodTypeStart-2]
    MethodType_text = method[MethodTypeStart+13:MethodDateStart-2]
    MethodDate_text = method[MethodDateStart+13:MethodVersionStart-2]
    MethodVersion_text = method[MethodVersionStart+16:MethodDescriptionStart-2]
    MethodDescription_text = method[MethodDescriptionStart+20:MethodProtocolsStart-2]
    MethodProtocols_text = method[MethodProtocolsStart+18:MethodContactStart-2]
    MethodContact_text = method[MethodContactStart+16:-4] #changed   

    Protocol_list = MethodProtocols_text.split("\\n")
    Protocol_list.pop(0)
    #print(Protocol_list)
    
    MethodDescription_text = MethodDescription_text.replace('\\n','\n')
    
    Method_date = datetime.strptime("01-"+MethodDate_text, '%d-%M-%Y')
    try:
        Method_date = datetime.strptime("01-"+MethodDate_text, '%d-%M-%Y')
    except:
        Method_date = '1900-01-01'

    try:
        methodID = Method.objects.filter(MethodCode = MethodCode_text).filter(MethodTitle = MethodTitle_text).update(MethodType = MethodType_text, MethodDate = Method_date, MethodVersion = MethodVersion_text, MethodDescription = MethodDescription_text, MethodContact = MethodContact_text,)
        methodActual = Method.objects.get(MethodCode = MethodCode_text)
    except:
        pass

    for protocol in Protocol_list:
        protocol_parts = protocol.split('\\t')
        protocol_object = Protocol.objects.create(MethodID=methodActual, ProtocolTitle=protocol_parts[1], ProtocolCode=protocol_parts[0],)
        protocol_object.save()
        methodActual.Protocols.add(protocol_object)

for protocol in Protocols:
    ProtocolCodeStart = protocol.find("Protocol Code")
    ProtocolTitleStart = protocol.find("Protocol Title")
    ProtocolVersionStart = protocol.find("Protocol Version")
    ProtocolDateStart = protocol.find("Protocol Date")
    ProtocolAuthorsStart = protocol.find("Protocol Authors")
    ProtocolDescriptionStart = protocol.find("Protocol Description")
    ProtocolURLStart = protocol.find("Protocol URL")
    
    ProtocolCode_text = protocol[ProtocolCodeStart+15:ProtocolTitleStart-2]
    ProtocolTitle_text = protocol[ProtocolTitleStart+16:ProtocolVersionStart-2]
    ProtocolVersion_text = protocol[ProtocolVersionStart+18:ProtocolDateStart-2]
    ProtocolDate_text = protocol[ProtocolDateStart+15:ProtocolAuthorsStart-2]
    ProtocolAuthors_text = protocol[ProtocolAuthorsStart+18:ProtocolDescriptionStart-2]
    ProtocolDescription_text = protocol[ProtocolDescriptionStart+22:ProtocolURLStart-2]
    ProtocolURL_text = protocol[ProtocolURLStart+14:-2]
    
    ProtocolDescription_text = ProtocolDescription_text.replace('\\n','\n')
    
    Protocol_date = datetime.strptime("01-"+ProtocolDate_text, '%d-%M-%Y')
    #print(ProtocolCode_text+'\n'+ProtocolTitle_text+'\n'+ProtocolVersion_text+'\n'+ProtocolDate_text+'\n'+ProtocolAuthors_text+'\n'+ProtocolDescription_text+'\n'+ProtocolURL_text)

    protocolID = Protocol.objects.filter(ProtocolTitle=ProtocolTitle_text).filter(ProtocolCode=ProtocolCode_text).update(ProtocolCode = ProtocolCode_text, ProtocolTitle = ProtocolTitle_text, ProtocolVerision = ProtocolVersion_text, ProtocolDate = Protocol_date, ProtocolAuthor = ProtocolAuthors_text, ProtocolDescription = ProtocolDescription_text, ProtocolLink = ProtocolURL_text,)

for output in Outputs:
    OutputCodeStart = output.find("Output Code")
    OutputTypeStart = output.find("Output Type")
    OutputAuthorsStart = output.find("Output Authors")
    OutputDateStart = output.find("Output Date")
    OutputTitleStart = output.find("Output Title")
    OutputVersionStart = output.find("Output Version")
    OutputDescriptionStart = output.find("Output Description")
    OutputDOIStart = output.find("Output DOI")
    OutputCitationStart = output.find("Output Citation")
    OutputURLStart = output.find("Output URL")
    OutputConstraintsStart = output.find("Output Constraints")
    
    OutputCode_text = output[OutputCodeStart+13:OutputTypeStart-2]
    OutputType_text = output[OutputTypeStart+13:OutputAuthorsStart-2]
    OutputAuthors_text = output[OutputAuthorsStart+16:OutputDateStart-2]
    OutputDate_text = output[OutputDateStart+13:OutputTitleStart-2]
    OutputTitle_text = output[OutputTitleStart+14:OutputVersionStart-2]
    OutputVersion_text = output[OutputVersionStart+16:OutputDescriptionStart-2]
    OutputDescription_text = output[OutputDescriptionStart+20:OutputDOIStart-2]
    OutputDOI_text = output[OutputDOIStart+12:OutputCitationStart-2]
    OutputCitation_text = output[OutputCitationStart+17:OutputURLStart-2]
    OutputURL_text = output[OutputURLStart+12:OutputConstraintsStart-2]
    OutputConstraints_text = output[OutputConstraintsStart+20:-2]
    
    OutputDescription_text = OutputDescription_text.replace('\\n','\n')
    OutputCitation_text = OutputCitation_text.replace('\\n','\n')
    OutputCitation_text = OutputCitation_text.replace('\\n','\n')
    OutputConstraints_text = OutputConstraints_text.replace('\\n','\n')
    
    #print(OutputCode_text+'\n'+OutputType_text+'\n'+OutputAuthors_text+'\n'+OutputDate_text+'\n'+OutputTitle_text+'\n'+OutputVersion_text+'\n'+OutputDescription_text+'\n'+OutputDOI_text+'\n'+OutputCitation_text+'\n'+OutputURL_text+'\n'+OutputConstraints_text)
    try:
        outputDate = datetime.strptime("01-"+OutputDate_text, '%d-%M-%Y')
    except:
        outputDate = '1900-01-01'
        
    outputFileName = OutputURL_text.split('/')[-1]
    
    outputID = Output.objects.filter(OutputURI=outputFileName).filter(OutputTitle=OutputTitle_text).update(OutputType=OutputType_text,OutputAuthors=OutputAuthors_text,OutputDate=outputDate,OutputTitle=OutputTitle_text,OutputVersion=OutputVersion_text,OutputDescription=OutputDescription_text,OutputDOI=OutputDOI_text,OutputCitation=OutputCitation_text,OutputURI=OutputURL_text,OutputConstraints=OutputConstraints_text)
    
    outputA = Output.objects.filter(OutputURI=outputFileName)
    outputB = Output.objects.filter(OutputTitle=OutputTitle_text)