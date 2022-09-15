from django.contrib import admin
from django.urls import path 
from .import views

urlpatterns = [
    path('',views.index),
    # path('karan/',views.karan),
    path('search',views.search),
    path('search-action',views.search_action,name='search_action'),
    path('signup',views.signup),
    

]
