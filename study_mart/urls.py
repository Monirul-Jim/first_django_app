"""
URL configuration for study_mart project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from machine_learning import views
# this also can be doing
# from machine_learning.views import machine
# from machine_learning.views import deep_learning
# from Blogs import views as b
# from Deep_learning import views as dpl
# from Data_analysis import views as dta
# from About_us import views as about
urlpatterns = [
    path('admin/', admin.site.urls),
    path('ml/', include('machine_learning.urls')),
    path('about/', include('About_us.urls')),
    path('blog/', include('Blogs.urls')),
    path('data_ana/', include('Data_analysis.urls')),
    path('deep/', include('Deep_learning.urls')),

]
