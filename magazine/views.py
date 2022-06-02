from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def homepage(request):
    return render(request, 'magazine/home.html')

#def trialpage(request, trial-html):
    #return HttpResponse('request %s' % 'trial-html')

def betterpage(request):
    return HttpResponse('Hi good to see you')
