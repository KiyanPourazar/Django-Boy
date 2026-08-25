from .views import *
from django.contrib import admin
from django.urls import path, include
from blog.feeds import LatestEntriesFeed


app_name = 'accounts'

urlpatterns = [
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('signup', signup, name='signup'),
]