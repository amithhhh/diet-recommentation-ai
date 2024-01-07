from django.http import HttpResponse
from django.shortcuts import render
from recommentation import prediction


def home(request):
    age = 28
    h = 2
    w = 120
    a = 1.5
    ans = prediction(age,w,h,a)
    return render(request,'index.html',{'ans':ans})

