from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Exam
# Register your models here.

class ExamAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display =('id','department','role','topic','question','answeroption','a','b','c','d')
    search_fields =['department','topic']
admin.site.register(Exam,ExamAdmin)