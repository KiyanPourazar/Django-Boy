from django import template
from blog.models import Post

register = template.Library()

@register.simple_tag(name='get_posts')
def get_posts():
    return Post.objects.filter(status=1)

@register.filter
def snippet(value,arg=200):
    return value[:arg] + "..."

# @register.inclusion_tag('website/popularposts.html')
# def popularposts():
#     posts = Post.objects.filter(status=1).order_by('published_date')[:2]
#     return {'posts':posts}

@register.inclusion_tag('blog/blog-popular-posts.html')
def latest_posts(arg=3):
    posts = Post.objects.filter(status=1).order_by('published_date')[:arg]
    return {'posts':posts}