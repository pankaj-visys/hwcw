# tutorial/tables.py
import django_tables2 as tables
from .models import Work

class WorkTable(tables.Table):
    
    my_extra_column = tables.Column(verbose_name='My calculated value')
    class Meta:
        model = Work
        template_name = "django_tables2/bootstrap.html"
        fields = ("description","dateOfAssignment","subject","workfile",)