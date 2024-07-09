from django.urls import path, include
from .views import upload_file, payslip_view

urlpatterns = [
    path('list/', upload_file, name='list'),
    path('testfilepdf/', payslip_view, name='testfilepdf')
]