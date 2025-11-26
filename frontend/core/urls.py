from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_view, name='landing'),
    path('auth/', views.auth_view, name='auth'),
    path('home/', views.home_view, name='home'),
    path('generate/', views.input_view, name='input'),        # <--- Matches 'input'
    path('dashboard/', views.dashboard_view, name='dashboard'), # <--- Matches 'dashboard'
]