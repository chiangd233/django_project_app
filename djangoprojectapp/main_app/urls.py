from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name = "home"),
    path('about/', views.About.as_view(), name = "about"),
    path('create/', views.Workout_Create.as_view(), name = "workout_create"),
    path('<int:pk>', views.Workout_Detail.as_view(), name = "workout_detail"),
    path('<int:pk>/update', views.Workout_Update.as_view(), name = "workout_update"),
    path('<int:pk>/delete/', views.Workout_Delete.as_view(), name = "workout_delete"),
    path('user/<username>/', views.profile, name = 'profile'),
    path('exercises/', views.Exercise_Index.as_view(), name = "exercise"),
    path('exercises/create', views.Exercise_Create.as_view(), name = "exercise_create"),
    path('exercises/delete', views.Exercise_Delete.as_view(), name = "exercise_delete"),
]