from django.shortcuts import render
from .models import Status 

# Create your views here.
from django.views.generic import TemplateView, ListView

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView): # new
    template_name = 'about.html'

class ServicesPageView(TemplateView): # new
    template_name = 'services.html'

class StatusListView(ListView): # new
    model = Status
    template_name = 'status_list.html'