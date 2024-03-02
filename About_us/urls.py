from django.urls import path
from . import views

urlpatterns = [
    path('a/', views.About_us, name='about'),
    path('t/', views.teachers_info)
]
