'''Workapp URL patterns'''

from django.urls import path

from .views import (
    AllWorkListView,
    FilteredWorkListView,
    MyWorkListView,
    WorkTagListView,
    WorkDetailView,
)

app_name = 'work'

urlpatterns = [
    path('', AllWorkListView.as_view(), name='alllist'),
    path('mylist', MyWorkListView.as_view(), name='mylist'),
    path('mylist1', FilteredWorkListView.as_view(), name='mylist1'),
    path('tag/<slug:tag>/', WorkTagListView.as_view(), name='tag'),
    path('<int:pk>/', WorkDetailView.as_view(), name='detail'),
]