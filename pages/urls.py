from django.urls import path
from .views import HomePageView, AboutPageView, ServicesPageView, StatusListView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('services/', ServicesPageView.as_view(), name='services'),
    path('status-list/<int:id>', StatusListView.as_view(), name='status-list'),
]