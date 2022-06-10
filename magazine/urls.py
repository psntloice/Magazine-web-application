#created urls file to add url config for the magazine app

from django.urls import path

from . import views

urlpatterns =[
    path('',views.homepage,name = 'home'),
    path('about/',views.aboutpage,name = 'about'),
]