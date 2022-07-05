from django.contrib import admin

# Register your models here.
from .models import NewAppSalary, HrEmployee

class ModelAdminHrEmployee(admin.ModelAdmin):
    fields = ['rf_id','emp_firstname','emp_title','emp_active']
    list_display = ['emp_firstname', 'emp_title', 'rf_id' ]

admin.site.register(HrEmployee, ModelAdminHrEmployee)

class ModelAdminAppSalary(admin.ModelAdmin):
    list_display = ("employee_full_name", "salary_amount",)
    # list_editable = ("salary",)
    search_fields = ['employee__emp_firstname','employee__emp_lastname' ]

    def salary_amount(self, obj):
        return '%.2f BDT' % obj.salary

admin.site.register(NewAppSalary,ModelAdminAppSalary)