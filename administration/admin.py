from django.contrib import admin
from .models import Myfiles


class MyfilesAdmin(admin.ModelAdmin):
    model = Myfiles
    list_display = ['pk', 'title', 'submitter', 'batch', 'description', 'dateOfAssignment']

# Register your models here.
admin.site.register(Myfiles, MyfilesAdmin)