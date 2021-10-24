from django.urls import path
from . import views

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.api_overview, name='api_overview'),
    path('users/', views.show_all, name='users'),
    path('users/<int:pk>/', views.view_user, name='user'),
    path('users/self/', views.view_own_user, name='view_own_profile'),
    path('register/', views.register_user, name='register'),
    path('login/', obtain_auth_token, name='login'),
    path('reviews/create/', views.register_review, name='register_review'),
    path('reviews/upvote/', views.upvote_review, name='upvote_review'),
    path('reviews/downvote/', views.downvote_review, name='downvote_review'),
    path('reviews/delete/', views.delete_review, name='delete_review'),
]
