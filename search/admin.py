from django.contrib import admin
from .models import Case, Tblcasesummary, Ltdrawdata, Tblescalation, Tblinstallbase, Tblltdreport, Tblpoa, Tblltdreason, Tblsystemfaultfix
# from .models import *

class CaseAdmin(admin.ModelAdmin):
    list_display = ('user', 'entry_date', 'case_number', 'utid', 'system')



class TblescalationAdmin(admin.ModelAdmin):
    list_display = ('case_id', 'entry_date', 'case_description', 'utid')

class TblinstallbaseAdmin(admin.ModelAdmin):
    list_display = ('utid', 'fab', 'install_start')




admin.site.register(Case, CaseAdmin)
admin.site.register(Tblescalation, TblescalationAdmin)
admin.site.register(Tblinstallbase, TblinstallbaseAdmin)
