from django.contrib import admin

# Register your models here.

from .models import *
from .forms import *


# class ComputerAdmin(admin.ModelAdmin):
# 	list_display = ["computer_name", "IP_address", "users_name", "MAC_address", "purchase_date", "timestamp"]
# 	form = ClinicalForm
# 	list_filter = ['computer_name', 'IP_address']
# 	search_fields = ['computer_name', 'IP_address','MAC_address']













 
# admin.site.register(Computer)
admin.site.register(Clinical)
admin.site.register(Quarter)
admin.site.register(DiseaseReport)
admin.site.register(Region)
admin.site.register(Species)
admin.site.register(Localty)
admin.site.register(PrincipalSign)
admin.site.register(ClinicalDiagnosis)
admin.site.register(DiseaseCode)
admin.site.register(ControlMeasures)
admin.site.register(VaccinationHistory)
admin.site.register(SampleType)
admin.site.register(Approver)