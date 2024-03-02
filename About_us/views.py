from django.shortcuts import render
from django.http import HttpResponse
from About_us.models import Teacher
# Create your views here.


def About_us(request):
    return render(request, 'about/about.html')


def teachers_info(request):
    teach = Teacher.objects.all()
    return render(request,'about/t.html',{'thr':teach} )
