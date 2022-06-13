#created urls file to add url config for the magazine app

from django.urls import path

from .views import Homepage, Createnew, Editt, Getdetail, Delette
from . import views

urlpatterns =[
    path('',Homepage.as_view(),name = 'home'),
    path('post/<int:pk>/', Getdetail.as_view(), name ='getdetail'),
    path('post/new', Createnew.as_view(), name = 'addnew'),
    path('post/<int:pk>/edit', Editt.as_view(), name='editer' ),
    path('post/<int:pk>/delete', Delette.as_view(), name='on_delete' ),
    path('about/',views.aboutpage,name = 'about'),
]