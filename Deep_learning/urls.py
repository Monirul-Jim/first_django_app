from django.urls import path
from . import views

urlpatterns = [

    path('', views.Deep_Learning, name='deep'),
]
