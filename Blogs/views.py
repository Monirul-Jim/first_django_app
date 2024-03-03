from django.http import HttpResponse
from django.shortcuts import render
from Blogs.forms import TeachersRegistration

# Create your views here.


def blog1(request):
    return render(request, 'blogs/blogs.html')


def showFormsData(request):
    if request.method == 'POST':
        fm = TeachersRegistration(request.POST)
        if fm.is_valid():
            print(fm.cleaned_data['password'])
            print(fm.cleaned_data['re_password'])
    else:
        fm = TeachersRegistration()
        print('this is get statement')
    # fm.order_fields(field_order=['email', 'last_name', 'first_name'])
    return render(request, 'blogs/forms.html', {'form': fm})
