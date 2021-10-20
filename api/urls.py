from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview, name='api_overview'),
    path('users/', views.show_all, name='users'),
    path('users/<int:pk>/', views.view_user, name='user'),
    path('register/', views.register_user, name='register'),
]
