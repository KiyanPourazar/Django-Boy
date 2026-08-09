from .views import *
from django.contrib import admin
from django.urls import path, include

app_name = 'website'

urlpatterns = [
    path('',index_home, name='index'),
    path('about/',index_about, name='about'),
    path('contact/',index_contact, name='contact'),
    path('test/', test_view, name='test'),
    path('elements/', elements_view, name='elements'),

]