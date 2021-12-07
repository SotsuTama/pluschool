from django.shortcuts import render
from django.http import HttpResponse
from .models import NgWordTb

def login(request):
    return render(request, 'pluschool/login.html')

def qTop(request):

    return render(request,'pluschool/q_and_a_top.html')


def data_test(request):
    data = NgWordTb.objects.all()
    params = {
        'title':'test',
        'data':data,
    }
    return render(request, 'pluschool/data_test.html', params)



def carender_manage(request):

    return render(request, 'pluschool/carender_manage.html')