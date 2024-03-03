
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def Deep_Learning(request):
    return render(request, 'deep_learn/deep_learning.html')


def registration(request):
    fm = UserCreationForm()
    return render(request, 'deep_learn/register.html', {'form': fm})
