from django.contrib import admin
from django.urls import path,include
from myuser import views

urlpatterns = [
    path('user_index/',views.user_index, name ='index'),
    path('tables/',views.data_table,name='tables'),
    path('tables/',views.data_table,name='tables'),
    path('user_destination/',views.user_destination,name='user_destination'),
    path('user_contact/',views.user_contact,name='user_contact'),
    path('user_mybooking/',views.user_mybooking, name='user_mybooking'),
    path('user_about/',views.user_about,name='user_about'),
    path('user_packages/',views.user_package,name='user_package'),
    path('user_team/',views.user_team,name='user_team'),
    path('user_service/<int:id>/',views.user_service,name='user_service'),
    path('user_testimonial/',views.user_testimonial,name='user_testimonial'),
    # path('search/', views.search_packages, name='search_packages'),
    path('package_detail/<int:id>/',views.package_detail,name='package_detail'),
    path('bookpackage/<int:id>/',views.book_package,name='bookpackage'),
    path('payment/<int:id>/',views.payment,name='payment'),
    path('loginviews/',views.loginviews,name='loginviews'),
    path('register/',views.register,name='register'),
    path('confirmed/<int:id>/',views.conf_book,name='confirmed'),
    path('pdf/',views.pdf,name='pdf'),
    path('searchpackages/',views.search_packages,name='searchpackages'),

    



]