
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
        
        WorktaskID_text = f_text[WorktaskIDstart+31:NameStart-9]
        Name_text = f_text[NameStart+33:LeadStart-9]
        Lead_text = f_text[LeadStart+21:StatusStart-9]
        Status_text = f_text[StatusStart+21:StatusStart-9]
        StartDate_text = f_text[StartDateStart+27:EndDateStart-9]
        EndDate_text = f_text[EndDateStart+25:SummaryStart-9]
        Summary_text = f_text[SummaryStart+24:SpeComStart-9]
        SpeCom_text = f_text[SpeComStart+50:ConMeasStart-9]
        ConMeas_text = f_text[ConMeasStart+41:LocationStart-9]
        Location_text = f_text[LocationStart+29:ProductStart-399]
        Output_text = f_text[OutputStart+34:-5]
        
        
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
            product_URI = product_list[1].split("\\r\\n")
            new_output = Output.objects.create(ProjectID = project, OutputTitle = product_list[0], OutputURI = product_URI[0])
            new_output.save()   
            project.Outputs.add(new_output)
    '''for product in product_list:
    product = product.strip("\\n")'''
    
    #print(f_text)


