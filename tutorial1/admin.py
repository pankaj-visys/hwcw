from django.contrib import admin
from .models import Work


class WorkAdmin(admin.ModelAdmin):
    model = Work
    list_display = ['pk', 'title', 'description', 'dateOfAssignment', 'submitter', 'school', 'grade', 'subject']

# Register your models here.
admin.site.register(Work, WorkAdmin)
