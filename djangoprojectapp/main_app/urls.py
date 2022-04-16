from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name = "home"),
    path('about/', views.About.as_view(), name = "about"),
    path('create/', views.Workout_Create.as_view(), name = "workout_create"),
    path('<int:pk>', views.Workout_Detail.as_view(), name = "workout_detail"),
    path('<int:pk>/update', views.Workout_Update.as_view(), name = "workout_update"),
]