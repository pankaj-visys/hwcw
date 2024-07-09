from django.urls import path
from .views import logout_view, SignupPageView

urlpatterns = [
    path('logout/', logout_view, name='logout'),
    path('signup/', SignupPageView.as_view(), name='signup'),
]
