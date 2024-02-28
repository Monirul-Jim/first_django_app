from django.urls import path
from . import views

urlpatterns = [
    path('a/', views.About_us,),
]
