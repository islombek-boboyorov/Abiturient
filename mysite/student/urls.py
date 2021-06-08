from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('details/', views.details, name="courses_details"),
    path('courses/', views.courses, name="courses"),
    path('trainer/', views.trainers, name="trainer"),
    path('events/', views.events, name="events"),
    path('pricing/', views.pricing, name="pricing"),
]
