from .views import *
from django.contrib import admin
from django.urls import path, include
from blog.feeds import LatestEntriesFeed


app_name = 'blog'

urlpatterns = [
    path('', blog_view, name='index'),
    path('<int:pid>', blog_single, name='single'),
    path('category/<str:cat_name>', blog_view, name='category'),
    # path('post-<int:pid>', test, name='test'),
    path('author/<str:author_username>', blog_view, name='author'),
    path('search/', blog_search, name='search'),
    path('tag/<str:tag_name>', blog_view, name='tag'),
    path('rss/feed/', LatestEntriesFeed()),
]
