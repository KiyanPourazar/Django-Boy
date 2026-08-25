from django.http import HttpResponse,JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from taggit.models import Tag
from blog.forms import CommentForm
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
# from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required(login_url='/accounts/login')
def blog_view(request, **kwargs):
    posts = Post.objects.filter(status=1)
    tags = Tag.objects.all()
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__title=kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username=kwargs['author_username'])
    if kwargs.get('tag_name') != None:
        posts = posts.filter(tags__name=kwargs['tag_name'])

    posts = Paginator(posts, 3)

    try:
        page_number = request.GET.get('page')
        posts = posts.page(page_number)
    except (PageNotAnInteger, EmptyPage):
        posts = posts.page(1)

    context = {
        'posts':posts,
        'tags':tags
    }

    return render(request,'blog/blog-home.html',context)

def blog_single(request, pid):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
           form.save()
           messages.success(request, "Your comment has been submitted.")
        else:
            messages.error(request, "Your comment has been submitted.")
    posts = Post.objects.filter(status=1)
    post = get_object_or_404(posts, pk=pid)

    if not post.login_required:
        comments = Comment.objects.filter(post=post.id, approved=True).order_by('-created_date')
        form = CommentForm()
        context = {'post': post, 'comments': comments, 'form': form}
        return render(request, 'blog/blog-single.html', context)
    else:
        if request.user.is_authenticated:
            comments = Comment.objects.filter(post=post.id, approved=True).order_by('-created_date')
            form = CommentForm()
            context = {'post': post, 'comments': comments, 'form': form}
            return render(request, 'blog/blog-single.html', context)
        else:
            return HttpResponseRedirect(reverse('accounts:login'))

def test(request, pid):
    # post = Post.objects.get(id=pid)
    post = get_object_or_404(Post, pk=pid)
    context = {'post':post}
    return render(request,'test.html',context)

def blog_category(request, cat_name):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__title=cat_name)
    context = {'posts':posts}
    return render(request, 'blog/blog-home.html', context)

def blog_search(request):
    posts = Post.objects.filter(status=1)
    # print(request.__dict__)
    if request.method == "GET":
        # print(request.GET.get('s'))
        if s := request.GET.get('s'):
            posts = posts.filter(content__contains=s)

    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)