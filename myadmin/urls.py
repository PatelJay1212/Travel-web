from django.contrib import admin
from django.urls import path
from myadmin import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('trial/',views.trialview,name='trial'),
    path('index/',views.indexview,name='ad_index'),
    path('signup/',views.signupview,name='signup'),
    path('signin/',views.signinview,name='signin'),

    path('form/',views.formview,name='form'),
    path('form2/',views.form2view,name='form2'),

    # path('vr/',views.virtualview,name='virtual'),
    path('table/',views.tableview,name='table'),
    path('table2/',views.table2view,name='table2'),

    path('Categorydelete/<int:id>/',views.Categorydelete,name='Categorydelete'),
    path('Categoryedit/<int:id>/',views.Categoryedit,name='Categoryedit'),
    path('Categoryupdate/<int:id>/',views.Categoryupdate,name='Categoryupdate'),

    path('Packagesdelete/<int:id>/',views.Packagesdelete,name='Packagesdelete'),
    path('Packagesedit/<int:id>/',views.Packagesedit,name='Packagesedit'),
    path('Packagesupdate/<int:id>/',views.Packagesupdate,name='Packagesupdate'),


    # path('rtl/',views.rtlview,name='rtl'),
    # path('billing/',views.billingview,name='billing'),
    path('dashboard/',views.dashview,name='dashboard1'),
    path('elements/',views.eleview,name='elements'),
    path('logout/',views.logoutview,name='logout'),



]