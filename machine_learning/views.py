from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def machine(request):
    course = 'machine learning'
    TClass = 21
    seat = 20
    duration = '2.5 month'
    offering = {'c': course, 'tl': TClass, 'st': seat, 'cd': duration}
    return render(request, 'machine_learn/machine_learning.html', context=offering)


def random(request):
    return render(request, "machine_learn/random_forest.html")


def K_nearest(request):
    return render(request, "machine_learn/knn.html")


def dtree(request):
    return render(request, "machine_learn/DT.html")
