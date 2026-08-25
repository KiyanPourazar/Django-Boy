from .views import *
from django.contrib import admin
from django.urls import path, include
from blog.feeds import LatestEntriesFeed


app_name = 'accounts'

urlpatterns = [
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('signup', signup_view, name='signup'),
]