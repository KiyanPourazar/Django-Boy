from .views import *
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('',index_home),
    path('about/',index_about),
    path('contact/',index_contact),

]