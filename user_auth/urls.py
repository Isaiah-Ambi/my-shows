from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

# from django.conf import settings

urlpatterns = [
    path('register/', views.registration_view, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
]