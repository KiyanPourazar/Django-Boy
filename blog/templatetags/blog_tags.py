from django import template
from blog.models import Post

register = template.Library()

@register.simple_tag(name='get_posts')
def get_posts():
    return Post.objects.filter(status=1)

@register.filter
def snippet(value,arg=200):
    return value[:arg] + "..."

