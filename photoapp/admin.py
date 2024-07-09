from django.contrib import admin
from .models import Photo, Assignment


class PhotoAdmin(admin.ModelAdmin):
    model = Photo
    list_display = ['pk', 'title', 'description', 'dateOfAssignment', 'submitter', 'school', 'grade', 'subject']

# Register your models here.
admin.site.register(Photo, PhotoAdmin)

class AssignmentAdmin(admin.ModelAdmin):
    model = Assignment
    list_display = ['pk', 'title', 'description', 'dateOfAssignment']

# Register your models here.
admin.site.register(Assignment, AssignmentAdmin)