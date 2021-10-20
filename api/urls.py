from django.urls import path
from . import views

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.api_overview, name='api_overview'),
    path('users/', views.show_all, name='users'),
    path('users/<int:pk>/', views.view_user, name='user'),
    path('register/', views.register_user, name='register'),
    path('login/', obtain_auth_token, name='login'),
]
