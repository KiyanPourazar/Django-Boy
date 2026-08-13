from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from blog.models import Post


# Create your views here.
def blog_view(request):
    posts = Post.objects.filter(status=1)
    context = {'posts':posts}
    return render(request,'blog/blog-home.html',context)

def blog_single(request):
    context = {'title':'WARNING','content':'Oh shit here we go again'}
    return render(request,'blog/blog-single.html', context)

def test(request):
    posts = Post.objects.filter(status=1)
    context = {'posts':posts}
    return render(request,'test.html',context)