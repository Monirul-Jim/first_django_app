from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.


def data_analysis(request):
    return render(request, 'data_analysises/data_analysis.html')


class DataAnalysis(View):
    def get(self, request):
        return render(request, 'data_analysises/class.html')
