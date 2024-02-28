from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def machine(request):
    return render(request, 'machine_learn/machine_learning.html')


def random(request):
    return render(request, "machine_learn/random_forest.html")


def K_nearest(request):
    return render(request, "machine_learn/knn.html")


def dtree(request):
    return render(request, "machine_learn/DT.html")
