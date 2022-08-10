from django.urls import path

 

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile_list, name='profile_list'),
    path('profile/create/', views.profile_create, name='profile_create'),
    path('watch/<str:pk>/', views.watch, name='watch'),
    path('movie/detail/<str:pk>/', views.show_movie_detail, name='show_movie_detail'),
    path('movie/play/<str:pk>/', views.show_movie, name='show_movie'),
]   