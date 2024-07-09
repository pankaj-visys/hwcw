'''Works app generic views'''

from django import forms
from django.shortcuts import get_object_or_404, HttpResponse, Http404
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from . import views
from django.views import View
from .pdfcreator import renderPdf
from django_tables2 import SingleTableView, SingleTableMixin


from django_filters.views import FilterView
from django_filters import FilterSet, CharFilter, ChoiceFilter, DateFilter


from .models import Work
from .tables import WorkTable

SCHOOL_CHOICES = (
    ('lmc','LMC'),
    ('sfc', 'SFC'),
    ('cms','CMS'),
    ('mbic','MBIC'),
)

GRADE_CHOICES = (
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
    ('6','6'),
    ('7','7'),
    ('8','8'),
    ('9','9'),
    ('10','10'),
    ('11','11'),
    ('12','12'),
)

SUBJECT_CHOICES = (
    ('English','Eng'),
    ('Hindi','Hin'),
    ('Mathematics','Maths'),
    ('Computer','Comp'),
)

class DateInput(forms.DateInput):
    input_type = 'date'

class WorkFilter(FilterSet):
    subject = ChoiceFilter(choices=SUBJECT_CHOICES)
    grade = ChoiceFilter(choices=GRADE_CHOICES, empty_label=None)
    school = ChoiceFilter(choices=SCHOOL_CHOICES, empty_label=None)
    dateOfAssignment = DateFilter(widget=DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Work
        fields = {"dateOfAssignment": ["exact"], "school": ["exact"], "grade": ["exact"], "subject": ["exact"],}

class FilteredWorkListView(SingleTableMixin, FilterView):
    table_class = WorkTable
    model = Work
    template_name = "tutorial1/mylist.html"
    filterset_class = WorkFilter


class AllWorkListView(SingleTableView):
    model = Work
    table_class = WorkTable
    template_name = 'tutorial1/alllist.html'
    # context_object_name = 'photos'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['works'] = Work.objects.all()
        
        print("context", context)
        return context
    
class MyWorkListView(SingleTableView):
    model = Work     
    table_class = WorkTable
    template_name = 'tutorial1/mylist.html'
    # context_object_name = 'photos'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['works'] = Work.objects.all().filter(submitter=self.request.user)
        print("context", context)
        return context


class WorkTagListView(AllWorkListView): 
    template_name = 'tutorial1/taglist.html'
    # Custom function
    def get_tag(self):
        return self.kwargs.get('tag')
    def get_queryset(self):
        return self.model.objects.filter(tags__slug=self.get_tag())
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tag"] = self.get_tag()
        return context
     

class WorkDetailView(DetailView):
    model = Work
    template_name = 'tutorial1/detail.html'
    context_object_name = 'work'