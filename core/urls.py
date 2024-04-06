from django.urls import path
from . import views


urlpatterns = [
    path('search/', views.search, name='search'),
    path('', views.watchlist, name='home'),
    path('watchlist/', views.watchlist, name='watchlist'),
    path('add_show/<int:id>/', views.add_show, name='add_show'),
    
]