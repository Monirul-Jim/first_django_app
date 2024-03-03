from django.urls import path
from . import views

urlpatterns = [
    path('', views.data_analysis, name='data_analysis'),
    path('class/', views.DataAnalysis.as_view())
]
