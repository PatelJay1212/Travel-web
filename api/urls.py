from django.contrib import admin
from django.urls import path,include
from api import views

urlpatterns = [
    path('',views.homeview,name='home'),
    path('registerview/',views.registerview,name='registerview'),
    path('loginview/',views.loginview,name='loginview'),
    path('add/',views.additem,name='add'),
    path('delete/',views.deleteitem,name='delete'),
    path('update/<int:id>',views.updateitem,name='update'),
]