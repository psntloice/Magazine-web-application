from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#connects to the home template
def homepage(request):
    return render(request, 'magazine/home.html')

#def trialpage(request, trial-html):
    #return HttpResponse('request %s' % 'trial-html')

def aboutpage(request):
    return render(request, 'magazine/about.html')
