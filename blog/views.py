from django.http import HttpResponse,JsonResponse
from django.shortcuts import render


# Create your views here.
def blog_view(request):
    return render(request,'blog/blog-home.html')

def blog_single(request):
    context = {'title':'WARNING','content':'Oh shit here we go again'}
    return render(request,'blog/blog-single.html', context)