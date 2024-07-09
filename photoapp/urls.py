'''Photoapp URL patterns'''

from django.urls import path

from .views import (
    AllPhotoListView,
    MyPhotoListView,
    PhotoTagListView,
    PhotoDetailView,
    PhotoCreateView,
    PhotoUpdateView,
    PhotoDeleteView
)

app_name = 'photo'

urlpatterns = [
    path('', AllPhotoListView.as_view(), name='alllist'),
    path('mylist', MyPhotoListView.as_view(), name='mylist'),
    path('tag/<slug:tag>/', PhotoTagListView.as_view(), name='tag'),
    path('<int:pk>/', PhotoDetailView.as_view(), name='detail'),
    path('create/', PhotoCreateView.as_view(), name='create'),
    path('<int:pk>/update/', PhotoUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', PhotoDeleteView.as_view(), name='delete'),
]