from django.contrib import admin
from .models import Status
from django.contrib.auth.admin import UserAdmin



# Register your models here.
class StatusAdmin(admin.ModelAdmin):
    model = Status
    list_display = ['pk', 'statusText', 'statusDate', 'statusClient']

admin.site.register(Status, StatusAdmin)