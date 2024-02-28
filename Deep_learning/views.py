
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def Deep_Learning(request):
    return render(request,'deep_learning.html')
