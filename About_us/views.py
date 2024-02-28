from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def About_us(request):
    return render(request,'about.html')
