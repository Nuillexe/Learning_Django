from django.contrib import admin
from django.urls import path, include
from home.views import display_home

app='name'
urlpatterns=[
    path('',display_home,name='display_home')

]