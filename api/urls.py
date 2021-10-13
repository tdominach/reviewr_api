from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='apiOverview'),
    path('users/', views.ShowAll, name='users'),
    path('users/<int:pk>/', views.viewUser, name='user'),
    path('register/', views.registerUser, name='user registration'),

]
