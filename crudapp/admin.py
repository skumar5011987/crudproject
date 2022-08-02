from django.contrib import admin
from .models import Employee
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name','role','email']

admin.site.register(Employee,EmployeeAdmin)