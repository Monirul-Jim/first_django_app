from django.urls import path
from . import views

urlpatterns = [

    path('machine/', views.machine, name='machine_learning'),
    path('random/', views.random, name='random_number'),
    path('knn/', views.K_nearest, name='knn'),
    path('dt/', views.dtree, name='dt'),
]
