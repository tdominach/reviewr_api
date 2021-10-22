from django.urls import path
from . import views

urlpatterns = [
    path('businesses/<location>/', views.businesses),
    path('business/<id>/', views.business),
    path('reviews/<id>/', views.reviews),
]
