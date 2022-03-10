
#AIMS Mini project importing
from datetime import datetime
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AIMS.settings")
import django
django.setup()
from projects.models import *
from scopes.models import *

directory = "Stub_Imports"

for filename in os.listdir(directory):
    file_dir = os.path.join(directory, filename)
    if os.path.isfile(file_dir):
        print(file_dir)
        
        f = open(file_dir,"rb")
        f_text = str(f.readlines())

        WorktaskIDstart = f_text.find("Project (Work Task) ID")
        NameStart = f_text.find("Project (Work Task) Name")
        LeadStart = f_text.find("Project Lead")
        StatusStart = f_text.find("Project Status")
        StartDateStart = f_text.find("Project Start Date")
        EndDateStart = f_text.find("Project End Date")
        SummaryStart = f_text.find("Project Summary")
        SpeComStart = f_text.find("Associated Species and Cover Type Targets")
        ConMeasStart = f_text.find("Associated Conservation Measures")
        LocationStart = f_text.find("Associated Locations")
        ProductStart = f_text.find("Project Outputs")
        OutputStart = f_text.find("'Output Title")
        
        WorktaskID_text = f_text[WorktaskIDstart+28:NameStart-6]
        Name_text = f_text[NameStart+30:LeadStart-6]
        Lead_text = f_text[LeadStart+18:StatusStart-6]
        Status_text = f_text[StatusStart+18:StatusStart-6]
        StartDate_text = f_text[StartDateStart+24:EndDateStart-6]
        EndDate_text = f_text[EndDateStart+22:SummaryStart-6]
        Summary_text = f_text[SummaryStart+21:SpeComStart-6]
        SpeCom_text = f_text[SpeComStart+47:ConMeasStart-6]
        ConMeas_text = f_text[ConMeasStart+38:LocationStart-6]
        Location_text = f_text[LocationStart+26:ProductStart-396]
        Output_text = f_text[OutputStart+31:-2]
        
        
        StartDate_date = datetime.strptime("01/01/"+StartDate_text, '%M/%d/%Y')
        EndDate_date = datetime.strptime("01/01/"+EndDate_text, '%M/%d/%Y')

        SpeCom_list = SpeCom_text.split("; ")
        ConMeas_list = ConMeas_text.split("; ")
        Location_list = Location_text.split("; ")
        Output_list = Output_text.split("', '")
        
        for output in Output_list:
            product_list = output.split("\\t")
            for product in product_list:
                product = product.strip("\\n")


        project = Project(WorktaskID = WorktaskID_text, ProjectName = Name_text, ProjectLead = Lead_text, ProjectStatus = Status_text, ProjectStart = StartDate_date, ProjectEnd = EndDate_date, ProjectSummary = Summary_text)
        project.save()
                
        for spe_com in SpeCom_list:
            try:
                scope = SpeciesCommunity.objects.get(Acronym = spe_com)
            except:
                scope = SpeciesCommunity.objects.create(Acronym = spe_com)
            project.SpeComs.add(scope)
            project.save()
                        
        for con_meas in ConMeas_list:
            try:
                conservation = ConservationMeasure.objects.get(CMCode = con_meas)
            except:
                conservation = ConservationMeasure.objects.create(CMCode = con_meas)
            project.ConMeas.add(conservation)
            project.save()    
                                
        for local in Location_list:
            try:
                location = Location.objects.get(LocationCode = local)
            except:
                location = Location.objects.create(LocationCode = local)
            project.Locations.add(location)
            project.save()    
                                        
        for output in Output_list:
            product_list = output.split("\\t")
            new_output = Output.objects.create(ProjectID = project, OutputTitle = product_list[0], OutputURI = product_list[1])
            new_output.save()   
            project.Outputs.add(new_output)
    '''for product in product_list:
    product = product.strip("\\n")'''
    
    #print(f_text)


