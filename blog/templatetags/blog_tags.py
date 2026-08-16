from django import template
from blog.models import Post, Category

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

@register.inclusion_tag('blog/blog-latest-posts.html')
def latest_posts(arg=3):
    posts = Post.objects.filter(status=1).order_by('-published_date')[:arg]
    return {'posts':posts}

@register.inclusion_tag('blog/blog-post-categories.html')
def postcategories(arg=3):
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name]=posts.filter(category=name).count()

    return {'categories':cat_dict}
