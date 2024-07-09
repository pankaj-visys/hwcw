# api/urls.py
from django.urls import path
from . import views
from .views import BookList, BookDetail, CityList, GradeList, SchoolList


urlpatterns = [
    path('book/', BookList.as_view()),
    path('book/<int:pk>/', BookDetail.as_view()),

    path('city/', CityList.as_view()),
    path('grade/', GradeList.as_view()),
    path('school/', SchoolList.as_view()),

    path('city_list/', views.city_list, name='city_list'),
    path('school_list/', views.school_list, name='school_list'),
    path('grade_list/', views.grade_list, name='grade_list'),
    path('all_list/', views.all_list, name='all_list'),
    path('click_all_list/', views.click_all_list, name='click_all_list'),
    path('updateSchoolGradeGroup/', views.updateSchoolGradeGroup, name='updateSchoolGradeGroup'),
    path('updateGradeBox/', views.updateGradeBox, name='updateGradeBox'),
    path('book_List/', views.book_List, name='book_List'),
    path('decrement/', views.decrement, name='decrement'),
    path('increment/', views.increment, name='increment'),
]