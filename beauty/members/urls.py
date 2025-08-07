from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('select_gender/', views.select_gender, name='select_gender'),
    path('select_ethnicity/<str:gender>/', views.select_ethnicity, name='select_ethnicity'),
    path('compare/<str:folder>/', views.compare_faces, name='compare_faces'),
    path('compare/movies/', views.compare_movies, name='compare_movies'),
    path('compare/places/', views.compare_places, name='compare_places'),
    path('vote/', views.vote, name='vote'),
]
